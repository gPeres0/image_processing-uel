import cv2 as cv
import numpy as np

def downsample(img, new_size):
    h, w = img.shape[:2]
    nh, nw = new_size
    row_idx = (np.linspace(0, h-1, nh)).astype(int)
    col_idx = (np.linspace(0, w-1, nw)).astype(int)
    return img[np.ix_(row_idx, col_idx)]

img = cv.imread('../img/Lenna_gray.jpg', cv.IMREAD_GRAYSCALE)

size_256 = (256, 256)
size_128 = (128, 128)
size_64 = (64, 64)
size_32 = (32, 32)

cv.imshow('original', img)
cv.imshow('resized_1', downsample(img, size_256))
cv.imshow('resized_2', downsample(img, size_128))
cv.imshow('resized_3', downsample(img, size_64))
cv.imshow('resized_4', downsample(img, size_32))
cv.waitKey(0)
