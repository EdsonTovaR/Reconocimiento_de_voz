import librosa
import librosa.display
import matplotlib.pyplot as plt

# Cargar un archivo de audio WAV
audio_file = "audio.wav"

# Cargar la señal de audio y su tasa de muestreo
y, sr = librosa.load(audio_file)

# Extraer los coeficientes MFCC
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

# Visualizar los coeficientes MFCC
plt.figure(figsize=(10, 4))
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.tight_layout()
plt.show()
