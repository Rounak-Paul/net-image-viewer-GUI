import numpy as np
import cv2

img = cv2.imread('1.jpg')

import netmod.netmod.imageprocessing as ip


# blue, green, red = cv2.split(img)

# # We create a dummy 3D array
# blue_channel = np.zeros(img.shape, img.dtype)
# green_channel = np.zeros(img.shape, img.dtype)
# red_channel = np.zeros(img.shape, img.dtype)


# cv2.mixChannels([blue, green, red], [blue_channel], [0,0])
# cv2.mixChannels([blue, green, red], [green_channel], [1,1])
# cv2.mixChannels([blue, green, red], [red_channel], [2,2])

# blue = blue/255 - 0.8
# red = red/255 - 0
# green = green/255 - 0


# img = cv2.merge((blue, green, red))

# cv2.imshow('a',img)

# print(blue)

# rgb = np.array([255,255,100])

# r = 255 - rgb[2]
# g = 255 - rgb[1]
# b = 255 - rgb[0]

# # We create a dummy 3D array
# blue_channel = np.zeros(img.shape, img.dtype)
# green_channel = np.zeros(img.shape, img.dtype)
# red_channel = np.zeros(img.shape, img.dtype)

# blue_channel = blue_channel + b
# green_channel = green_channel + g
# red_channel = red_channel + r

# print(red_channel)

# blue, green, red = cv2.split(img)

# blue = blue - blue_channel
# green = green - green_channel
# red = red - red_channel

# img = img - blue_channel
# img = img - green_channel
# img = img - red_channel

# blue = blue - b
# green = green - g
# red = red - r

# img = cv2.merge((blue, green, red))

# cv2.imshow('img',img)
cv2.imshow('img',ip.layerExtractSlider(img,np.array([255,255,255])))
cv2.waitKey(0)