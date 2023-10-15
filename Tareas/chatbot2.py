import tkinter as tk
import pyttsx3 as voz
from time import sleep
import subprocess as sub
import pyautogui as auto
import speech_recognition as sr

def interpretar(comando_de_audio):
    comando_de_audio = comando_de_audio.split(' ')

    navegador = ('navegador' or 'chrome') in comando_de_audio
    escribir = ('escribir' or 'texto') in comando_de_audio
    abrir_calc = ('calculadora' or 'calcula' or 'calcular') in comando_de_audio
    musica= ('musica'or'cancion') in comando_de_audio
    clima=('clima' or 'temperatura') in comando_de_audio
    hora=('hora' or 'horas') in comando_de_audio
    fecha=('fecha' or 'día') in comando_de_audio
    


    if navegador:
        abrir_navegador()
    elif escribir:
        abrir_blockNotas()
    elif abrir_calc:
        abrir_calculadora()

def abrir_blockNotas():
    sub.call('start notepad.exe', shell=True)
    sleep(1.5)
    asistente = voz.init()
    velocidad = asistente.getProperty('rate')
    asistente.setProperty('rate', velocidad - 50)
    asistente.setProperty('voice', 'TTS_MS_ES-MX_SABINA_11.0')
    asistente.say("Abriendo el block de notas")
    asistente.runAndWait()

def abrir_navegador():
    sub.call('start Chrome.exe', shell=True)
    sleep(1.5)
    asistente = voz.init()
    velocidad = asistente.getProperty('rate')
    asistente.setProperty('rate', velocidad - 50)
    asistente.setProperty('voice', 'TTS_MS_ES-MX_SABINA_11.0')
    asistente.say("Abriendo el navegador")
    asistente.runAndWait()

def abrir_calculadora():
    sub.call('calc.exe', shell=True)

def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di algo")
        audio = r.listen(source)
        print("Ya escuche")
        try:
            texto = r.recognize_google(audio, language='es-MX')
            print("Tu dijiste: {}".format(texto))
            interpretar(texto)
        except:
            print("No te escuche")
            pass

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Chatbot")
root.geometry("800x400")
root.configure(bg='#42A5F5')


# Cargar una imagen de fondo
bg_image = tk.PhotoImage(file="Tareas\iondo.png")  
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)
bg_label.place(x=200, y=0)


# Botón para activar el chatbot
boton = tk.Button(root, text="Escuchar", command=escuchar, bg='#009688', fg='white')
boton.place(x=20, y=50)

# Función para cerrar la ventana
def cerrar_ventana():
    root.destroy()

# Botón para cerrar la ventana
boton_cerrar = tk.Button(root, text="Cerrar", command=cerrar_ventana, bg='#D81B60', fg='white')
boton_cerrar.place(x=20, y=20)


# Iniciar el bucle de la interfaz gráfica
root.mainloop()
