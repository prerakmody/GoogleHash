# def top100Vertical(verticalImages, inputImage):
#     top100 = []
#     for each in verticalImages:

#     pass


# if __name__ == "__main__":
#     top100 = {}
#     for verticalImage in enumerate(verticalImages):
#         top100[verticalImage.id] = top100Vertical(verticalImages, verticalImage)
    
#     return top100


import read, submit
import sys
import numpy as np 
import time
from operator import attrgetter
from collections import namedtuple
# slide = [photo] or [photo1, photo2]

def findInterestingScore(slide1, slide2):
    interestScore = 0
    
    slide1Tag = set()
    for pic1 in slide1:
       slide1Tag = set().union(slide1Tag, pic1.tags)

    slide2Tag = set()
    for pic2 in slide2:
        slide2Tag = set().union(slide2Tag, pic2.tags)

    interestScore = min(getCommonTagCount(slide1Tag, slide2Tag),
                        getFirstPicUnique(slide1Tag, slide2Tag),
                        getSecondPicUnique(slide1Tag, slide2Tag))
    
    return interestScore

def getCommonTagCount(slide1Tag, slide2Tag):
    return len(set(slide1Tag) & set(slide2Tag))

def getFirstPicUnique(slide1Tag, slide2Tag):
    return len(set(slide1Tag) - set(slide2Tag))

def getSecondPicUnique(slide1Tag, slide2Tag):
    return len(set(slide2Tag) - set(slide1Tag))

"""
def findMostInterestingPair(horizontal, vertical):
    for hphoto1 in horizontal:
        # find the most interesting horizontal
        for hphoto2 in horizontal:
            if (hphoto1 != hphoto2):
                findInterestingScore(hphoto1, hphoto2)

        # find the most interesting vertical pair
        for vphoto1 in vertical:
            for vphoto2 in vertical:
                if (vphoto1 != vphoto2):
                    findInterestingScore(hphoto1, vphoto1, vphoto2)


    slide1 = findFirstSlide(horizontal, vertical)
"""

# return the first slide or None if no slide can be created
def findFirstSlide(photos):
    if len(photos) == 0:
        return None

    if (photos[0].align == 'H'):
        return [photos[0]]
    
    for (i, photo) in enumerate(photos):
        if i > 0 and photo.align == 'V':
            return [photos[0], photo]

    return None

# divide photos by alignment
def dividePhotos(photos):
    horizontal = []
    vertical = []
    for pic in photos:
        if pic.align == 'H':
            horizontal.append(pic)
        else:
            vertical.append(pic)
            
    return horizontal, vertical

# find the slide of photos most interesting to slide1
def findMostInterestingSlide(slide1, horizontal, vertical, verbose=0):    

    topScore = -1
    topPhoto = []
    if verbose : print ('************')
    topSlide = None
    
    tic = 0
    if verbose:
        tic = time.time()
    # find most interesting horizontal slide
    for photo in horizontal:
        slide2 = [photo]
        score = findInterestingScore(slide1, slide2)
        if (score > topScore):
            topScore = score
            topSlide = slide2
            topPhoto   = [photo]
    if verbose : print ('Hor : ', time.time() - tic, 's')

    if verbose : tic = time.time()
    # print (len(vertical))

    if (len(vertical) >= 2):
        photo1 = vertical[0]
        for j in range(1, len(vertical[:10])):
            photo2 = vertical[j]
            slide2 = [photo1, photo2]
            score = findInterestingScore(slide1, slide2)
            if (score > topScore):
                topScore = score
                topSlide = slide2
                topPhoto = [photo1, photo2]
        if verbose: print ('Ver : ', time.time() - tic, 's')
    
    # Step3 : Removal Operation
    for each in topPhoto:
        
    return topSlide

# remove photos in slide from photos
def removeSlideFromPhotos(photos, slide):
    for photo in slide:
        photos.remove(photo)

def solve(photos):
    slideshow = []

    slide1 = findFirstSlide(photos)
    slideshow.append(slide1)
    horizontal, vertical = dividePhotos(photos)
    vertical = sorted(vertical, key=attrgetter('tagCount'))
    removeSlideFromPhotos(photos, slide1)

    i = 0
    while (findFirstSlide(photos) != None):        
        i = i + 1
        #print(i)
        slide2 = findMostInterestingSlide(slide1, horizontal, vertical, 1)
        slideshow.append(slide2)
        removeSlideFromPhotos(photos, slide2)

        slide1 = slide2

    return slideshow


filename = sys.argv[1]
N, photos = read.read(filename)
slideshow = solve(photos)

# print('slideshow')
# print(slideshow)

# print('submit')
submit.submit(slideshow)


