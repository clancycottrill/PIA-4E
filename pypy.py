import os
import subprocess

def file_encrypt():
    try: 
        subprocess.run(["python", "file_encrypt.py"])
    except Exception as e:
        print(f"Error al ejecutar uno de los scripts: {e}")

def port_scan():
    try: 
        subprocess.run(["python", "port_scan.py"])
    except Exception as e:
        print(f"Error al ejecutar uno de los scripts: {e}")

def shodan_search():
    try: 
        subprocess.run(["python", "shodan_search.py"])
    except Exception as e:
        print(f"Error al ejecutar uno de los scripts: {e}")

def ipabuse_search():
    try: 
        subprocess.run(["python", "ipabuse_search.py"])
    except Exception as e:
        print(f"Error al ejecutar uno de los scripts: {e}")

def internetdb_search():
    try: 
        subprocess.run(["python", "internetdb_search.py"])
    except Exception as e:
        print(f"Error al ejecutar uno de los scripts: {e}")



