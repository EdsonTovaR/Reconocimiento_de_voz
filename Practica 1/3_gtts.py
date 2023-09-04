from gtts import gTTS
tts = gTTS('Hola mundo. Estamos convirtiendo texto a voz con Python.', lang='es-us')
tts_ingles = gTTS('Hello world! testing tts in Python', lang='en')
tts_frances = gTTS('Bonsoir, Elliot', lang='fr-fr')

with open("3_hola_es_en_fr.mp3", "wb") as archivo:
    tts.write_to_fp(archivo)
    tts_ingles.write_to_fp(archivo)
    tts_frances.write_to_fp(archivo)