import os
import speech_recognition as sr
import pyfiglet
from funciones import *
from tabulate import tabulate


def inicio():
    os.system("cls")

    try:
        while True:
            titulo = 'Registro de Voces'
            a = pyfiglet.figlet_format(titulo)
            print(a)
            print("**************************")
            print(':: Selecione una opción ::')
            print('**************************')
            print()
            print("\t1. Ingresar una nueva voz")
            print("\t2. Mostrar todas las voces registradas")
            print("\t3. Buscar los registros de una voz")
            print("\t4. Modificar los datos de una voz")
            print("\t5. Eliminar un registro de voz")
            print("\t6. Salir de la aplicación")
            print()
            opcion = input("Escoja una opción: ")

            os.system("cls")

            if opcion == "1":
                nueva_voz()
            elif opcion == "2":
                mostrar_voz()
            elif opcion == "3":
                buscar_voz()
            elif opcion == "4":
                modificar_voz()
            elif opcion == "5":
                eliminar_voz()
            elif opcion == "6":
                break
            else:
                print("--------------------------")
                print("Escoja una opción correcta")
                print("---------------------------")
    except AttributeError as err:
        print("***********************************")
        print(':: Error de conección ¯\_(ツ)_/¯ ::')
        print("***********************************")
        print()
        input("presione enter para continuar...")
        inicio()

def nueva_voz():
    nombre=input("Ingresa tu nombre: ")
    genero=input("Ingresa tu genero: ")
    voz=reconocimiento()
    os.system('cls')
    registro=registrar(nombre,genero,voz)
    print(len(registro)* '-')
    print(registro)
    print(len(registro)* '-')
    input("Presione enter para continuar")
    os.system('cls')





def mostrar_voz():
    datos=mostrar()
    header=['NOMBRE','GENERO','VOZ']
    tabla=tabulate(datos,header,tablefmt='facncy_grid')
    print(tabla)
    input("Presione enter para seguir...")
    os.system('cls')
    

def buscar_voz():
    id = input("Ingrese el nombre del usuario que quiere buscar: ")
    os.system('cls')
    datos = buscar(id)

    if  not datos:
        print("---------------------------------")
        print('*** El registro del usuario no existe ***')
        print("---------------------------------")
        input("Presione enter para continuar...")
        os.system('cls')
    else:
        header = ['NOMBRE', 'GENERO', 'VOZ']
        tabla = tabulate(datos, header, tablefmt='fancy_grid')
        print(tabla)
        input("Presione enter para continuar...")
        os.system('cls')

        
    
def modificar_voz():
    id=input("Ingrese el nombre del alumno a modificar: ")
    dato=buscar(id)

    if not dato:
        print("-------------------------------")
        print(':: El id del alumno no existe ::')
        print('-------------------------------')
        input("Presione enter para continuar...")
        os.system('cls')
    else:
        campo=0
        nuevo_valor=''
        while campo not in ['1','2','3']:
            header=['NOMBRE','GENERO','VOZ']
            tabla=tabulate(dato,header,tablefmt='fancy_grid')
            print(tabla)

            print("----------------------------------------")
            campo=input('Seleccione el campo que desea modificar ')


    

def eliminar_voz():
    return

if __name__=='__main__':
    inicio()

