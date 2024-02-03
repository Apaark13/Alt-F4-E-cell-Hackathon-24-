import cv2
import numpy as np
from htr import HandwrittenTextRecognizer

# Load the image
img = cv2.imread('handwritten.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a HandwrittenTextRecognizer object
htr = HandwrittenTextRecognizer()

# Recognize the text in the image
text = htr.recognize(gray)

print(text)