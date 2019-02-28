import read, submit2
import sys
import numpy as np 
import time
from operator import attrgetter
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
def findMostInterestingSlide(slide1, horizontal, vertical, verbose=0, limit=50):
    #if verbose : print("photos=" + str(len(photos)))
    
    topScore = -1
    topSlide = None
    
    if verbose : print("a")
    tic = 0
    if verbose:
        tic = time.time()
    # find most interesting horizontal slide
    for i in range(0, min(len(horizontal), limit)):
        photo = horizontal[i]
        slide2 = [photo]
        score = findInterestingScore(slide1, slide2)
        if (score > topScore):
            topScore = score
            topSlide = slide2
    if verbose : print (time.time() - tic, 's')


    if verbose : print("b")
    if verbose : tic = time.time()
    # find most interesting vertical slide
    #vertical = sorted(vertical)
    #vertical = vert(1:100)
    #for i in range(0, len(vertical)):
        #photo1 = vertical[i]
    if (len(vertical) >= 2):
        photo1 = vertical[0]
        for j in range(1, min(len(vertical), limit)):
            photo2 = vertical[j]
            slide2 = [photo1, photo2]
            score = findInterestingScore(slide1, slide2)
            if (score > topScore):
                topScore = score
                topSlide = slide2
        if verbose: print (time.time() - tic, 's')
    return topSlide, topScore

# remove photos in slide from photos
def removeSlideFromPhotos(photos, slide):
    for photo in slide:
        try:
            photos.remove(photo)
        except ValueError:
            pass

def solve(photos, verbose):
    slideshow = []

    horizontal, vertical = dividePhotos(photos)

    vertical = sorted(vertical, key=attrgetter('tagCount'), reverse=True)
    horizontal = sorted(horizontal, key=attrgetter('tagCount'), reverse=True)

    slide1 = findFirstSlide(photos)
    slideshow.append(slide1)
    removeSlideFromPhotos(photos, slide1)
    removeSlideFromPhotos(horizontal, slide1)
    removeSlideFromPhotos(vertical, slide1)

    i = 0
    while (findFirstSlide(photos) != None):        
        i = i + 1        
        slide2, score = findMostInterestingSlide(slide1, horizontal, vertical, 0, 50)
        if verbose: print("slide: " + str(i) + ", score: " + str(score) + ", remaining photos: " + str(len(photos)))
        slideshow.append(slide2)
        removeSlideFromPhotos(photos, slide2)
        removeSlideFromPhotos(horizontal, slide2)
        removeSlideFromPhotos(vertical, slide2)

        slide1 = slide2

    return slideshow



# print('slideshow')
# print(slideshow)

# print('submit')

##############################################

if len(sys.argv) == 3:
    filename_ip = sys.argv[1]
    filename_op = sys.argv[2]
    N, photos = read.read(filename_ip)
    slideshow = solve(photos, verbose=1)
    submit2.submit(slideshow, filename_op)
else:
    print ('Not enough arguments!')
