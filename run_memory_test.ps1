# run_memory_test.ps1

$testScript = "memory_test.py"

# Install dependencies
Write-Host "Installing dependencies from requirements.txt..."
try {
    python -m pip install -r "requirements.txt"
} catch {
    Write-Host "Error installing dependencies: $_"
    Write-Host "Please ensure Python is installed and in your PATH."
    exit 1
}

Write-Host "Running memory test..."
try {
    python $testScript
} catch {
    Write-Host "An error occurred while running the test script: $_"
    exit 1
}
