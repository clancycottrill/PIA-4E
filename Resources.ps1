<#
.Sinopsis
Modulo para revisar el uso de recursos del sistema (Memoria, disco, procesador y red)

.Description 
Este módulo muestra informacion sobre el espacio libre en memoria y disco o el uso del procesador y las estadisticas de red! 

.Example
Get-InfoCPU

.Notes
Este módulo forma parte de un script mas extenso pero se puede seguir usando como un modulo independiente.
Solo eligiendo la funcion que se desea ejecutar

#>


#https://adamtheautomator.com/get-wmiobject/

#Los parametros de "TotalVisibleMEmorySize" y "FreePhysicalMemory" los saque con el comando: "Get-WMIObject -Class Win32_OperatingSystem | format-list *"

#Los calculos matematicos para convertir a GB si los saque con ayuda de IA:)




Function Get-InfoMemory {
    Get-WMIObject -Class Win32_OperatingSystem | Select-Object @{Name="TotalVisibleMemorySize (GB)";Expression={[math]::round($_.TotalVisibleMemorySize/ 1MB, 2)}}`
    , @{Name="FreePhysicalMemory (GB)";Expression={[math]::round($_.FreePhysicalMemory/ 1MB, 2)}} | Format-List
}

#https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-psdrive?view=powershell-7.4
Function Get-InfoDisk {
    Get-PsDrive -PSProvider FileSystem | Select-Object Name, @{Name="Used (GB)";Expression={[math]::round($_.Used/ 1GB, 2)}}`
     ,@{Name="Free (GB)";Expression={[math]::round($_.Free/ 1GB, 2)}} | Format-List
}

#https://learn.microsoft.com/en-us/powershell/module/cimcmdlets/get-ciminstance?view=powershell-7.4
Function Get-InfoCPU {
    Get-CimInstance -ClassName Win32_Processor | Select-Object DeviceID, Name, @{Name="LoadPercentage";Expression={$_.LoadPercentage}} | FOrmat-List
    $CPU=Read-Host "Quiere obtener informacion mas detallada del CPU? Si(s)/No(n): "
    if ($CPU -eq "s"){
            Get-CimInstance -ClassName Win32_Processor | Format-List *
        }
}


#Esto si lo investigue con IA, me parecia poco practico poner por separado los comandos de "Get-NetAdapter" y "Get-NetAdapterStatistics"
Function Get-InfoNet {
    $adapters = Get-NetAdapter
    $adapters | ForEach-Object {
        $stats = Get-NetAdapterStatistics -Name $_.Name
        [PSCustomObject]@{
        Name              = $_.Name
        Status            = $_.Status
        LinkSpeed         = $_.LinkSpeed
        MacAddress        = $_.MacAddress
        ReceivedBytes     = [math]::round($stats.ReceivedBytes / 1MB, 2)
        SentBytes         = [math]::round($stats.SentBytes / 1MB, 2)
        }
    }
}

#Referencias: https://www.youtube.com/watch?v=UIxpx2Aohxs

Get-InfoMemory 
Get-InfoDisk
Get-InfoCPU
Get-InfoNet