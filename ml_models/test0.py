from model import *

results = {
  'kate_beckinsale': {
    'face_2': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_6': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_3': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_7': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_5': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_4': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
  },
  'lauren_cohan': {
    'face_2': [False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_6': [False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_3': [False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_7': [False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_5': [True, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_4': [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
  },
  'dwayne_johnson': {
    'face_2': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_6': [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_1': [True, True, True, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False],
    'face_3': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_7': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_5': [True, False, True, False, False, True, False, False, False, False, True, True, False, False, False, True, False, True, False, True],
    'face_4': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
  },
  'madonna': {
    'face_2': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_6': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_3': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_7': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_5': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_4': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
  },
  'sofia_vergara': {
    'face_2': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_6': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_3': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 'face_7': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_5': [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_4': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
  },
  'ben_afflek': {
    'face_2': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_6': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_3': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_7': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_5': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_4': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
  },
  'anne_hathaway': {
    'face_2': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_6': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_3': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_7': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_5': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_4': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
  },
  'arnold_schwarzenegger': {
    'face_2': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_6': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_3': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_7': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_5': [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False],
    'face_4': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
  },
  'mindy_kaling': {
    'face_2': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_6': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_3': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_7': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_5': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_4': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
  },
  'elton_john': {
    'face_2': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_6': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_3': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_7': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_5': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_4': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
  'jerry_seinfeld': {
    'face_2': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_6': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_3': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_7': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_5': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_4': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
  },
  'will_smith': {
    'face_2': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_6': [True, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False],
    'face_1': [False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, True, False, False, False, False, True],
    'face_3': [True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False],
    'face_7': [True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_5': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_4': [False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False]
  },
  'keanu_reeves': {
    'face_2': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_6': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_3': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_7': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_5': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_4': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             },
  'simon_pegg': {
    'face_2': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_6': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_3': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_7': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_5': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    'face_4': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
  }
}


scor_result = {
  'kate_beckinsale': {
    'face_2': 0.0,
    'face_6': 0.0,
    'face_1': 0.0,
    'face_3': 0.0,
    'face_7': 0.0,
    'face_5': 0.0,
    'face_4': 0.0
  },
  'lauren_cohan': {
    'face_2': 0.0,
    'face_6': 0.0,
    'face_1': 0.0,
    'face_3': 0.0,
    'face_7': 0.0,
    'face_5': 7.14,
    'face_4': 0.0
  },
  'dwayne_johnson': {
    'face_2': 0.0,
    'face_6': 5.0,
    'face_1': 30.0,
    'face_3': 0.0,
    'face_7': 0.0,
    'face_5': 40.0,
    'face_4': 0.0
  },
  'madonna': {

    'face_2': 0.0,
    'face_6': 0.0,
    'face_1': 0.0,
    'face_3': 0.0,
    'face_7': 0.0,
    'face_5': 0.0,
    'face_4': 0.0
  },
  'sofia_vergara': {
    'face_2': 0.0,
    'face_6': 0.0,
    'face_1': 0.0,
    'face_3': 0.0,
    'face_7': 0.0,
    'face_5': 4.35,
    'face_4': 0.0
  },
  'ben_afflek': {
    'face_2': 0.0,
    'face_6': 0.0,
    'face_1': 0.0,
    'face_3': 0.0,
    'face_7': 0.0,
    'face_5': 0.0,
    'face_4': 0.0
  },
  'anne_hathaway': {
    'face_2': 0.0,
    'face_6': 0.0,
    'face_1': 0.0,
    'face_3': 0.0,
    'face_7': 0.0,
    'face_5': 0.0,
    'face_4': 0.0
  },
  'arnold_schwarzenegger': {
    'face_2': 0.0,
    'face_6': 0.0,
    'face_1': 0.0,
    'face_3': 0.0,
    'face_7': 0.0,
    'face_5': 8.7,
    'face_4': 0.0
  },
  'mindy_kaling': {
    'face_2': 0.0,
    'face_6': 0.0,
    'face_1': 0.0,
    'face_3': 0.0,
    'face_7': 0.0,
    'face_5': 0.0,
    'face_4': 0.0
  },
  'elton_john': {
    'face_2': 0.0,
    'face_6': 0.0,
    'face_1': 0.0,
    'face_3': 0.0,
    'face_7': 0.0,
    'face_5': 0.0,
    'face_4': 0.0
  },
  'jerry_seinfeld': {
    'face_2': 0.0,
    'face_6': 0.0,
    'face_1': 0.0,
    'face_3': 0.0,
    'face_7': 0.0,
    'face_5': 0.0,
    'face_4': 0.0
  },
  'will_smith': {
    'face_2': 0.0,
    'face_6': 19.05,
    'face_1': 19.05,
    'face_3': 14.29,
    'face_7': 9.52,
    'face_5': 0.0,
    'face_4': 4.76
  },
  'keanu_reeves': {
    'face_2': 0.0,
    'face_6': 0.0,
    'face_1': 0.0,
    'face_3': 0.0,
    'face_7': 0.0,
    'face_5': 0.0,
    'face_4': 0.0
  },
  'simon_pegg': {
    'face_2': 0.0,
    'face_6': 0.0,
    'face_1': 0.0,
    'face_3': 0.0,
    'face_7': 0.0,
    'face_5': 0.0,
    'face_4': 0.0
  }
}


# fonction pour associer un nom à la face detecter
def find_celebrity(my_results_dico):
  pass


# detected_faces = extract_faces('helicia.jpg')
# show_and_save_detected_faces(detected_faces)
# results_ = predict_celebrity()


df = score_df(results)
print(df)

print(df['face_1'].max)
