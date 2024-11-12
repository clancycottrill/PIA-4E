#!/usr/bin/python3

import subprocess
import os
import hashlib
from datetime import datetime
import time

def menu_bash():

    def calculate_hash(file_path):
        """Función para calcular el hash SHA256 de un archivo"""
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            while True:
                byte_block = f.read(4096)
                if not byte_block:
                    break
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()


    def execute_script(script_name, report_name):
        script_path = os.path.join(os.getcwd(), script_name)
        report_path = os.path.join(os.getcwd(), report_name)
        
        try:
            with open(report_path, 'w') as report:
                print(f"Ejecutando el script {script_name}...")
                result = subprocess.run(['bash', script_path], capture_output=True, text=True)
                report.write("Output:\n")
                report.write(result.stdout)
                if result.stderr:
                    report.write("\nError:\n")
                    report.write(result.stderr)
            hash_report = calculate_hash(report_path)
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Tarea '{script_name}' ejecutada el: {current_date}")
            print(f"Hash del reporte: {hash_report}")
            print(f"Ubicación y nombre del archivo: {report_path}")
            print(f"Reporte generado: {report_name}")
        except Exception as e:
            print(f"Ocurrió un error al ejecutar {script_name}: {e}")


    while True:
        print("Seleccione el script de Bash que desea ejecutar:")
        print("1) PortScan.sh")
        print("2) HoneyPotCreation.sh")

        opcion = input("Introduzca el número correspondiente (1 o 2): ")

        if opcion == "1":
            execute_script('PortScan.sh', 'portscan_report.txt')
            break
        elif opcion == "2":
            execute_script('HoneyPotCreation.sh', 'honeypot_report.txt')
            break
        else:
            print("Opción inválida. Por favor, ingrese 1 o 2.")

    print("Script ejecutado correctamente.")

