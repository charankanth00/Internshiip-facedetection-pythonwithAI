import cv2
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

train_face_model = cv2.CascadeClassifier(
    cv2.data.haarcascades
    + "haarcascade_frontalface_default.xml")

img = cv2.imread(os.path.join(BASE_DIR, 'img.jpg'))

gra_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coord = train_face_model.detectMultiScale(gra_img)
#print(gra_img)
print(face_coord)
count=0

print(count)
(x, y, w, h) = face_coord[0]
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 00), 2)
(x, y, w, h) = face_coord[1]
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 170, 00), 2)
train_face_model = cv2.CascadeClassifier(
    cv2.data.haarcascades
    + "haarcascade_frontalface_default.xml")



gra_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imagestring = train_face_model.detectMultiScale(gra_img)
#print(gra_img)
print(face_coord)
count=0

print(count)
(x, y, w, h) = face_coord[0]
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 00), 2)
(x, y, w, h) = face_coord[1]
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 170, 00), 2)


cv2.imshow("face detect program",img)
ch = cv2.waitKey()
if(ch == ord('s')):
    #save image
    pass
else:
    #delete image
    pass
print("finished")
