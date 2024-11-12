import requests
import json
import logging
import os

def main():
    logging.basicConfig(
        filename='internetdb_search_logs.log',
        filemode='a',
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO
    )

    f_output = open("internetdb_search_results.txt", "a") 

    def search_internetdb(ip_address):
        url = f"https://internetdb.shodan.io/{ip_address}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                f_output.write(f"Resultados para la IP: {ip_address}\n")
                f_output.write(json.dumps(data, indent=4))  
                f_output.write("\n\n")
                print(f"Resultados guardados para la IP: {ip_address}")
                logging.info(f"Resultados guardados para la IP: {ip_address}")
            else:
                print(f"No se encontraron datos para la IP: {ip_address}")
                logging.warning(f"No se encontraron datos para la IP: {ip_address}")
        except Exception as e:
            print(f"Error al realizar la solicitud: {e}")
            logging.error(f"Error al realizar la solicitud para la IP {ip_address}: {e}")

    ip_address = input("Introduzca la IP que desea verificar en InternetDB: ")
    search_internetdb(ip_address)

if __name__ == "__main__":
    main()

