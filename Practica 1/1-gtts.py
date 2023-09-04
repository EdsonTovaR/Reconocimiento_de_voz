"""CONVERTIR EL TEXTO A VOZ CON PYTHON USANDO gTTS"""

from gtts import gTTS

tts=gTTS('Hola mundo.Estamnos convirtiendo textoa voz con Python.', lang='es-us')
tts.save('1_hola_mundo.mp3')