"""
I got sick of saving ifunny.co images and having to crop out the stupid
watermark on the bottom every single time. I made the folder that ifunny saves
images to auto-sync with a folder in my google drive every 5 minutes, then every
hour or so I have this program run on my computer automatically, whether or not
I'm logged on. This program will analyze every .jpg and .png for a watermark.
If it detects a watermark, it will crop the meme by the amount of pixels in a
watermark. Everything else it will leave alone. These cropped memes are then
synced back with my phone every 5 minutes, where they are backed up to my Google
photos.
"""
from PIL import Image, ImageFilter, ImageChops
from config import *
import os

template = Image.open(templateLocation).convert('RGB')
#template.show() # debug only


for filename in os.listdir(driveLocation):
    imageLocation = os.path.join(driveLocation, filename)

    #if the image is a .png or .jpg...
    if filename.endswith(".jpg") or filename.endswith(".png"):
        #load the image
        im = Image.open(imageLocation)
        #the dimensions of the location where the watermark would be to analyze it
        box = (im.size[0] - 141, im.size[1] - 17, im.size[0], im.size[1]) # template is 141 x 17px
        #the part of the image that may contain a watermark
        watermarkRegion = im.crop(box).convert('RGB')
        #the pixel differences, 2 exactly same images would have a color difference of 0
        diff = ImageChops.difference(template, watermarkRegion)
        #print(len(diff.getcolors(9999)))
        #unfortunately the difference is usually a lot higher than 0, but not to worry, I haven't yet had a mistake using 1750 as the bar
        if len(diff.getcolors(9999)) > 1750:
            #print("no watermark detected") #debug only
            os.rename(imageLocation , os.path.join(croppedLocation, filename))
        else:
            #print("watermark detected") #debug only
            noWatermarkRegion = (0, 0, im.size[0], im.size[1] - 21)
            cropped = im.crop(noWatermarkRegion)
            cropped.save(os.path.join(croppedLocation, filename))

    #delete old
    os.remove(imageLocation)
