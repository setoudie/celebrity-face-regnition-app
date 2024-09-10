import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# import face_recognition
from deepface import DeepFace

result = DeepFace.verify("gning.jpg","gning1.jpg")
print(result)

img_path = 'images/train/arnold_schwarzenegger/400px-Arnold_Schwarzenegger_(9048849809).jpg'

# Fonction pour visualiser une image avec matplotlib
def plot_image(path):
    """
        :param path: Chemin de l'image
        :return: None

        Cette fonction lis et affiche une image avec matplotlib
    """
    img = mpimg.imread(path)
    plt.imshow(img)
    plt.show()

# Fonction pour visualiser une image avec OpenCV
def show_image_with_cv2(path):
    """
        :param path: Chemin de l'image
        :return: None

        Cette fonction utilise cv2 de Opencv pour afficher une image
    """
    img = cv2.imread(path)
    cv2.imshow("Image", img)
    cv2.waitKey(0)

plot_image(img_path)
# show_image_with_cv2(img_path)

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

alignment_modes = [True, False]

face_objs = DeepFace.extract_faces(
  img_path = "my_team.png",
  detector_backend = backends[4],
  align = alignment_modes[0],
)