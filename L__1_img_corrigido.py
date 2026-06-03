import cv2 as cv

# Leitura em escala de cinza: flag 0 ou cv.IMREAD_GRAYSCALE
img_gray = cv.imread('messi5.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('Imagem em escala de cinza', img_gray)
cv.waitKey(0)
cv.destroyAllWindows()

# Leitura colorida: flag 1 ou cv.IMREAD_COLOR
img_color = cv.imread('messi5.jpg', cv.IMREAD_COLOR)
cv.imshow('Imagem colorida', img_color)
k = cv.waitKey(0) & 0xFF

if k == 27:  # ESC
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('messi_colorida.png', img_color)
    cv.destroyAllWindows()
