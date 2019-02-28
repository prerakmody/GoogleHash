import numpy as np
import collections

# globalEntity = collections.namedtuple('globalEntity', 'field1 field2 field3 field4 field5')
# subEntity1   = collections.namedtuple('subEntity1', 'field1 field2 field3')
# subEntity2   = collections.namedtuple('subEntity2', 'field1 field2 field3')
# subEntity3   = collections.namedtuple('subEntity3', 'field1 field2 field3')

photo = collections.namedtuple('photo', 'id align tagCount tags')

def read(ip_file, verbose=0):
    file = open(ip_file, 'rb')
    line = file.readline()
    N = int(line)
    # print ('Album has N = ', N, ' photos')

    ########################################## Top Line
    photos = []
    for i in range(N):
        line = file.readline()
        photoAlign = line.split(' ')[0]
        photoTagCount = int(line.split(' ')[1])
        photoTags     = line[:-1].split(' ')[2:]
            
        photos.append(photo(id=i, align=photoAlign, tagCount=photoTagCount, tags = photoTags))
        if i < -1 and verbose==1:
            print ('*************')
            print ('photoAlign : ', photoAlign)
            print ('photoTagCount : ', photoTagCount)
            print ('photoTags : ', photoTags)

    if verbose:
        for i in range(2):
            print ('***********************************************')
            idx = np.random.randint(N)
            #print (photos[idx].align)
            #print (photos[idx].tagCount)
            #print (photos[idx].tags)
            print (photos[idx])

    return N, photos

# def findCommonTags(photo1, photo2):
#     return set(photo1.tags + photo2.tags)

# def findScore(photo1, photo2):
#     pass
#     # photo1 - photo2




if __name__ == "__main__":
    # read('ip/a_example.txt', verbose=1) #4
    # read('ip/b_lovely_landscapes.txt', verbose=1) # 80000
    # read('ip/c_memorable_moments.txt', verbose=1) #1000
    read('ip/d_pet_pictures.txt', verbose=1) # 90000
    read('ip/e_shiny_selfies.txt', verbose=1) # 80000

"""
from operator import attrgetter
from collections import namedtuple

Person = namedtuple('Person', 'name age score')
seq = [Person(name='nick', age=23, score=100),
       Person(name='bob', age=25, score=200)]

sorted(seq, key=attrgetter('name'))

set(['r', 'a', 't'] + ['r', 'a', 'p'])
Intersection : set(a) & set(b)
Union : set().union(a,b)
Diff : set(a) - set(b)
"""