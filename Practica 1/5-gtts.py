from gtts import gTTS

tts = gTTS('Hola mundo. Estamos convirtiendo texto a voz con Python.', lang='es-us', slow=True )

tts.save("5_hola_mundo.mp3")
