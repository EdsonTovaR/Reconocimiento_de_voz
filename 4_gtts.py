from gtts import gTTS
from playsound import playsound

NOMBRE_ARCHIVO ="sonido_generado.mp3"

tss = gTTS('Hola mundo. Estamos convirtiendo texto a voz con python.',lang='es-us')

#Nota:Podriamos llamadar directamente a save

with open(NOMBRE_ARCHIVO,"wb") as archivo:
    tss.write_to_fp(archivo)

#Reproducimos el archivo
playsound(NOMBRE_ARCHIVO)