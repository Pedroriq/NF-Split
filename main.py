import cv2 as cv

# Carregue o classificador pré-treinado para detecção de faces
face_cascade = cv.CascadeClassifier('hand.xml')

# Inicie a captura de vídeo da câmera (0 representa a câmera padrão)
cap = cv.VideoCapture(0)

while True:
    # Leia um frame do vídeo
    ret, frame = cap.read()
    print(f'{ret} - {frame}')
    # Converta o frame para escala de cinza para a detecção de faces
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detecte faces no frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenhe retângulos ao redor das faces detectadas
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Exiba o frame resultante
    cv.imshow('Detectando Rostos', frame)

    # Saia do loop se a tecla 'q' for pressionada
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Libere os recursos
cap.release()
cv.destroyAllWindows()