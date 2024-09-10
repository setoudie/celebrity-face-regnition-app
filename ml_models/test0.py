from deepface import DeepFace
from PIL import Image

path='gning1.jpg'
img = Image.open(path)
img = img.convert("L")
img.save('gray_heli.jpg')
img.show()

objs = DeepFace.analyze(
  img_path = "gray_heli.jpg",
  actions = ['age'],
)

print(objs)