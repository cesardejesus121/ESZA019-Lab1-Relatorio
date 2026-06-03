import time
import cv2 as cv

cap = cv.VideoCapture('big_buck_bunny.mp4')

if not cap.isOpened():
    raise RuntimeError('Não foi possível abrir o vídeo big_buck_bunny.mp4')

fps_video = cap.get(cv.CAP_PROP_FPS)
intervalo_normal = 1 / fps_video if fps_video > 0 else 1 / 25.0

# Altere este fator:
# fator_velocidade > 1 deixa mais rápido; fator_velocidade < 1 deixa mais lento.
fator_velocidade = 1.0
intervalo = intervalo_normal / fator_velocidade

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv.imshow('frame', frame)
    time.sleep(intervalo)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
