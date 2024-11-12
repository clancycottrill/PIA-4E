import subprocess
import os

script_route = os.getcwd()  #Getcurrentworkingdirectory! Para conseguir la ruta de donde estamos ejecutando el script


def loginlogs():

    mod_route = os.path.join (script_route, 'LoginLogs.ps1') #usamos os.path.join para juntar el directorio actual con el script de ps
    try:
        result = subprocess.run (["powershell", "-Executionpolicy", "Bypass", "-File", mod_route], capture_output=True, text=True)

        if result.stdout:
            with open('loginlogs_report.txt', 'a') as r:
                r.write("Resultados generados por módulo 'LoginLogs'")
                r.write("\n \n")
                r.write(result.stdout)

        else:
            with open('loginlogs_report.txt', 'a') as r:
                r.write("Sin resultados.'")
                r.write("\n \n")

        if result.stderr:
            print("Error en módulo 'LoginLogs'.")
            with open('loginlogs_report.txt', 'a') as r:
                r.write("Error en módulo 'LoginLogs'")
                r.write("\n \n")
                r.write(result.stderr)


    except Exception as e:
        print("Error al ejecutar 'LoginLogs':", e)


def resources():
    mod_route = os.path.join (script_route, 'Resources.ps1')
    try:
        result = subprocess.run (["powershell", "-Executionpolicy", "Bypass", "-File", mod_route], capture_output=True, text=True)

        if result.stdout:
            with open('resources_report.txt', 'a') as r:
                r.write("Resultados generados por módulo 'Resources'")
                r.write("\n \n")
                r.write(result.stdout)

        else:
            with open('resources_report.txt', 'a') as r:
                r.write("Sin resultados.'")
                r.write("\n \n")

        if result.stderr:
            with open('resources_report.txt', 'a') as r:
                r.write("Error en módulo 'Resources'")
                r.write("\n \n")
                r.write(result.stderr)

    except Exception as e:
        print("Error al ejecutar 'Resources':", e)


def revealhf():
    mod_route = os.path.join (script_route, 'RevealHiddenFiles.ps1')
    try:
        result = subprocess.run (["powershell", "-Executionpolicy", "Bypass", "-File", mod_route], capture_output=True, text=True)

        if result.stdout:
            with open('revealhf_report.txt', 'a') as r:
                r.write("Resultados generados por módulo 'RevealHiddenFiles'")
                r.write("\n \n")
                r.write(result.stdout)

        else:
            with open('revealhf_report.txt', 'a') as r:
                r.write("Sin resultados.'")
                r.write("\n \n")

        if result.stderr:
            with open('revealhf_report.txt', 'a') as r:
                r.write("Error en módulo 'RevealHiddenFiles'")
                r.write("\n \n")
                r.write(result.stderr)

    except Exception as e:
        print("Error al ejecutar 'RevealHiddenFiles':", e)


def vthashcheck():
    mod_route = os.path.join (script_route, 'VirusTotalCheck.ps1')
    try:
        result = subprocess.run (["powershell", "-Executionpolicy", "Bypass", "-File", mod_route], capture_output=True, text=True)

        if result.stdout:
            with open('vthashcheck_report.txt', 'a') as r:
                r.write("Resultados generados por módulo 'VirusTotalHashCheck'")
                r.write("\n \n")
                r.write(result.stdout)

        else:
            with open('vthashcheck_report.txt', 'a') as r:
                r.write("Sin resultados.'")
                r.write("\n \n")

        if result.stderr:
            with open('vthashcheck_report.txt', 'a') as r:
                r.write("Error en módulo 'VirusTotalHashCheck'")
                r.write("\n \n")
                r.write(result.stderr)

    except Exception as e:
        print("Error al ejecutar 'VirusTotalHashCheck':", e)

