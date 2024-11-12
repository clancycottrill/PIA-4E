import requests
import json
import sys
import simplejson
import os

class API:
    def __init__(self, apikey):
        self.apikey = apikey
        self.url = "https://api.abuseipdb.com/api/v2/"
        self.h = {
            "Accept" : "application/json",
            "Key" : self.apikey
        }

    def checkip(self, ipaddress, maxdays=90):
        url= self.url + "check"
        parameters = {
            "ipAddress" : ipaddress,
            "maxAgeInDays" : maxdays
        }
        try:
            response = requests.get(url, headers=self.h, params=parameters)
            return response.json()
        
        except requests.exceptions.ConnectionError:
            return {"error": "Error de conexión. Verifica tu conexión a internet."}
        
        except requests.exceptions.Timeout:
            return {"error": "La solicitud ha excedido el tiempo de espera."}
        
        except requests.exceptions.RequestException as e:
            return {"error": f"Error inesperado: {str(e)}"}
        
        except simplejson.errors.JSONDecodeError:
            return {"error": "Error al procesar la respuesta en formato JSON."}

def main():
    f_output = open("ipabuse_search_results.txt", "a")  

    apikey = input("Introduzca su apikey de ipabuse: ")
    ipaddress = input("Introduzca la IP a verificar: ")
    api = API(apikey)
    resultado = api.checkip(ipaddress)
    f_output.write(f"Resultado de la verificación de IP {ipaddress}:\n")
    f_output.write(json.dumps(resultado, indent=4))  
    f_output.write("\n\n")

if __name__ == "__main__":
    main()
