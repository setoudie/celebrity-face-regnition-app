from deepface import DeepFace
import matplotlib.pyplot as plt
import numpy as np
import cv2

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

faces = DeepFace.extract_faces('seny_ucad.jpg', detector_backend=backends[1], enforce_detection=False)
# print(len(faces))

img_array = faces[0]['face']

# initiale face shape (73, 73, 3)
print(img_array.shape)

# Transform shape to a good shape --> (224, 224, 3)
resize_img_array = cv2.resize(img_array, (224, 224))

print(resize_img_array.shape)

# img_face = np.squeeze(faces[0]['face'].shape)
# print(img_face.shape)
plt.imshow(resize_img_array)
plt.show()