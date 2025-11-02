# run_memory_test.ps1

$envFile = ".env"
$testScript = "memory_test.py"

if (-not (Test-Path -Path $envFile)) {
    Write-Host "Error: .env file not found."
    Write-Host "Please run the setup_env.ps1 script first to create the environment."
    exit 1
}

# Read the .env file and extract the python executable path
$envContent = Get-Content -Path $envFile
$pythonExecutable = ""
foreach ($line in $envContent) {
    if ($line -match "^PYTHON_EXECUTABLE=(.+)") {
        $pythonExecutable = $matches[1]
        break
    }
}

if (-not ($pythonExecutable)) {
    Write-Host "Error: PYTHON_EXECUTABLE not found in .env file."
    exit 1
}

if (-not (Test-Path -Path $pythonExecutable)) {
    Write-Host "Error: Python executable not found at the specified path: $pythonExecutable"
    Write-Host "Please check the .env file or run setup_env.ps1 again."
    exit 1
}

# Install dependencies
Write-Host "Installing dependencies from requirements.txt..."
try {
    & $pythonExecutable -m pip install -r "requirements.txt"
} catch {
    Write-Host "Error installing dependencies: $_"
    exit 1
}

Write-Host "Running memory test using: $pythonExecutable"
try {
    & $pythonExecutable $testScript
} catch {
    Write-Host "An error occurred while running the test script: $_"
    exit 1
}
