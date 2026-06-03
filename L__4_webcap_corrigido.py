import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError('Não foi possível abrir a câmera')

width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# FPS adequado para webcam e para reprodução posterior.
fps = 10.0

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('saida.avi', fourcc, fps, (width, height))

print("Pressione 'q' para encerrar a gravação.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print('Não foi possível receber o frame. Encerrando...')
        break

    # Qualquer processamento deveria ser feito aqui, antes de exibir e gravar.
    # Exemplo: frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    out.write(frame)          # grava a imagem normal, sem inversão vertical
    cv.imshow('frame', frame)

    if cv.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()
