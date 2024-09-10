from deepface import DeepFace

result = DeepFace.verify("gning.jpg","gning1.jpg")
print(result)

info = DeepFace.analyze(img_path='gning1.jpg', actions=['gender'],)
print(info)
# face_objs = DeepFace.extract_faces(
#   img_path="my_team.png",
#   anti_spoofing = True
# )
# assert all(face_obj["is_real"] is True for face_obj in face_objs)
