import cv2 # импортируем библиотеку компьютерного зрения opencv

eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml") #тут используются уже готовые каскады для определения глаз
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #каскад для определения лица

cap = cv2.VideoCapture(0) #переменная в которой хранится камера

while True:  # бесконечный цикл так как видео состоит из множества изображений
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame,
                        cv2.COLOR_BGR2GRAY)  # преобразует изображение в оттенки серого так как программе так лечге работать
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3,
                                          minNeighbors=5)  # Применяет метод обнаружения лица в изображении
    eyes = eye_cascade.detectMultiScale(gray)  # Применяет метод обнаружения глаз в изображении

    if len(faces) > 0 and len(eyes) > 0:  # Проверяет, есть ли обнаруженные лица и глаза
        cv2.putText(frame, "no sleep", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                    2)  # Наносит текст "no sleep" на кадр
    else:  # Параметры определяют положение, шрифт, масштаб, цвет и толщину текста
        cv2.putText(frame, "maybe sleep", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),
                    2)  # Наносит текст "maybe sleep"

    cv2.imshow('Video Stream', frame)  # Отображает обработанный кадр

    if cv2.waitKey(1) & 0xFF == ord('q'):  # если была нажата клавиша q то программа закрывается
        break

cap.release() #освобождает ресурсы
cv2.destroyAllWindows() #закрывает все окна