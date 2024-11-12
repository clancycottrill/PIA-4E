# PIA-4E

Cuarto entregable del PIA de Programación para Ciberseguridad!

Este repositorio contiene los 11 módulos correspondientes al cuarto entregable del PIA de Programación para Ciberseguridad, además de un script principal y tres módulos independientes para manejar los 11 módulos mediante el uso de menús.

Contiene los siguientes módulos:

1. file_encrypt.py
2. ipabuse_search.py
3. port_scan.py
4. shodan_search.py
5. internetdb_search.py
6. VirusTotalCheck.ps1
7. LoginLogs.ps1
8. Resources.ps1
9. RevealHiddenFiles.ps1
10. PortScan.sh
11. HoneypotCreation.sh

Además, contiene los siguientes scripts y módulos extra para manejar los 11 módulos:
12. PIA-4E
13. pspy.py
14. pypy.py
15. shpy.py


======================================================

En cuanto a las funciones individuales de los módulos:

file_encrypt: Nuestro módulo complejo. Este módulo se encarga de encriptar y desencriptar archivos seleccionados por el usuario, así como proporcionar la llave necesaria para desencriptarlo en caso de querer hacerlo manualmente.

ipabuse_search: Este módulo se encarga de revisar la API AbuseIPDB para revisar actividades maliciosas reportadas por usuarios de internet.

port_scan: Este módulo se encarga de escanear los puertos de una IP ingresada por el usuario y determinar si está cerrado o abierto.

shodan_search: Este módulo se encarga de revisar la API de Shodan para analizar una IP específicamente que sea de México y reportar las vulnerabilidades reportadas por usuarios de internet. 

internetdb_search: Este módulo se encarga de revisar la API de Internetdb para conseguir hostnames, puertos abiertos y vulnerabilidades reportadas por usuarios de internet de alguna dirección IP.

VirusTotalCheck: Calcula los hashes de archivos en un directorio y consulta la API de VirusTotal para verificar su seguridad (cabe recalcar que la API se tiene que introducir manualmente, no viene integrada)

LoginLogs: Muestra información acerca de los logs de seguridad, específicamente los logs de inicio de sesión y cambios de contraseña, así como los intentos fallidos de ambos.

Resources: Muestra informacion sobre el espacio libre en memoria y disco o el uso del procesador y las estadisticas de red.

RevealHiddenFiles: Revisa un directorio específico dado por el usuario y ofrece las opciones de revisar tanto archivos y carpetas ocultos como los archivos y carpetas regulares en el directorio elegido.

PortScan: Escanea los puertos de la dirección IP que indique el usuario, así como un rango de puertos. Se le da la opción adicional al usuario de mandar los resultados a un archivo txt.

HoneypotCreation: Inicia una honeypot en el puerto indicado por el usuario, así como imprimir en la consola un reporte con cualquier intento de conexión al honeypot. Adicionalmente, se le da la opción al usuario de reiniciar el honeypot con otros puertos.

======================================================

Aclaraciones de los scripts:

Para el módulo 'LoginLogs.ps1': Se necesitan permisos de administrador para poder acceder a los logs de seguridad que el script utiliza, de lo contrario no se imprime la información correctamente.

Para el módulo 'shodan_search.py': El módulo está pensado para funcionar solamente con IPs localizadas en México. El módulo podría fallar usándolo con IPs fuera de México. 

Para el módulo 'shodan_search.py' y 'ipabuse_search.py': Para poder correr estos módulos, se necesitará una API Key de cada página. Para el módulo de 'shodan_search' específicamente, se necesita una cuenta arriba del nivel "gratis" para acceder a las vulnerabilidades, y que se ejecute correctamente.

Para el módulo 'PortScan': En caso de que no esté iniciado el servicio ssh, este módulo no funcionará. Se necesita correr la línea 'sudo systemctl start ssh.service' antes de correr el módulo.

Para el módulo 'HoneypotCreation': Al revisarse logs del sistema, se necesitan permisos de superuser (sudo). En caso de que no se muestren los logs, ejecute el script con 'sudo'.

======================================================

Realizado en conjunto por el equipo 5:

Santiago B.

Chris T.

Alexander T.
