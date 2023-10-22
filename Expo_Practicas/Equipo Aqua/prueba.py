import os
import speech_recognition as sr
""" r=sr.Recognizer()

with sr.Microphone() as source:

    print('Menciona tu numero de DNI....')

    nuevo= r.listen(source)

    print('realizado')



    try:

        voice=r.recognize_google(nuevo, language='es')

        print(voice)

    except Exception as e:

        print(e)

with open('nuevo.wav', "wb") as f:
      f.write(nuevo.get_wav_data())
 """
 
from cargar import extract_features, extract_features_from_file
from sklearn import preprocessing
import tensorflow as tf
from model import get_model, save_model
model = get_model()

features,label=extract_features_from_file('audios\\defaults\\common_voice_es_38029820.mp3')
# features = preprocessing.normalize(features.reshape(1,-1), norm='l2')
features = features.reshape(1,40)
predict = model.predict([features])
print(predict)

features,label=extract_features_from_file('audios\\omar.wav')
# features = preprocessing.normalize(features.reshape(1,-1), norm='l2')
features = features.reshape(1,40)
predict = model.predict([features])
print(predict)

features,label=extract_features_from_file('nuevo.wav')
# features = preprocessing.normalize(features.reshape(1,-1), norm='l2')
features = features.reshape(1,40)

predict = model.predict([features])
print(predict)

