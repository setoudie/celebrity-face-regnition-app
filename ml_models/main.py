import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img_path = 'images/train/arnold_schwarzenegger/400px-Arnold_Schwarzenegger_(9048849809).jpg'

# Fonction pour visualiser une image
def show_image(path):
    """
        :param path:
        :return: None

        Cette fonction lis et affiche une image a travers son path
    """
    img = mpimg.imread(path)
    plt.imshow(img)
    plt.show()

show_image(img_path)