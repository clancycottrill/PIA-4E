from cryptography.fernet import Fernet, InvalidToken
import os
import logging


def write_to_txt(message):
    with open("file_encrypt_results.txt", "a") as txt_file:
        txt_file.write(message + "\n")

def main():
    logging.basicConfig (filename = 'Encrypt-Decrypt_Files.log',
                     filemode = 'a',
                     format ="%(asctime)s - %(levelname)s - %(message)s",
                     datefmt = "%m/%d/%Y %I:%M:%S %p", level = logging.INFO)

    def generate_key():
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        logging.info(f'Clave generada: {key}')
        write_to_txt(f'Clave generada: {key}')  
    def load_key():
        try:
            return open("secret.key", "rb").read()
        except FileNotFoundError:
            print("Error: El archivo de clave 'secret.key' no se encontró.")
            logging.warning('El archivo ''secret.key'' no se encontro')
            write_to_txt('Error: El archivo de clave "secret.key" no se encontró.')  
            return None

    def encrypt_file(file_name):
        key = load_key()
        if key is None:
            return
        fernet = Fernet(key)
        try:
            with open(file_name, "rb") as file:
                original = file.read()
            encrypted = fernet.encrypt(original)
            with open(file_name + ".encrypted", "wb") as encrypted_file:
                encrypted_file.write(encrypted)
            os.remove(file_name)
            message = f"{file_name} ha sido cifrado, eliminado y guardado como {file_name}.encrypted"
            print(message)
            logging.info(message)
            write_to_txt(message) 
        except Exception as e:
            print(f"Error al cifrar el archivo: {e}")
            logging.warning(f'No se pudo cifrar el archivo, ocurrio un error: {e}')
            write_to_txt(f'Error al cifrar el archivo: {e}')  

    def decrypt_file(file_name):
        key = load_key()
        if key is None:
            return
        fernet = Fernet(key)
        try:
            with open(file_name, "rb") as encrypted_file:
                encrypted = encrypted_file.read()
            decrypted = fernet.decrypt(encrypted)
            with open(file_name.replace(".encrypted", ""), "wb") as decrypted_file:
                decrypted_file.write(decrypted)
            os.remove(file_name)
            message = f"{file_name} ha sido descifrado y guardado como {file_name.replace('.encrypted', '')}"
            print(message)
            logging.info(message)
            write_to_txt(message)  
        except InvalidToken:
            print("Error: El archivo no es un archivo cifrado válido.")
            write_to_txt("Error: El archivo no es un archivo cifrado válido.")  
        except Exception as e:
            print(f"Error al descifrar el archivo: {e}")
            logging.warning(f'No se pudo descifrar el archivo, ocurrio un error: {e}')
            write_to_txt(f'Error al descifrar el archivo: {e}')  

    def ValidateFile(file_name):
        if os.path.exists(file_name):
            print(f"El archivo {file_name} existe")
            return True
        else:
            print(f"El archivo {file_name} no existe o no se puede acceder.")
            write_to_txt(f"El archivo {file_name} no existe o no se puede acceder.")  
            return False

    while True:
        x = input('¿Quiere cifrar un archivo? (s/n): ')
        
        if x == 's':
            print('Generando clave')

            generate_key()
            print('Clave guardada en el archivo: secret.key')
            logging.info('Clave guardada en el archivo  ''secret.key')
            write_to_txt('Clave guardada en el archivo  ''secret.key')  
            file_name = input('Ingrese la ruta completa del archivo que desea encriptar: ')
            try:
                if ValidateFile(file_name):
                    encrypt_file(file_name)
                else:
                    print('Por favor, ingrese un archivo que exista.')
            except Exception as e:
                print(f'Error: {e}')
                logging.warning(f'Ocurrió un error: {e}')
                write_to_txt(f'Ocurrió un error: {e}')  
                
        elif x == 'n':
            decrypt_choice = input('¿Quiere desencriptar un archivo? (s/n): ')
            if decrypt_choice == 's':
                file_name = input('Ingrese la ruta completa del archivo que desea desencriptar (debe tener la extensión .encrypted): ')
                try:
                    if ValidateFile(file_name):
                        decrypt_file(file_name)
                    else:
                        print('Por favor, ingrese un archivo que exista.')
                except Exception as e:
                    print(f'Error: {e}')
                    logging.warning(f'Ocurrió un error: {e}')
                    write_to_txt(f'Ocurrió un error: {e}') 
            else:
                break
        else:
            print('Por favor, solo ingrese (s/n)')
            continue

main()
