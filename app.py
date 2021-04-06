
# import the necessary packages
from imutils.object_detection import non_max_suppression
import numpy as np
import pytesseract
import argparse
import cv2

from views.AuthView import AuthView
from controllers.AuthController import AuthController
from views.DetectionView import DetectionView

class MyApp:

    def run(self):
        av = AuthView()
        av.next = self.controllers
        av.load()



    def controllers(self):
        dv = DetectionView()
        dv.ocr('images/example_07.jpg')

    def printSomething(self):
        print("This is My App print function")


app = MyApp()
app.run()



