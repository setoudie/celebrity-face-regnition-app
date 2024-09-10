from deepface import DeepFace
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
import os

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


# Fonction pour détecter et extraire les visages d'une image
def extract_faces(img_path):
  """
  Cette fonction utilise DeepFace pour détecter les visages dans une image, puis redimensionne
  chaque visage détecté à une taille de 224x224 pixels.

  :param img_path: str
      Chemin vers l'image à partir de laquelle les visages seront extraits.

  :return: list
      Retourne une liste contenant des tableaux numpy pour chaque visage détecté, redimensionné à (224, 224).

  Exemple d'utilisation :
  ----------------------
  faces = extract_faces("chemin/vers/image.jpg")

  Détails :
  --------
  1. La fonction détecte les visages dans l'image spécifiée à l'aide de DeepFace.
  2. Chaque visage détecté est contenu dans un dictionnaire avec plusieurs informations, telles que :
      - `face['face']` : Tableau numpy représentant l'image du visage détecté.
      - `face['facial_area']` : Coordonnées délimitant la région du visage (yeux, nez, bouche, etc.).
      - `face['confidence']` : Niveau de confiance de la détection (pas utilisé explicitement ici).
  3. Les visages sont ensuite redimensionnés à une taille standard de 224x224 pixels à l'aide d'OpenCV.
  4. Chaque visage redimensionné est ajouté à la liste `all_faces` qui est retournée par la fonction.

  Notes :
  ------
  - `enforce_detection=False` permet à la fonction de continuer même si aucun visage n'est détecté.
  - `detector_backend` : Le backend de détection des visages utilisé par DeepFace est défini dans la variable `backends[0]`.
  """

  faces = DeepFace.extract_faces(img_path, detector_backend=backends[0], enforce_detection=False)

  all_faces = []
  for i in range(len(faces)):
    img_array = faces[i]['face']
    # print(faces[0])  # Affiche les informations du premier visage pour le débogage
    resize_img_array = cv2.resize(img_array, (224, 224))  # Redimensionne à (224, 224)
    all_faces.append(resize_img_array)
    img_array = []
    resize_img_array = []

  return all_faces


def show_and_save_detected_faces(faces):
    """
        Affiche chaque visage détecté et l'enregistre dans un fichier.

        :param faces: list
        Liste de tableaux numpy représentant des visages détectés.
    """
    # Création du dossier "detected_face" s'il n'existe pas
    save_dir = 'detected_faces'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i, face in enumerate(faces):
        plt.imshow(face)
        plt.axis('off')

        # Sauvegarde du visage dans un fichier avant de l'afficher
        plt.savefig(f'{save_dir}/face_{i+1}.jpg')
        # plt.close()  # Ferme la figure pour libérer la mémoire
        # Affiche l'image après l'avoir sauvegardée
        plt.imshow(face)
        plt.show()


detected_faces = extract_faces('helicia.jpg')
show_and_save_detected_faces(detected_faces)

print(len(detected_faces))

