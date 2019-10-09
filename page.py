#!/usr/bin/python
import cv2

class live_image():
    def __init__(self):

        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    def video_eyes(self):
        self.cap = cv2.VideoCapture(0)
        while True:
            self.ret, self.frame = self.cap.read()
            self.frame = cv2.resize(self.frame, (750, 550))
            self.eyes = self.eye_cascade.detectMultiScale(self.frame, 1.1, 14)
            for (ex, ey, ew, eh) in self.eyes:
                cv2.rectangle(self.frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            cv2.imshow('Eyes only', self.frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()

    def video_face(self):
        self.cap = cv2.VideoCapture(0)
        while True:
            self.ret, self.frame = self.cap.read()
            self.frame = cv2.resize(self.frame, (750, 550))
            self.face = self.face_cascade.detectMultiScale(self.frame, 1.3, 5)
            for (x, y, w, h) in self.face:
                cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            cv2.imshow('Face only', self.frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()

    def face_eyes(self):
        self.cap = cv2.VideoCapture(0)
        while True:
            self.ret, self.frame = self.cap.read()
            self.frame = cv2.resize(self.frame, (750, 550))
            self.face = self.face_cascade.detectMultiScale(self.frame, 1.3, 5)

            for (x, y, w, h) in self.face:
                cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            self.eyes = self.eye_cascade.detectMultiScale(self.frame, 1.3, 10)
            for (ex, ey, ew, eh) in self.eyes:
                cv2.rectangle(self.frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            cv2.imshow('Eyes and Face', self.frame)
            if cv2.waitKey(1) & 0xFF == ord('q') :
                break

        self.cap.release()
        cv2.destroyAllWindows()
