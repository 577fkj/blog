import PIL.Image
import os
import cv2

filename = os.getcwd() + "\\logo.png"
im = PIL.Image.open(filename)
rootdir = os.getcwd()
list = os.listdir(rootdir)
for i in range(0,len(list)):
    path = os.path.join(rootdir,list[i])
    if os.path.isfile(path):
        if list[i][-3:] == 'png':
            im = PIL.Image.open(filename)
            img = cv2.imread(path)
            size = img.shape[:2]
            im = im.resize(size, PIL.Image.LINEAR)
            im.save(path)