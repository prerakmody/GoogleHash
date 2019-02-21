def sortNearestCacheForEndpoint(endpoint):
    sorted_cache = endpoint.cache_servers
    sorted_cache = sorted(sorted_cache, key=lambda x: x[1])
    return sorted_cache

def calculateScore(caches_state, requests, endpoints):
    totalScore = []
    totalrequests = 0
    for request in requests:
        request_vid         = request[0]
        request_endpoint_id = request[1]
        request_vidcount    = request[2]
        totalrequests      += request_vidcount

        latency_endpoint_dc = endpoints[request_endpoint_id].latency

        endpoint = endpoints[request_endpoint_id]

        ##  sort the caches
        #print ('******************************')
        sorted_caches = sortNearestCacheForEndpoint(endpoint)
        for cache_obj in sorted_caches: #[[vid, vid], [vid, vid], [] ...]
            cache_obj_id = cache_obj[0]            
            #print ('Cache : ', cache_obj, ' || Vid : ', request_vid)

            if request_vid in caches_state[cache_obj_id]:
            # if request_vid in used_cache:
                #print ('Cache ID : ', cache_obj_id)
                #print('Cache Server : ', endpoints[request_endpoint_id]['cache_servers'])
                #cache_server = [x for x in endpoints[request_endpoint_id]['cache_servers'] if x[0] == used_cache_id][0]
                #print('Cache Server : ', cache_server)
                
                latency_cache = cache_obj[1]
                totalScore.append((latency_endpoint_dc - latency_cache) * request_vidcount)

    return (1000 * sum(totalScore) / totalrequests )
