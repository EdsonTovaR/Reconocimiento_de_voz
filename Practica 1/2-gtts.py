from gtts import gTTS

tts=gTTS('Hola mundo.Estamnos convirtiendo textoa voz con Python.', lang='es-us')

with open("2_hola_mundo.mp3", "wb") as archivo:
    tts.write_to_fp(archivo)