

from os import path
from os import listdir, remove

import librosa

import numpy as np
from sklearn.preprocessing import LabelEncoder
from keras.utils.np_utils import to_categorical
from sklearn import preprocessing
from sqlalchemy import true


def extract_features(y,sr):
    y = y.astype(np.float32) / 32767.0
    mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T,axis=0)
    stft = np.abs(librosa.stft(y))
    chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sr).T,axis=0)
    mel = np.mean(librosa.feature.melspectrogram(y=y,sr=sr).T,axis=0)
    contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sr).T,axis=0)
    tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(y), sr=sr).T,axis=0)
    features =np.concatenate((mfccs,chroma,mel, contrast, tonnetz))
    features = preprocessing.normalize(features.reshape(1,-1), norm='l2')
    return features[0]

def extract_mffc(y,sr):
    y = y.astype(np.float32) / 32767.0
    mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T,axis=0)
    features = preprocessing.normalize(mfccs.reshape(1,-1), norm='l2')
    return features[0]

def extract_features_from_file(file_name):
    y, sr = librosa.load(file_name,sr=22050,duration=5)
    features = extract_mffc(y, sr)
    return features, file_name.split('.')[0]

def get_autdios_features():
    PATH  = 'audios'
    if not path.exists(PATH):
        return
    
    x = []
    y_labels = []
    index = 0
    for file in listdir(PATH):
        if file.endswith('.wav'):
            features, label = extract_features_from_file(path.join(PATH, file))
            x.append(features)
            y_labels.append(index)
            index+=1

    x = np.array(x)
    encoder = LabelEncoder()
    y = to_categorical(y_labels)
    print(x.shape)
    print(y.shape)
    print(y)
    return x, y

def isRegist():
    PATH  = 'audios'
    if not path.exists(PATH):
        return False
    
    for file in listdir(PATH):
        if file.endswith('.wav'):
            remove(path.join(PATH, file))
        
    return True

if __name__ == "__main__":
    y,sr=librosa.load('audios\\omar.wav',sr=22050,duration=5)
    mffcs = extract_mffc(y, sr)
    print(mffcs.shape)