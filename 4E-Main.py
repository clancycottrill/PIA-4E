from datetime import datetime
import subprocess 
import sys
import argparse
import os
import hashlib
import pspy  #modulos locales
import pypy  #
import shpy  #  


parser = argparse.ArgumentParser(prog='Script4E', description='Script principal del último entregable de Programación para Ciberseguridad.') #paso de parámetros con argparse OPCIONALES.
parser.add_argument("-mod", dest="modulo", type=int, help="Lenguaje de módulos a ejecutar. Puede ser 1 para POWERSHELL, 2 para BASH o 3 para PYTHON.")
parser.add_argument('-ct', dest="cibertarea",type=int, help="Cibertarea a realizar. Puede ser 1-4 para POWERSHELL, 1-2 para BASH y 1-5 para PYHON." )
args = parser.parse_args() 

report_loc = os.getcwd() #ruta donde estan los reportes, la cual es la misma que el script
raw_date = datetime.now()
today = raw_date.strftime ('%c') #en este caso, %c cambia el formato a dia, mes, fecha, hora y año

#Menu principal para windows
def menu_main_windows():
    val = True
    while val:
        if args.modulo:
            option = int(args.modulo)
        else:
            print("¿A qué módulos quiere acceder?")
            print("-----------------------------------------")
            print("1. Módulos de Powershell")
            print("2. Módulos de Bash")
            print("3. Módulos de Python")
            print("4. Salir")
            print("-----------------------------------------")
            option = input("Ingrese una opción: ")
            while not (option.isdigit() and 1 <= int(option) <= 4):
                print ("Ingrese un número válido del 1 al 4.")
                option = input("Ingrese una opción: ")
        option = int(option)

        if option == 1:
            print("Entrando al menú de Powershell...")
            menu_ps()
        elif option == 2:
            print("No se pueden ejecutar scripts de Bash en este SO. Regresando al menu...")
        elif option == 3:
            print("Entrando al menú de Python...")
            menu_py()
        else:
            print("Saliendo del programa...")
            val = False 

        if args.modulo:
            val = False #para salir del bucle infinito que ocurre cuando se pasan argumentos desde la terminal

#Menu principal para mac
def menu_main_mac():
    val = True
    while val:
        if args.modulo:
            option = int(args.modulo)
        else:
            print("¿A qué módulos quiere acceder?")
            print("-----------------------------------------")
            print("1. Módulos de Powershell")
            print("2. Módulos de Bash")
            print("3. Módulos de Python")
            print("4. Salir")
            print("-----------------------------------------")
            option = input("Ingrese una opción: ")
            while not (option.isdigit() and 1 <= int(option) <= 4):
                print ("Ingrese un número válido del 1 al 4.")
                option = input("Ingrese una opción: ")

        if option == 1:
            print("Entrando al menú de Powershell...")
            menu_ps()
        elif option == 2:
            print("No se pueden ejecutar scripts de Bash en este SO. Regresando al menu...")
        elif option == 3:
            print("Entrando al menú de Python...")
            menu_py()
        else:
            print("Saliendo del programa...")
            val = False 

        if args.modulo:
            val = False

#menu principal para SO LINUX
def menu_main_linux():
    val = True
    while val:
        if args.modulo:
            option = int(args.modulo)
        else:
            print("¿A qué módulos quiere acceder?")
            print("-----------------------------------------")
            print("1. Módulos de Powershell")
            print("2. Módulos de Bash")
            print("3. Módulos de Python")
            print("4. Salir")
            print("-----------------------------------------")
            option = input("Ingrese una opción: ")
            while not (option.isdigit() and 1 <= int(option) <= 4):
                print ("Ingrese un número válido del 1 al 4.")
                option = input("Ingrese una opción: ")

        if option == 1:
            print("Entrando al menú de Powershell...")
            menu_ps()
        elif option == 2:
            print("Entrando al menú de Bash...")
            shpy.menu_bash()
        elif option == 3:
            print("Entrando al menú de Python...")
            menu_py()
        else:
            print("Saliendo del programa...")
            val = False

        if args.modulo:
            val = False

#Menu de powershell
def menu_ps():
    val = True
    while val:
        if args.cibertarea:
            option = int(args.cibertarea)
        else:
            print("¿Qué módulo de Powershell quiere usar?")
            print("-----------------------------------------")
            print("1. LoginLogs")
            print("2. Resources")
            print("3. RevealHiddenFiles")
            print("4. VirusTotalHashCheck")
            print("5. Salir al menú principal")
            print("-----------------------------------------")
            option = input("Ingrese la opción: ")

            while not (option.isdigit() and 1 <= int(option) <= 5):
                print ("Ingrese un número válido del 1 al 5.")
                option = input("Ingrese una opción: ")

        option = int(option)
        if option == 1:
            print("Ejecutando 'LoginLogs'...")
            pspy.loginlogs()
            report_name = "loginlogs_report.txt"
            report_loc_loginlogs = os.path.join (report_loc, report_name)
            hash_value = hash_calc(report_loc_loginlogs)
            print ("La tarea 'LoginLogs' fue ejecutada en la fecha:", today, '\n')
            print ("El hash del reporte", report_name, 'es:\n', hash_value, "\n Y se encuentra en la siguiente ubicación:\n")
            print (report_loc_loginlogs)            

        elif option == 2:
            print("Ejecutando 'Resources'...")
            pspy.resources()
            report_name = "resources_report.txt"
            report_loc_resources = os.path.join (report_loc, report_name)
            hash_calc(report_loc_resources)
            hash_value = hash_calc(report_loc_resources)
            print ("La tarea 'Resources' fue ejecutada en la fecha:", today, '\n')
            print ("El hash del reporte", report_name, 'es:\n', hash_value, "\n Y se encuentra en la siguiente ubicación:\n")
            print (report_loc_resources) 

        elif option == 3:
            print("Ejecutando 'RevealHiddenFiles'...")
            pspy.revealhf()
            report_name = "revealhf_report.txt"
            report_loc_revealhf = os.path.join (report_loc, report_name)
            hash_calc(report_loc_revealhf)
            hash_value = hash_calc(report_loc_revealhf)
            print ("La tarea 'RevealHiddenFiles' fue ejecutada en la fecha:", today, '\n')
            print ("El hash del reporte", report_name, 'es:\n', hash_value, "\n Y se encuentra en la siguiente ubicación:\n")
            print (report_loc_revealhf) 

        elif option == 4:
            print("Ejecutando 'VirusTotalHashCheck'...")
            pspy.vthashcheck()
            report_name = "vthashcheck_report.txt"
            report_loc_vthashcheck = os.path.join (report_loc, report_name)
            hash_calc(report_loc_vthashcheck)
            hash_value = hash_calc(report_loc_vthashcheck)
            print ("La tarea 'RevealHiddenFiles' fue ejecutada en la fecha:", today, '\n')
            print ("El hash del reporte", report_name, 'es:\n', hash_value, "\n Y se encuentra en la siguiente ubicación:\n")
            print (report_loc_vthashcheck) 

        else:
            print("Saliendo al menú principal...")
            val = False 
        
        if args.cibertarea:
            val = False

#Menu de python
def menu_py():
    val = True
    while val:
        if args.cibertarea:
            option = int(args.cibertarea)
        else:
            print("¿Qué módulo de Python quiere usar?")
            print("-----------------------------------------")
            print("1. File_Encrypt")
            print("2. Port_Scan")
            print("3. Shodan_Search")
            print("4. IPAbuse_Search")
            print("5. InternetDB_Search")
            print("6. Salir al menú principal")
            print("-----------------------------------------")
            option = input("Ingrese la opción: ")

            while not (option.isdigit() and 1 <= int(option) <= 6):
                print ("Ingrese un número válido del 1 al 5.")
                option = input("Ingrese una opción: ")

        option = int(option)
        if option == 1:
            print("Ejecutando 'File_Encrypt'...")
            pypy.file_encrypt()
            report_name = "file_encrypt_results.txt"
            report_loc_loginlogs = os.path.join (report_loc, report_name)
            hash_value = hash_calc(report_loc_loginlogs)
            print ("La tarea 'File_Encrypt' fue ejecutada en la fecha:", today, '\n')
            print ("El hash del reporte", report_name, 'es:\n', hash_value, "\n Y se encuentra en la siguiente ubicación:\n")
            print (report_loc_loginlogs)            

        elif option == 2:
            print("Ejecutando 'Port_Scan'...")
            pypy.port_scan()
            report_name = "port_scan_results.txt"
            report_loc_resources = os.path.join (report_loc, report_name)
            hash_calc(report_loc_resources)
            hash_value = hash_calc(report_loc_resources)
            print ("La tarea 'Port_Scan' fue ejecutada en la fecha:", today, '\n')
            print ("El hash del reporte", report_name, 'es:\n', hash_value, "\n Y se encuentra en la siguiente ubicación:\n")
            print (report_loc_resources) 

        elif option == 3:
            print("Ejecutando 'Shodan_Search'...")
            pypy.shodan_search()
            report_name = "shodan_search_results.txt"
            report_loc_revealhf = os.path.join (report_loc, report_name)
            hash_calc(report_loc_revealhf)
            hash_value = hash_calc(report_loc_revealhf)
            print ("La tarea 'Shodan_Search' fue ejecutada en la fecha:", today, '\n')
            print ("El hash del reporte", report_name, 'es:\n', hash_value, "\n Y se encuentra en la siguiente ubicación:\n")
            print (report_loc_revealhf) 

        elif option == 4:
            print("Ejecutando 'IPAbuse_Search'...")
            pypy.ipabuse_search()
            report_name = "ipabuse_search_results.txt"
            report_loc_vthashcheck = os.path.join (report_loc, report_name)
            hash_calc(report_loc_vthashcheck)
            hash_value = hash_calc(report_loc_vthashcheck)
            print ("La tarea 'IPAbuse_Search' fue ejecutada en la fecha:", today, '\n')
            print ("El hash del reporte", report_name, 'es:\n', hash_value, "\n Y se encuentra en la siguiente ubicación:\n")
            print (report_loc_vthashcheck) 
        
        elif option == 5:
            print("Ejecutando 'InternetDB_Search'...")
            pspy.vthashcheck()
            report_name = "internetdb_search_results.txt"
            report_loc_vthashcheck = os.path.join (report_loc, report_name)
            hash_calc(report_loc_vthashcheck)
            hash_value = hash_calc(report_loc_vthashcheck)
            print ("La tarea 'InternetDB_Search' fue ejecutada en la fecha:", today, '\n')
            print ("El hash del reporte", report_name, 'es:\n', hash_value, "\n Y se encuentra en la siguiente ubicación:\n")
            print (report_loc_vthashcheck) 
            
        else:
            print("Saliendo al menú principal...")
            val = False 
        
        if args.cibertarea:
            val = False


def hash_calc(report_path):  
    file_obj = open (report_path, "rb")
    file = file_obj.read()
    hash = hashlib.sha512(file)
    hashed_res = hash.hexdigest()
    return hashed_res


#Identificación de sistema operativo
if sys.platform.startswith('linux'):
    print ("Se detectó que su sistema operativo es Linux.")
    print ("Tendrá acceso a 11/11 módulos.")
    menu_main_linux()
    
    
elif sys.platform.startswith('darwin'):
    print ("Se detectó que su sistema operativo es MacOS.")
    print ("Tendrá acceso a 9/11 módulos, con excepción de los módulos de Bash.")
    menu_main_mac()

elif sys.platform.startswith('win32'):
    print ("Se detectó que su sistema operativo es Windows.")
    print ("Tendrá acceso a 9/11 módulos, con excepción de los módulos de Bash.")
    menu_main_windows()

else:
    print ("Su sistema operativo no es conocido.")
    print ("De todas maneras, tendrá acceso a 11/11 módulos.")
    menu_main_linux()
