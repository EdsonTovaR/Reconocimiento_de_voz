import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
# Carga un archivo de audio (asegúrate de tener uno disponible en la misma ubicación)
audio_file = 'Expo_Practicas/EquipoQuesea/Mi audio.mp3'

# Carga la señal de audio y muestrea a 22050 Hz
y, sr = librosa.load(audio_file, sr=22050)

# Extrae características acústicas, como el espectrograma y el chromagram
spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
chromagram = librosa.feature.chroma_stft(y=y, sr=sr)

# Visualiza el espectrograma y el chromagram
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
librosa.display.specshow(librosa.power_to_db(spectrogram, ref=np.max), y_axis='mel', x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel Spectrogram')

plt.subplot(2, 1, 2)
librosa.display.specshow(chromagram, y_axis='chroma', x_axis='time')
plt.colorbar()
plt.title('Chromagram')
plt.tight_layout()

plt.show()