import librosa 
import librosa.display 
import matplotlib.pyplot as plt
import numpy as np

# Cargamos el archivo de audio
audio_file_path = librosa.example('trumpet')  # 'trumpet' es un ejemplo, cámbialo al nombre de tu archivo de audio

y, sr= librosa.load(audio_file_path)

#Calcular el espectograma mel 
mel_spec= librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)

#Convertir a decibeles (escala logaritmica)
mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

#Mostrar el espectrograma mel
plt.figure(figsize=(10,4))
librosa.display.specshow(mel_spec_db, x_axis='time', y_axis='mel', sr=sr, fmax=8000)
plt.colorbar(format='%+2.0f dB')
plt.title('Mel Spectrogram')
plt.show()

#Calcular los coeficientes cepstrales de frecuencia (MFCC)
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

#Mostrar los MFCC
plt.figure(figsize=(10,4))
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.show()
