<#
.SYNOPSIS
Módulo para revisar archivos y carpetas ocultas en un directorio.

.DESCRIPTION
Este módulo revisa un directorio específico dado por el usuario y ofrece las opciones de revisar tanto archivos y carpetas ocultos como los archivos y carpetas regulares en el directorio elegido. 

.PARAMETER Folder
Ruta de la carpeta a revisar.

.EXAMPLE
.Get-Hidden -Folder "C:\ruta\a\carpeta"

.NOTES
Este módulo forma parte de un script más grande, pero se puede seguir utilizando como un módulo independiente. La única función que usa es "Get-Hidden", y se le da el parámetro de -Folder, junto a la ruta que se quiere revisar.

#>


Set-StrictMode -Version Latest

#Inicio de función
  
function Get-Hidden {

#Definición de parametros.

    param(
    [Parameter (Mandatory = $True)]
    [string]$Folder
)


#Verificación del directorio. 
    try {
    if (-not (Test-Path $Folder)) {
        Write-Host "El directorio $Folder no existe." -ForegroundColor Yellow
        return
        
        
    }
} catch {
    Write-Host "Error con la verificación del directorio: $($_.Exception.Message)"
    return
    
    
}
    
    $salida = $False 

#Inicio de ciclo del menú
 
    while ($salida -eq $False) {

        $opcion = Read-Host -Prompt "¿Qué información desea ver?
        [1] Solo archivos ocultos
        [2] Todos los archivos
        [3] Solo carpetas ocultas
        [4] Todas las carpetas
        [5] Todos los archivos y carpetas ocultas
        [6] Todos los archivos y carpetas
        [7] Salir"

        switch ($opcion) {
            1 {
                try {
                    $archivos = Get-ChildItem -Path $Folder -Attributes Hidden -File | Where-Object {$_.Attributes -match "Hidden"} 
                    if ($archivos) {
                        $archivos | Format-Table Name, Mode, LastWriteTime -Autosize
                    } else {
                        Write-Host "No se encontraron archivos ocultos en el directorio." -ForegroundColor Red
                    }

                } catch {
                    Write-Host "Error al revisar los archivos ocultos: $($_.Exception.Message)" -ForegroundColor Red
            }
            break
            }
            2 {
                try {
                    $archivos = Get-ChildItem -Path $Folder -File -Force 
                    if ($archivos) {
                        $archivos | Format-Table Name, Mode, LastWriteTime -Autosize
                    } else {
                        Write-Host "No se encontraron archivos en el directorio." -ForegroundColor Red
                    }
                } catch {
                    Write-Host "Error al revisar todos los archivos: $($_.Exception.Message)" -ForegroundColor Red 
            }
            break
            }
            3 {
                try {
                    $archivos = Get-ChildItem -Path $Folder -Attributes Hidden -Directory | Where-Object {$_.Attributes -match "Hidden"} 
                    if ($archivos) {
                        $archivos | Format-Table Name, Mode, LastWriteTime -Autosize
                    } else {
                        Write-Host "No se encontraron carpetas ocultas en el directorio." -ForegroundColor Red
                    }
                } catch {
                    Write-Host "Error al revisar las carpetas ocultas: $($_.Exception.Message)" -ForegroundColor Red
            }
            break
            }
            4 {
                try {
                    $archivos = Get-ChildItem -Path $Folder -Directory -Force 
                     if ($archivos) {
                        $archivos | Format-Table Name, Mode, LastWriteTime -Autosize
                    } else {
                        Write-Host "No se encontraron carpetas en el directorio." -ForegroundColor Red
                    }
                } catch {
                    Write-Host "Error al revisar todas las carpetas: $($_.Exception.Message)" -ForegroundColor Red
            }
            break
            }
            5 {
                try {
                    $archivos = Get-ChildItem -Path $Folder -Attributes Hidden | Where-Object {$_.Attributes -match "Hidden"} 
                    if ($archivos) {
                        $archivos | Format-Table Name, Mode, LastWriteTime -Autosize
                    } else {
                        Write-Host "No se encontraron archivos ocultos o carpetas ocultas en el directorio." -ForegroundColor Red
                    }
             } catch {
                    Write-Host "Error al revisar todos los archivos y carpetas ocultas: $($_.Exception.Message)" -ForegroundColor Red
            }
            break
            }
            6 {
                try {
                    $archivos = Get-ChildItem -Path $Folder -Force 
                    if ($archivos) {
                        $archivos | Format-Table Name, Mode, LastWriteTime -Autosize
                    } else {
                        Write-Host "No se encontraron archivos o carpetas en el directorio." -ForegroundColor Red
                    }
             } catch {
                Write-Host "Error al revisar todos los archivos y carpetas: $($_.Exception.Message)" -ForegroundColor Red 
            }
            break
            }
            7 {
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

Get-Hidden


