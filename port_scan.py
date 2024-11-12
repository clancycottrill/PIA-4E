import socket
import sys
import re 
import logging
import os

def main():
    logging.basicConfig(
        filename='Information_Ports.log',
        filemode='a',
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO
    )

    f_output = open("port_scan_results.txt", "a")  

    def validar_ip(ip):
        patron = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
        return re.match(patron, ip) is not None

    def validar_puertos(PortList):
        for port in PortList:
            if not (0 <= port <= 65535):
                return False
        return True

    def Arguments():
        PortList=[]
        while True:
            ip=input('Ingrese la IP en la que desea hacer el escaneo:')
            if validar_ip(ip):
                break
            else:
                print('Dirección IP no válida.')
        while True:
            try:
                ports = input('Ingrese los puertos que desea escanear separados por una coma (ej. 80, 443):')
                PortList=[int(p) for p in ports.split(',')]
                if not validar_puertos(PortList):
                    raise ValueError('Rango de puertos incorrecto.')
                break
            except ValueError as e:
                print(f'Error: {e}')
        return ip, PortList

    def escanear_puertos(ip, PortList):
        for port in PortList:
            try:
                socket.setdefaulttimeout(1)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((ip, port))
                f_output.write(f'Puerto {port} abierto\n')  
                logging.info(f'Puerto {port} abierto')
            except:
                f_output.write(f'Puerto {port} cerrado\n')  
                logging.info(f'Puerto {port} cerrado')

    ip, PortList = Arguments()
    escanear_puertos(ip, PortList)

if __name__ == "__main__":
    main()


