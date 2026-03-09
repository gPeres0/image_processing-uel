import numpy as np
import cv2 as cv

img = cv.imread('../img/Lenna_gray.jpg', cv.IMREAD_GRAYSCALE)

altura = img.shape[0]
largura = img.shape[1]

cv.imshow('imagem',img)
cv.waitKey(0)
cv.destroyAllWindows()