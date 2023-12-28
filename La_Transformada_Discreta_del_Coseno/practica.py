import librosa
import numpy as np 
import matplotlib.pyplot as plt
import scipy
#Funcion para extraer caracteristicas de MFCC utilizando la DCT 
def extract_mfcc_features(file_path):
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast') 
    
    #Extraer coeficientes MFCC utilizando librosa
    mfccs = librosa.feature.mfcc(audio, sr=sample_rate, n_mfcc=40)
    
    #Aplicar la DCT a los coeficientes MFCC 
    mfccs = scipy.fftpack.dct(mfccs, axis=0, type=2, norm='ortho')
    
    return mfccs
#Ruta del archivo de audio
audio_file = "person.wav"

#Extraer caracteristicas de MFCC utilizando DCT 
mfcc_features = extract_mfcc_features(audio_file)
#Visualizar los coeficientes MFCC despues de aplicar DCT
plt.imshow(mfcc_features, cmap='viridis', origin='lower', aspect='auto')
plt.xlabel('Tiempo')
plt.ylabel('Coeficientes MFCC')
plt.title('Coeficientes MFCC despues de DCT')
plt.colorbar()
plt.show()