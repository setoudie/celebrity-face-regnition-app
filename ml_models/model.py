# Importation des bibliothèques nécessaires
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

# Liste des backends de détection disponibles
backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'fastmtcnn', 'retinaface', 'mediapipe', 'yolov8', 'yunet', 'centerface']

# Options d'alignement des visages
alignement_modes = [True, False]


def extract_faces(img_path):
    """
    Détecte et extrait les visages d'une image donnée.

    :param img_path: Chemin de l'image à analyser
    :return: Liste des visages détectés et redimensionnés
    """
    # Utilisation de DeepFace pour extraire les visages
    faces = DeepFace.extract_faces(img_path, detector_backend=backends[4], enforce_detection=False)

    all_faces = []
    for i in tqdm(range(len(faces)), desc="Extraction des faces"):
        img_array = faces[i]['face']
        # Redimensionnement de chaque visage à 224x224 pixels
        resize_img_array = cv2.resize(img_array, (224, 224))
        all_faces.append(resize_img_array)

    return all_faces


def show_and_save_detected_faces(faces):
    """
    Affiche et sauvegarde les visages détectés.

    :param faces: Liste des visages détectés
    """
    # Création ou nettoyage du dossier de sauvegarde
    save_dir = 'detected_faces/'
    if os.path.exists(save_dir):
        shutil.rmtree(save_dir)
    os.makedirs(save_dir)

    # Sauvegarde de chaque visage
    for i, face in tqdm(enumerate(faces), desc='Show and Save faces'):
        plt.imshow(face)
        plt.axis('off')
        plt.savefig(f'{save_dir}/face_{i + 1}.jpg')


def predict_celebrity():
    """
    Prédit l'identité des célébrités pour les visages détectés.

    :return: Dictionnaire des résultats de prédiction
    """
    save_dir = 'detected_faces'
    images_dir = 'images'
    result = dict()

    if os.path.exists(save_dir) and os.path.exists(images_dir):
        all_detected_faces = os.listdir(save_dir)
        celebrity_dir = os.listdir(images_dir)

        for celebrity_name in celebrity_dir:
            result[celebrity_name] = dict()
            celebrity_name_images = os.listdir(images_dir + "/" + celebrity_name)

            print(f"\nCelebrity Name : {celebrity_name}", end='\n\n')
            for face in all_detected_faces:
                result[celebrity_name][face.split('.')[0]] = list()

                for i in tqdm(range(len(celebrity_name_images)), desc=f'Verify {celebrity_name} images : {face}'):
                    face_path = save_dir + "/" + face
                    celeb_img_path = images_dir + "/" + celebrity_name + "/" + celebrity_name_images[i]

                    # Redimensionnement et sauvegarde temporaire de l'image de célébrité
                    img = cv2.imread(celeb_img_path)
                    resized_celeb_img = cv2.resize(img, (224, 224))
                    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
                        temp_file_name = temp_file.name
                        cv2.imwrite(temp_file_name, resized_celeb_img)

                    # Vérification de la correspondance des visages
                    face_match = DeepFace.verify(
                        img1_path=face_path,
                        img2_path=temp_file_name,
                        detector_backend=backends[0],
                        align=alignement_modes[0],
                        enforce_detection=False,
                    )
                    result[celebrity_name][face.split('.')[0]].append(face_match['verified'])

    return result


def calculate_score(my_face_bool_list):
    """
    Calcule le score de correspondance pour un visage.

    :param my_face_bool_list: Liste de booléens indiquant les correspondances
    :return: Score en pourcentage
    """
    true_val = my_face_bool_list.count(True)
    total_val = len(my_face_bool_list)
    score = 100 * true_val / total_val
    return round(score, 2)


def get_celeb_faces_score(my_celeb_result_dict):
    """
    Calcule les scores pour tous les visages d'une célébrité.

    :param my_celeb_result_dict: Dictionnaire des résultats pour une célébrité
    :return: Dictionnaire des scores par visage
    """
    celeb_faces_scores = dict()
    for face in my_celeb_result_dict:
        celeb_faces_scores[face] = calculate_score(my_celeb_result_dict[face])
    return celeb_faces_scores


def get_all_celebs_faces_scores(rslt):
    """
    Calcule les scores pour toutes les célébrités.

    :param rslt: Dictionnaire des résultats pour toutes les célébrités
    :return: Dictionnaire des scores pour toutes les célébrités
    """
    all_celebs_scores = dict()
    for celeb in rslt:
        all_celebs_scores[celeb] = get_celeb_faces_score(rslt[celeb])
    return all_celebs_scores


def score_df(raw_data):
    """
    Crée un DataFrame pandas avec les scores et le sauvegarde en CSV.

    :param raw_data: Données brutes des résultats
    :return: DataFrame des scores
    """
    faces_scores = get_all_celebs_faces_scores(raw_data)
    df_faces_scores = pd.DataFrame.from_dict(faces_scores, orient='index')

    save_dir = 'data/'
    if os.path.exists(save_dir):
        shutil.rmtree(save_dir)
    os.makedirs(save_dir)
    df_faces_scores.to_csv(f'{save_dir}/faces_scores.csv')

    return df_faces_scores


def find_face_owner(scores_df):
    """
    Détermine le propriétaire probable de chaque visage basé sur les scores.

    :param scores_df: DataFrame des scores
    :return: Dictionnaire des propriétaires probables pour chaque visage
    """
    max_scores_faces = dict()

    for col in scores_df.columns:
        max_scores_faces[col] = dict()
        max_value = scores_df[col].max()
        max_index = scores_df[col].idxmax()

        if max_value >= 40.5:
            max_scores_faces[col]['face_name'] = max_index
        else:
            max_scores_faces[col]['face_name'] = 'Unknown'

        max_scores_faces[col]['face_score'] = max_value

    return max_scores_faces