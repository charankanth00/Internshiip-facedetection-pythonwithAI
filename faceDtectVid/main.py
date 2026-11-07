import cv2

train_face_model = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

vid = cv2.VideoCapture(0)

while True:

    #while successframe :
    successframe,frame = vid.read()
    successframe = True
    gra_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coord = train_face_model.detectMultiScale(gra_img)
    for (x, y, w, h) in face_coord:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 00), 2)
    cv2.imshow("face detect program", frame)
    cv2.waitKey(1)

"""


face_coord = train_face_model.detectMultiScale(gra_img)

(x, y, w, h) = face_coord[1]
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 00), 2)


"""
print("finished")
