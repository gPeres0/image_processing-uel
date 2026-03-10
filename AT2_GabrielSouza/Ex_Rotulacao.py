import cv2 as cv
import numpy as np

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def basicLabeling(thresh):
    rows, cols = thresh.shape
    label = 1
    labeled = np.zeros_like(thresh, dtype=np.int32)

    for i in range(rows):
        for j in range(cols):
            if thresh[i, j] > 0:
                labeled[i, j] = label
                label += 1

    changed = True
    while changed:
        changed = False
        # Cima pra baixo, esquerda pra direita
        for i in range(rows):
            for j in range(cols):
                min_label = labeled[i, j]

                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < rows and 0 <= ny < cols and labeled[nx, ny] > 0:
                        if labeled[nx, ny] < min_label:
                            min_label = labeled[nx, ny]
                
                if min_label < labeled[i, j]:
                    labeled[i, j] = min_label
                    changed = True
        
        # Baixo pra cima, direita pra esquerda
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if labeled[i, j] > 0:
                    min_label = labeled[i, j]
                    
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < rows and 0 <= ny < cols and labeled[nx, ny] > 0:
                            if labeled[nx, ny] < min_label:
                                min_label = labeled[nx, ny]
                    
                    if min_label < labeled[i, j]:
                        labeled[i, j] = min_label
                        changed = True
    
    return labeled

    

def bfsLabeling(thresh):
    rows, cols = thresh.shape
    label = 1
    labeled = np.zeros_like(thresh, dtype=np.int32)
    visited = np.zeros_like(thresh, dtype=bool)
    
    for i in range(rows):
        for j in range(cols):
            if thresh[i, j] > 0 and not visited[i, j]:
                queue = [(i, j)]
                visited[i, j] = True
                labeled[i, j] = label
                while queue:
                    x, y = queue.pop(0)
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and thresh[nx, ny] > 0 and not visited[nx, ny]:
                            visited[nx, ny] = True
                            labeled[nx, ny] = label
                            queue.append((nx, ny))
                label += 1
    
    return labeled

img = cv.imread('../img/Lenna_gray.jpg', cv.IMREAD_GRAYSCALE)
ret, thresh = cv.threshold(img, 128, 255, cv.THRESH_OTSU)

basic_labeled = basicLabeling(thresh)
bfs_labeled = bfsLabeling(thresh)

cv.imshow('original', img)
cv.imshow('thresholded', thresh)
cv.imshow('basic', (basic_labeled * 32).astype(np.uint8))
cv.imshow('bfs', (bfs_labeled * 32).astype(np.uint8))
cv.waitKey(0)
cv.destroyAllWindows()
