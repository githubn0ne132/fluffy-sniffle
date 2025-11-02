# --- Configuration ---
$pythonVersion = "3.11.4"
$pythonArch = "amd64"
$pythonDistUrl = "https://www.python.org/ftp/python/$pythonVersion/python-$pythonVersion-embed-$pythonArch.zip"
$pythonDirName = "python-$pythonVersion-embed-$pythonArch"
$pythonZipName = "$pythonDirName.zip"
$pythonExecutable = Join-Path -Path $pythonDirName -ChildPath "python.exe"
$requirementsFile = "requirements.txt"
$envFile = ".env"

# --- Helper Functions ---
function Download-File {
    param(
        [string]$Url,
        [string]$Filename
    )
    Write-Host "Downloading $Url..."
    try {
        Invoke-WebRequest -Uri $Url -OutFile $Filename
    } catch {
        Write-Host "Error downloading file: $_"
        exit 1
    }
}

function Extract-Zip {
    param(
        [string]$Filename,
        [string]$DestDir
    )
    Write-Host "Extracting $Filename to $DestDir..."
    try {
        Expand-Archive -Path $Filename -DestinationPath $DestDir -Force
    } catch {
        Write-Host "Error extracting zip file: $_"
        exit 1
    }
}

function Get-Pip {
    Write-Host "Ensuring pip is available..."
    $getPipUrl = "https://bootstrap.pypa.io/get-pip.py"
    $getPipScript = "get-pip.py"
    Download-File -Url $getPipUrl -Filename $getPipScript

    try {
        & ./$pythonExecutable $getPipScript
    } catch {
        Write-Host "Error running get-pip.py: $_"
        exit 1
    }

    Remove-Item $getPipScript
}

function Install-Dependencies {
    Write-Host "Installing dependencies from $requirementsFile..."
    try {
        & ./$pythonExecutable -m pip install -r $requirementsFile
    } catch {
        Write-Host "Error installing dependencies: $_"
        exit 1
    }
}

function Create-EnvFile {
    Write-Host "Creating $envFile file..."
    $absPath = (Resolve-Path -Path $pythonExecutable).Path
    Set-Content -Path $envFile -Value "PYTHON_EXECUTABLE=$absPath"
}

function Verify-Installation {
    Write-Host "Verifying installation..."
    try {
        $result = & ./$pythonExecutable --version
        Write-Host "Python version: $result"
        Write-Host "Installation successful!"
    } catch {
        Write-Host "Verification failed: $_"
        exit 1
    }
}

# --- Main ---
if (-not (Test-Path -Path $pythonDirName)) {
    if (-not (Test-Path -Path $pythonZipName)) {
        Download-File -Url $pythonDistUrl -Filename $pythonZipName
    }
    Extract-Zip -Filename $pythonZipName -DestDir "."
    Remove-Item $pythonZipName
} else {
    Write-Host "Python directory already exists. Skipping download and extraction."
}

Get-Pip
Install-Dependencies
Create-EnvFile
Verify-Installation