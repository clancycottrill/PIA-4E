import requests 
import json 
import logging 
import shodan
import os

def main():
    logging.basicConfig(
        filename='shodan_search_logs.log',
        filemode='a',
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO
    )

    f_output = open("shodan_search_results.txt", "a")  

    def shodan_request(apikey, ip): 
        shodanobj = shodan.Shodan(apikey)
        try:
            results = shodanobj.search(f"ip:{ip} country:MX has_vuln:True")

            if results['total'] > 0:
                for result in results['matches']:
                    f_output.write(f"IP: {ip}\n")
                    f_output.write(f"Ciudad de la IP: {result['location'].get('city', 'Ciudad no identificada')}\n")
                    vulns = result.get('vulns', None)
                    if vulns:
                        f_output.write(f"Vulnerabilidades: {vulns}\n")
                        f_output.write(f"Vulnerabilidades totales: {len(vulns)}\n")
                    else:
                        f_output.write("No hay vulnerabilidades identificadas.\n")
            else:
                f_output.write(f"No se encontraron resultados para la IP {ip}.\n")

        except shodan.APIError as e:
            f_output.write(f"Error en la API de Shodan: {e}\n")

    apikey = input("Ingrese su API Key de Shodan: ")
    ip = input("Ingrese la IP a revisar: ")
    shodan_request(apikey, ip)

if __name__ == "__main__":
    main()
