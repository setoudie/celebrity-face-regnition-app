from deepface import DeepFace
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
import os
import shutil
import tempfile
from tqdm import tqdm
import pandas as pd


backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'fastmtcnn', 'retinaface', 'mediapipe', 'yolov8', 'yunet', 'centerface',]

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

  faces = DeepFace.extract_faces(img_path, detector_backend=backends[4], enforce_detection=False)

  all_faces = []
  for i in tqdm(range(len(faces)), desc="Extraction des faces"):
    img_array = faces[i]['face']
    # print(faces[0])  # Affiche les informations du premier visage pour le débogage
    resize_img_array = cv2.resize(img_array, (224, 224))  # Redimensionne à (224, 224)
    all_faces.append(resize_img_array)
    img_array = []
    resize_img_array = []

  return all_faces

# Fonction pour afficher et sauvegarder les faces detectes
def show_and_save_detected_faces(faces):
    """
        Affiche chaque visage détecté et l'enregistre dans un fichier.

        :param faces: list
        Liste de tableaux numpy représentant des visages détectés.
    """
    # Création du dossier "detected_face" s'il n'existe pas
    save_dir = 'detected_faces/'
    if os.path.exists(save_dir):
        shutil.rmtree(save_dir) # Supression du dossier `detected_faces/` existant
    os.makedirs(save_dir) # Creation du dossier `detected_faces/`

    for i, face in tqdm(enumerate(faces), desc='Show and Save faces'):
        plt.imshow(face)
        plt.axis('off')

        # Sauvegarde du visage dans un fichier avant de l'afficher
        plt.savefig(f'{save_dir}/face_{i+1}.jpg')
        # plt.close()  # Ferme la figure pour libérer la mémoire
        # plt.show()


# Fonction pour predir une celebrite
def predict_celebrity():
    save_dir = 'detected_faces'
    images_dir = 'images'
    if os.path.exists(save_dir) and os.path.exists(images_dir):
        # pass
        all_detected_faces = os.listdir(save_dir)
        celebrity_dir = os.listdir(images_dir)

        # dictionnaire contenant les resultats : `result['celeb_name']['face'] = list of boolean`
        result = dict()

        for celeb_i, celebrity_name in enumerate(celebrity_dir):
            # print(celeb_i, celebrity_name)
            result[celebrity_name] = dict()
            celebrity_name_images = os.listdir(images_dir + "/" + celebrity_name)
            # print(celebrity_name_images)

            print(f"\nCelebrity Name : {celebrity_name}", end='\n\n')
            for face in all_detected_faces:
                result[celebrity_name][face.split('.')[0]] = list()

                for i in tqdm(range(len(celebrity_name_images)),desc=f'Verify {celebrity_name} images : {face}'):
                    face_path = save_dir + "/" + face
                    celeb_img_path = images_dir + "/" + celebrity_name + "/" + celebrity_name_images[i]

                    img = cv2.imread(celeb_img_path)
                    resized_celeb_img = cv2.resize(img, (224,224))

                    # Enregistrer l'image redimensionnée dans un fichier temporaire
                    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
                        temp_file_name = temp_file.name
                        cv2.imwrite(temp_file_name, resized_celeb_img)

                    # print(face_path, celeb_img_path)
                    face_match = DeepFace.verify(
                        img1_path=face_path,
                        img2_path=temp_file_name,
                        detector_backend=backends[0],
                        align=alignement_modes[0],
                        enforce_detection=False,
                    )
                    # print(face, celebrity_name_images[i], face_match['verified'])
                    result[celebrity_name][face.split('.')[0]].append(face_match['verified'])
            print()
                # break

        # print(result)
        return result


# ----------------------------
def calculate_score(my_face_bool_list):
    # pass
    true_val = my_face_bool_list.count(True)
    # false_val = my_face_bool_list.count(False)
    total_val = len(my_face_bool_list)
    score = 100 * true_val / total_val
    return round(score, 2)


# -------------------------------
def get_celeb_faces_score(my_celeb_result_dict):
    celeb_faces_scores = dict()
    for face in my_celeb_result_dict:
        celeb_faces_scores[face] = calculate_score(my_celeb_result_dict[face])
    # print(celeb_faces_scores)
    return celeb_faces_scores


def get_all_celebs_faces_scores(rslt):
    all_celebs_scores = dict()
    for celeb in rslt:
        all_celebs_scores[celeb] = get_celeb_faces_score(rslt[celeb])
    # print(all_celebs_scores)

    return all_celebs_scores


def score_df(raw_data):
    faces_scores = get_all_celebs_faces_scores(raw_data)
    df_faces_scores = pd.DataFrame.from_dict(faces_scores, orient='index')

    save_dir = 'data/'
    if os.path.exists(save_dir):
        shutil.rmtree(save_dir)

    os.makedirs(save_dir)
    df_faces_scores.to_csv(f'{save_dir}/faces_scores.csv')

    return df_faces_scores
