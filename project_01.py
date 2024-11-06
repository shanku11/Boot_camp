from heapq import merge

from  PIL import ImageTk, Image
import cv2
inputimage=cv2.imread("shanku.jpg")
blue,green,red=cv2.split(inputimage)
img=cv2.merge((red,green,blue))
im = Image.fromarray(img)
haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 2)
for (x, y, w, h) in faces_rect:
    outputimage=cv2.rectangle(inputimage, (x, y), (x + w, y + h), (0, 255, 0), 10)
#cv2.imshow('Detected faces', inputimage)
outputimage = cv2.merge((red,green,blue))
lue,green,red = cv2.split(outputimage)

oim=Image.fromarray(outputimage)
image3 = oim.resize((300, 300))
image3 = ImageTk.PhotoImage(image3)
