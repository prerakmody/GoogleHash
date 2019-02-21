import numpy as np
import collections

Endpoint = collections.namedtuple('Endpoint', 'latency cache_count cache_servers')

def read(ip_file):
    file = open(ip_file, 'rb')
    line = file.readline()

    main_videos      = int(line.split(' ')[0])
    main_endpoints   = int(line.split(' ')[1])
    main_requests     = int(line.split(' ')[2])
    main_cacheservers = int(line.split(' ')[3])
    main_capacityserver = int(line.split(' ')[4].split('\n')[0])

    #print ('Video COunt : ', main_videos)
    #print ('Endpoints : ', main_endpoints)
    #print ('Requests : ', main_requests)
    #print ('Cache Servers : ', main_cacheservers)
    #print ('Max Server Capacity : ', main_capacityserver)

    line = file.readline().split(' ')
    main_videosizes = [int(each) for each in line] # Size in MB
    #print ('')
    #print ('Video Sizes : ', main_videosizes[1:10], ' ....')
    #print ('Video Count : ', len(main_videosizes))

    main_endpoint_list = []
    for endpoint_idx in range(main_endpoints):
        endpoint_tmp = [int(each) for each in file.readline().split(' ')]
        endpoint_tmp = Endpoint(latency=endpoint_tmp[0], cache_count=endpoint_tmp[1], cache_servers=[])
        for cache_idx in range(endpoint_tmp.cache_count):
            tmp = [int(each) for each in file.readline().split(' ')]
            endpoint_tmp.cache_servers.append(tmp)

        main_endpoint_list.append( endpoint_tmp )
        
    
    rand_idx = np.random.randint(100)
    #print ('Endpoints : ', main_endpoint_list[rand_idx]['latency'], main_endpoint_list[rand_idx]['cache_count'], main_endpoint_list[rand_idx]['cache_servers'][1:10], ' ...')
    #print ('Endpoint Count : ', len(main_endpoint_list))

    main_requests_list = []
    for req_idx in range(main_requests):
        main_requests_list.append([int(each) for each in file.readline().split(' ')])
    
    #print ('')
    #print ('Total Requests : ', len(main_requests_list))
    #print ('SAmple request : ', main_requests_list[1:3], '...')

    
    
    return (main_cacheservers, main_capacityserver, main_videosizes, main_endpoint_list, main_requests_list)

if __name__ == "__main__":
    data = read('input/kittens.in.txt');