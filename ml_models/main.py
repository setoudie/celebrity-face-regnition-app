import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import face_recognition

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

# plot_image(img_path)
# show_image_with_cv2(img_path)

img = cv2.imread(img_path)
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
encoded_img = face_recognition.face_encodings(rgb_img)[0]