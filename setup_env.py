import os
import subprocess
import sys
import requests
import zipfile

# --- Configuration ---
PYTHON_VERSION = "3.11.4"
PYTHON_ARCH = "amd64"
PYTHON_DIST_URL = f"https://www.python.org/ftp/python/{PYTHON_VERSION}/python-{PYTHON_VERSION}-embed-{PYTHON_ARCH}.zip"
PYTHON_DIR_NAME = f"python-{PYTHON_VERSION}-embed-{PYTHON_ARCH}"
PYTHON_ZIP_NAME = f"{PYTHON_DIR_NAME}.zip"
PYTHON_EXECUTABLE = os.path.join(PYTHON_DIR_NAME, "python.exe")
REQUIREMENTS_FILE = "requirements.txt"
ENV_FILE = ".env"

def download_file(url, filename):
    """Downloads a file from a URL to a local filename."""
    print(f"Downloading {url}...")
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        sys.exit(1)

def extract_zip(filename, dest_dir):
    """Extracts a zip file to a destination directory."""
    print(f"Extracting {filename} to {dest_dir}...")
    try:
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall(dest_dir)
    except zipfile.BadZipFile as e:
        print(f"Error extracting zip file: {e}")
        sys.exit(1)

def get_pip():
    """
    Ensures pip is installed in the embedded Python distribution.
    This is a common step for embeddable Python versions.
    """
    print("Ensuring pip is available...")
    # The embeddable package for python doesn't come with pip.
    # We need to install it manually.
    # First, get the get-pip.py script
    get_pip_url = "https://bootstrap.pypa.io/get-pip.py"
    get_pip_script = "get-pip.py"
    download_file(get_pip_url, get_pip_script)

    # Now, run the script with our embedded python
    subprocess.run([PYTHON_EXECUTABLE, get_pip_script], check=True)

    # Clean up the script
    os.remove(get_pip_script)


def install_dependencies():
    """Installs dependencies from requirements.txt using the local Python."""
    print(f"Installing dependencies from {REQUIREMENTS_FILE}...")
    try:
        subprocess.run([PYTHON_EXECUTABLE, "-m", "pip", "install", "-r", REQUIREMENTS_FILE], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def create_env_file():
    """Creates a .env file with the path to the local Python executable."""
    print(f"Creating {ENV_FILE} file...")
    with open(ENV_FILE, "w") as f:
        f.write(f"PYTHON_EXECUTABLE={os.path.abspath(PYTHON_EXECUTABLE)}\n")

def verify_installation():
    """Verifies the Python installation by checking the version."""
    print("Verifying installation...")
    try:
        result = subprocess.run([PYTHON_EXECUTABLE, "--version"], capture_output=True, text=True, check=True)
        print(f"Python version: {result.stdout.strip()}")
        print("Installation successful!")
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Verification failed: {e}")
        sys.exit(1)

def main():
    """Main function to set up the Python environment."""
    if not os.path.exists(PYTHON_DIR_NAME):
        if not os.path.exists(PYTHON_ZIP_NAME):
            download_file(PYTHON_DIST_URL, PYTHON_ZIP_NAME)
        extract_zip(PYTHON_ZIP_NAME, ".") # Extract to current directory
        os.remove(PYTHON_ZIP_NAME) # Clean up the zip file
    else:
        print("Python directory already exists. Skipping download and extraction.")

    get_pip()
    install_dependencies()
    create_env_file()
    verify_installation()

if __name__ == "__main__":
    main()
