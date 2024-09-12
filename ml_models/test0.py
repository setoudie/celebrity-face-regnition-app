

results = {
           'kate_beckinsale': {'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
           'lauren_cohan': {'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
           'dwayne_johnson': {'face_1': [False, True, True, False, False, True, False, False, False, False, True, True, False, False, True, True, False, True, False, False]},
           'madonna': {'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
           'sofia_vergara': {'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
           'ben_afflek': {'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
           'anne_hathaway': {'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
           'arnold_schwarzenegger': {'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
           'mindy_kaling': {'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
           'elton_john': {'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
           'jerry_seinfeld': {'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
           'will_smith': {'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
           'keanu_reeves': {'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]},
           'simon_pegg': {'face_1': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]}
           }

taux = (results['dwayne_johnson']['face_1'].count(True)/len(results['dwayne_johnson']['face_1']))*100
print(taux)