import read, score
import sys
from tqdm import tqdm
import numpy as np 


def sortRequestBySavedTime(requests, endpoint_caches, caches_state):
    requests_tmp    = {}
    requests_sorted = []
    for request_id, request in enumerate(requests): #request = [vid, endpoint, requestcount]
        request_vid         = request[0]
        request_endpoint_id = request[1]
        request_vidcount    = request[2]

        latency_endpoint_dc        = endpoints[request_endpoint_id]['latency']
        latency_endpoint_bestcache = endpoint_caches[request_endpoint_id][0][0]

        latency_endpoint_bestserver = latency_endpoint_dc
        for cache in endpoint_caches[request_endpoint_id]:
            if request_vid in caches_state[cache[0]]:
                latency_endpoint_bestserver = cache[1]
                break

        #request_savedtime          = request_vidcount*(latency_endpoint_dc - latency_endpoint_bestserver)
        request_savedtime          = request_vidcount*(latency_endpoint_bestserver - latency_endpoint_bestcache)
        #request_savedtime          = request_vidcount*(latency_endpoint_dc - latency_endpoint_bestcache)
        
        requests_tmp[request_id]   = request_savedtime
    
    requests_tmp = sorted(requests_tmp.items(), key=lambda kv: kv[1], reverse=True) # [[req_id, saved_time]]

    for request_obj in requests_tmp:
        requests_sorted.append(requests[request_obj[0]])
    
    return requests_sorted

def sortNearestCacheForEndpoint(endpoint):
    sorted_cache = list(endpoint['cache_servers'])
    sorted_cache = sorted(sorted_cache, key=lambda x: x[1])
    return sorted_cache

# return space available in cache
def cache_free_size(video_sizes, video_ids, cache_capacity):
    
    space_available = cache_capacity    
    for id in video_ids:
        space_available = space_available - video_sizes[id] 

    return space_available

def cacheRequest(videos, caches, endpoint_caches, request):
    video = request[0]
    endpoint = request[1]
    requests_count = request[2]

    for cache in endpoint_caches[endpoint]:
        if cache_free_size(videos, caches[cache[0]], cache_capacity) >= videos[video]:
            # video is already cached here
            if video in caches[cache[0]]:
                return True

            caches[cache[0]].append(video)
            return True
    
    return False


def solve(cache_count, cache_capacity, videos, endpoints, requests):
    # arrays of videos in caches
    caches_state = [[] for i in range(cache_count)]

    requests = list(requests)

    # sort cache servers for each endpoint by latency (save time) 
    endpoint_caches = []
    for endpoint in endpoints:
        endpoint_caches.append(sortNearestCacheForEndpoint(endpoint))

    print ('[Init] Done!')

    while True:
        #print("while")

        continueLoop = False

        requests_sorted = sortRequestBySavedTime(requests, endpoint_caches, caches_state)
        # iterate over requests and try to cache them
        with tqdm(total=len(requests_sorted)) as pbar:
            for request in requests_sorted:
                pbar.update(1)
                # add video to the closest cache to the request endpoint with enough free space
                if cacheRequest(videos, caches_state, endpoint_caches, request):
                    requests.remove(request)
                    continueLoop = True
                    break

        # not able to cache any request => we are done
        if not continueLoop:
            break

    return caches_state





filename = sys.argv[1]
(cache_count, cache_capacity, videos, endpoints, requests) = read.read(filename)

caches_state = solve(cache_count, cache_capacity, videos, endpoints, requests)

# SCORE
score = score.calculateScore(caches_state, requests, endpoints)
#print(caches_state)
print(requests)
#print(endpoints)
print("SCORE = " + str(score))

# SUBMISSION FORMAT
used_caches = [(i, cache) for i, cache in enumerate(caches_state) if len(cache) > 0]
# print(len(used_caches))
# for i, cache in used_caches:
#     print(str(i) + " " + " ".join(str(x) for x in cache))