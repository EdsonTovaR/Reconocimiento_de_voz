import pyaudio as pyaudio
import speech_recognition as sr
import IPython.display as ipd
import io
import os
import pandas as pd
import librosa

import glob
import matplotlib as mpl
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import random
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import Adam
from keras.utils import np_utils
from sklearn import metrics
from sklearn.datasets import make_regression

from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.model_selection import train_test_split, GridSearchCV
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
from keras.callbacks import EarlyStopping
from keras import regularizers
from sklearn.preprocessing import LabelEncoder

from datetime import datetime

from pydub import AudioSegment

np.set_printoptions(suppress=True)

r=sr.Recognizer()

with sr.Microphone() as source:
    print('Menciona tu numero de DNI...')

    audio60= r.listen(source)
    print('realizado')

try:
    voice = r.recognize_google(audio, language='es')
    print(voice)

except Exception as e:
    print(e)

    ##--Guardamos el audio en un carpeta.
    with open('', "wb") as f:

        f.write(audio60.get_wav_data())

##--Cargamos y probamos el archivo de audio

audio=r'D:/KONECTA/APLICACIONES/VOICE_RECOGNITION/audio_captura/audio60.wav'
ipd.Audio(audio, rate=22050)