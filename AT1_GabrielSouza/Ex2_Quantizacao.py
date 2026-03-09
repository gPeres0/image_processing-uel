import numpy as np
import cv2 as cv

def quantize_grayscale(img, levels):
    step = 256 // levels
    quantized = (img // step) * step
    return quantized.astype(np.uint8)

img = cv.imread('../img/Lenna_gray.jpg', cv.IMREAD_GRAYSCALE)

quant_128 = quantize_grayscale(img, 128)
quant_64 = quantize_grayscale(img, 64)
quant_32 = quantize_grayscale(img, 32)
quant_16 = quantize_grayscale(img, 16)
quant_8 = quantize_grayscale(img, 8)
quant_4 = quantize_grayscale(img, 4)
quant_2 = quantize_grayscale(img, 2)

cv.imshow('original', img)
cv.imshow('128 levels', quant_128)
cv.imshow('64 levels', quant_64)
cv.imshow('32 levels', quant_32)
cv.imshow('16 levels', quant_16)
cv.imshow('8 levels', quant_8)
cv.imshow('4 levels', quant_4)
cv.imshow('2 levels', quant_2)
cv.waitKey(0)