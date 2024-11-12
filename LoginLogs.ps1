<#
.SYNOPSIS
Módulo para revisar logs de inicios de sesión y cambios de contraseña de usuarios.

.DESCRIPTION
Este módulo muestra información acerca de los logs de seguridad, específicamente los logs de inicio de sesión y cambios de contraseña, así como los intentos fallidos de ambos. 

.PARAMETER NewLogs
Este parámetro hace referencia al número de los logs más recientes a revisar. Se espera que el usuario introduzca un número entero, pero en caso de introducir un flotante de todas maneras funcionará el script.

.EXAMPLE
. Get-LogInChanges -NewLogs 5

.NOTES
Este módulo forma parte de un script más grande, pero se puede seguir utilizando como un módulo independiente. Se le da como parámetro el número de logs más recientes que queremos mostrar, y después se muestra un menú para elegir la información que se quiere ver.
En este caso, se elije entre inicios de sesión exitosos/fallidos y cambios de contraseña exitosos/fallidos.

#>


Set-StrictMode -Version Latest
#Inicio de función 

function Get-LogInChanges {

#Definición de parámetros

    param (
    [Parameter (Mandatory=$True)]
    [string]$NewLogs
    )

#Verificación de NewLogs para que no se introduzcan valores negativos o strings.

$ValidateNL = 0

    try {

    if ([int]::TryParse($NewLogs, [ref]$ValidateNL)) {

        if ($ValidateNL -lt 1) {
            Write-Host "Número de logs inválido, debe ser un entero igual o mayor a 1." -ForegroundColor Yellow
            return
        }
    } else {
        Write-Host "El valor ingresado no es un número entero válido." -ForegroundColor Yellow
        return
    }
} catch {
    Write-Host "Error con la verificación del número de logs: $($_.Exception.Message)"
    return
}

    $salida = $False 

#Inicio de ciclo del menú
 
    while ($salida -eq $False) {

        $opcion = Read-Host -Prompt "¿Qué logs desea ver?
        [1] Inicios de sesión exitosos
        [2] Inicios de sesión fallidos
        [3] Cambios de contraseña exitosos
        [4] Cambios de contraseña fallidos
        [5] Salir"

        switch ($opcion) {
            1 {
                try {
                    $events = Get-EventLog -LogName Security -InstanceId 4624 -Newest $NewLogs -ErrorAction SilentlyContinue 
                    if ($events) {
                        $events | Format-Table TimeGenerated, UserName, Message -Wrap
                  } else {
                        Write-Host "No se encontraron logs de inicios de sesión" -ForegroundColor Red
                  }

                } catch {
                    Write-Host "Error al revisar los inicios de sesión exitosos: $($_.Exception.Message)" -ForegroundColor Red
            }
            break
            }
            2 {
                try {
                    $events = Get-EventLog -LogName Security -InstanceId 4625 -Newest $NewLogs -ErrorAction SilentlyContinue 
                    if ($events) {
                        $events | Format-Table TimeGenerated, UserName, Message -Wrap
                } else {
                    Write-Host "No se encontraron logs de inicios de sesión fallidos." -ForegroundColor Red
                }

                } catch {
                    Write-Host "Error al revisar los inicios de sesión fallidos: $($_.Exception.Message)" -ForegroundColor Red 
            }
            break
            }
            3 {
                try {
                    $events = Get-EventLog -LogName Security -InstanceId 4724 -Newest $NewLogs -ErrorAction SilentlyContinue 
                    if ($events) {
                        $events | Format-Table TimeGenerated, UserName, Message -Wrap
                } else {
                    Write-Host "No se encontraron logs de cambios de contraseña exitosos." -ForegroundColor Red
                }

                } catch {
                    Write-Host "Error al revisar los Cambios de contraseña exitosos: $($_.Exception.Message)" -ForegroundColor Red
            }
            break
            }
            4 {
                try {
                    Get-EventLog -LogName Security -InstanceId 4723 -Newest $NewLogs -ErrorAction SilentlyContinue 
                    if ($events) {
                        $events | Format-Table TimeGenerated, UserName, Message -Wrap
                } else {
                    Write-Host "No se encontraron logs de cambios de contraseña fallidos." -ForegroundColor Red
                }
                    
                } catch {
                    Write-Host "Error al revisar los Cambios de contraseña fallidos: $($_.Exception.Message)" -ForegroundColor Red
            }
            break
            }
            5 {
                $salida = $True
                Write-Host "Saliendo del módulo..." -ForegroundColor DarkMagenta
            break
            }
            default {
                Write-Host "Opción inválida" -ForegroundColor Red
            break
            }
        }
    }
}

Get-LogInChanges
