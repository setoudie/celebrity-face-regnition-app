from deepface import DeepFace
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image

backends = [
  'opencv',
  'ssd',
  'dlib',
  'mtcnn',
  'fastmtcnn',
  'retinaface',
  'mediapipe',
  'yolov8',
  'yunet',
  'centerface',
]

alignement_modes =[True, False]

def extract_faces(img_path):
  faces = DeepFace.extract_faces(img_path, detector_backend=backends[0], enforce_detection=False)

  all_faces = []
  for i in range(len(faces)):
    img_array = faces[i]['face']
    resize_img_array = cv2.resize(img_array,(224,224))
    all_faces.append(resize_img_array)
    img_array = []
    resize_img_array = []
  return all_faces


detected_faces = extract_faces('my_team_gray.png')
print(len(detected_faces))

for face in detected_faces:
  plt.imshow(face)
  plt.show()