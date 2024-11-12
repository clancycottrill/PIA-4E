#!/bin/bash

# Función para mostrar el menú principal
function show_menu() {
    echo "========================="
    echo "    Menú Honeypot de Puertos    "
    echo "========================="
    echo "1) Iniciar honeypot"
    echo "2) Generar reporte"
    echo "3) Reiniciar con otros puertos"
    echo "4) Salir"
    echo "========================="
    echo "Elige una opción: "
}

# Función para manejar errores
function handle_error() {
    echo "Error: $1"
    exit 1
}

# Función para validar el puerto.
function validate_port() {
    if [[ $1 -lt 1 || $1 -gt 65535 ]]; then
        handle_error "Número de puerto inválido: $1. Por favor, usa un puerto entre 1 y 65535."
    fi
}

# Función para iniciar el Honeypot.
function start_honeypot() {
    read -p "Introduce los puertos a monitorizar (por ejemplo, 21 22 80): " -a ports
    for port in "${ports[@]}"
    do
        validate_port $port
        nc -lvp $port >> /var/log/honeypot.log 2>&1 &
        if [[ $? -ne 0 ]]; then
            handle_error "Fallo al abrir el puerto $port."
        else
            echo "Honeypot escuchando en el puerto $port"
        fi
    done
    echo "Honeypot iniciado. Monitorizando: ${ports[@]}"
}

# Función para generar el reporte del Honeypot.
function generate_report() {
    echo "===================="
    echo "    Reporte del Honeypot    "
    echo "===================="
    if [[ -f /var/log/honeypot.log ]]; then
        echo "Entradas de registro del honeypot:"
        cat /var/log/honeypot.log
    else
        echo "No se encontraron registros. Es posible que el honeypot no esté en funcionamiento."
    fi
}

# Función para correr nuevamente el Honeypot con un puerto diferente.
function rerun_honeypot() {
    killall nc 2>/dev/null
    echo "Instancias anteriores del honeypot detenidas."
    start_honeypot
}

# Opciones del menú
while true; do
    show_menu
    read option

    case $option in
        1)
            start_honeypot
            ;;
        2)
            generate_report
            ;;
        3)
            rerun_honeypot
            ;;
        4)
            echo "Saliendo..."
            exit 0
            ;;
        *)
            echo "Opción inválida. Por favor, elige un número válido."
            ;;
    esac
done
