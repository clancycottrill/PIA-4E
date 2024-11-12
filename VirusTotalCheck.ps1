# Enable Strict Mode
Set-StrictMode -Version Latest

function Invoke-VirusTotalCheck {
    <#
    .SYNOPSIS
    Calcula los hashes de archivos en un directorio y consulta la API de VirusTotal para verificar su seguridad.

    .DESCRIPTION
    Esta función calcula los hashes SHA256 de todos los archivos en el directorio especificado y luego consulta la API de VirusTotal para identificar archivos potencialmente maliciosos.

    .PARAMETER Path
    La ruta al directorio que contiene los archivos a hash.

    .PARAMETER ApiKey
    Su clave API de VirusTotal para autenticación.

    .OUTPUTS
    System.Collections.Generic.List[PSObject]

    .EXAMPLE
    Invoke-VirusTotalCheck -Path "C:\Users\bauti\Documents" -ApiKey "your_api_key"

    Este comando calcula los hashes SHA256 de los archivos en el directorio especificado y consulta la API de VirusTotal con esos hashes.
    #>


    param (
        [Parameter(Mandatory = $true, HelpMessage = "Enter the directory path.")]
        [string]$Path,

        [Parameter(Mandatory = $true, HelpMessage = "Enter your VirusTotal API key.")]
        [string]$ApiKey
    )

    try {
        # Validar que la ruta exista
        if (-Not (Test-Path -Path $Path)) {
            throw [System.IO.DirectoryNotFoundException] "The specified path does not exist: $Path"
        }

        # Cálculo de los hashes de los archivos
        $files = Get-ChildItem -Path $Path -File
        $hashList = @()

        foreach ($file in $files) {
            $hash = Get-FileHash -Algorithm SHA256 -Path $file.FullName
            $hashList += [PSCustomObject]@{
                FileName = $file.Name
                FilePath = $file.FullName
                Hash     = $hash.Hash
            }
        }

        # Checar si la lista de hashes está vacía.
        if ($hashList.Count -eq 0) {
            Write-Output "No files found in the specified directory."
            return
        }

        # VirusTotal API
        $vtUrl = "https://www.virustotal.com/api/v3/files/"
        $results = @()

        foreach ($hash in $hashList) {
            $uri = "$vtUrl$($hash.Hash)"
            $response = Invoke-RestMethod -Uri $uri -Headers @{ "x-apikey" = $ApiKey } -Method Get
            $results += [PSCustomObject]@{
                FileName  = $hash.FileName
                FilePath  = $hash.FilePath
                Hash      = $hash.Hash
                Result    = $response.data.attributes.last_analysis_stats
            }
        }

        # Mostrar resultados
        $results | Format-Table -AutoSize

    } catch {
        Write-Error "An error occurred: $_"
    }
}


Invoke-VirusTotalCheck