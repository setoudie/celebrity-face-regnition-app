from django.test import TestCase
from ml_model import *
# Create your tests here.

detected_faces = extract_faces('odc.jpg')
show_and_save_detected_faces(detected_faces)
