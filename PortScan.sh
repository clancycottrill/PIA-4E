#!/bin/bash

# Función para realizar el primer escaneo de puertos con nmap y verificando puertos con netcat.
function PortScan1 {
    read -p "Introduzca la direccion IP o el rango de IPs a escanear por ejemplo puede probar con ""127.0.0.1"" :" ip_range
    read -p "Introduzca el rango de puertos a escanear (por ejemplo, 1-100): " port_range
    echo "Escaneando puertos con nmap..."
    nmap -p $port_range $ip_range -oG - | grep "/open" > nmap_results.txt

    echo "Verificando puertos abiertos con netcat..."

    while read -r line; do 
        ip=$(echo $line | awk '{print $2}')
        ports=$(echo $line | grep -oP '\d+/open' | cut -d '/' -f 1)
        for port in $ports; do 
            nc -zv $ip $port 2>&1 | grep -q "open" && echo "Puerto $port en $ip está abierto"
        done
    done < nmap_results.txt
}

# Función para realizar el segundo escaneo de puertos con nmap y verificando puertos con netcat.
function PortScan2 {
    read -p "Introduzca la dirección IP o el rango de IPs a escanear por ejemplo puede probar con ""127.0.0.1"" :" ip_range
    read -p "Introduzca el rango de puertos a escanear (por ejemplo, 1-100): " port_range
    echo "Escaneando puertos con nmap..."

    echo "Verificando puertos abiertos con netcat..."
    nmap_output=$(nmap -p $port_range $ip_range -oG - | grep "/open")
    while read -r line; do 
        ip=$(echo $line | awk '{print $2}')
        ports=$(echo $line | grep -oP '\d+/open' | cut -d '/' -f 1)
        for port in $ports; do 
            nc -zv $ip $port 2>&1 | grep -q "open" && echo "Puerto $port en $ip está abierto"
        done
    done <<< "$nmap_output"
}

# Condición infinita para ejecutar la función PortScan1 o PortScan2 y dar la opción de generar el archivo txt con los resultados.
while true; do
    read -p "¿Desea generar un archivo txt donde se guarden los resultados del escaneo? (Introduzca S para SI o N para NO): " var
    case $var in
        [sS])
            while true; do 
                PortScan1
                read -p "Desea ejecutar otra vez la funcion? (Introduzca S para SI o N para NO): " fun
                case $fun in
                    [sS])
                        continue;;
                    [nN])
                        break;;
                    *)
                        echo "Opción inválida, por favor ingrese (S/N)";;
                esac
            done
            break;;
        [nN])
            while true; do
                PortScan2
                read -p "Desea ejecutar otra vez la función? (Introduzca S para SI o N para NO): " fun
                case $fun in
                    [sS])
                        continue;;
                    [nN])
                        break;;
                    *)
                        echo "Opción inválida, por favor ingrese (S/N)";;
                esac
            done
            break;;
        *)
            echo "Opción inválida, por favor ingrese (S/N)";;
    esac
done

