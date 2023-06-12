# import python library
import os
import sys
# import zeppelin2nb module
from ze2nb import ze2nb

# Ruta del directorio actual
curr_dir = os.getcwd()

# Obtener una lista de nombres de carpetas en el directorio actual
folders = [nombre for nombre in os.listdir(
    curr_dir) if os.path.isdir(os.path.join(curr_dir, nombre))]

skipfolders = [".git", ".metals", ".vscode"]


def check_file_content(file_name):
    try:
        # Open the file in read mode
        with open(file_name, 'r', encoding='utf-8') as file:
            # Read the content of the file
            content = file.read()

            # Check if the content is empty
            if content:
                return True
            else:
                return False

    except FileNotFoundError:
        return False


# Example usage
file_name = "file.txt"
check_file_content(file_name)

# Recorrer los nombres de las carpetas
for folder in folders:
    file = folder + "/" + 'note.json'

    if folder in skipfolders or not check_file_content(file):
        print("SKIPPING: ", folder)
        continue

    print(folder)
    ze2nb(file)