import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError('Não foi possível abrir a câmera')

print("Pressione 'x' para salvar foto1.png ou 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        print('Não foi possível receber o frame. Encerrando...')
        break

    cv.imshow('frame', frame)
    key = cv.waitKey(1) & 0xFF

    if key == ord('x'):
        cv.imwrite('foto1.png', frame)
        print("Imagem salva como 'foto1.png'.")
    elif key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
