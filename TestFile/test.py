import os
import pandas as pd
from git import Repo

def guardar_hello_world_en_excel():
    palabra = "Hello World"

    # Crear un DataFrame con la palabra "Hello World"
    df = pd.DataFrame({'Palabra': [palabra]})

    # Obtenemos la ruta del directorio de trabajo actual de Jenkins
    directorio_trabajo = os.environ['WORKSPACE']

    # Guardar el DataFrame en un archivo Excel en el directorio de trabajo de Jenkins
    archivo_excel = os.path.join(directorio_trabajo, "Hello_World.xlsx")
    df.to_excel(archivo_excel, index=False)
    print(f"El archivo '{archivo_excel}' ha sido creado y la palabra 'Hello World' ha sido guardada en él.")

    # Agregar el archivo Excel al área de preparación de Git
    repo = Repo.init(directorio_trabajo)  # Inicializar el repositorio en el directorio de trabajo
    repo.index.add([archivo_excel])

    # Hacer el commit con un mensaje
    commit_message = "Agregando archivo Excel generado por Jenkins"
    repo.index.commit(commit_message)

    # Verificar si el control remoto 'origin' ya existe
    if 'origin' in [remote.name for remote in repo.remotes]:
        remote_origin = repo.remote('origin')
    else:
        # Crear el control remoto 'origin' si no existe
        url = 'https://140.82.114.4/RodriFallas/TestFiles.git'
        remote_origin = repo.create_remote('origin', url=url)

    # Hacer push al repositorio remoto en la rama "main"
    remote_origin.push("HEAD:main")

    print(f"Se ha hecho el commit y el push al repositorio remoto en la rama 'main'.")

if __name__ == "__main__":
    guardar_hello_world_en_excel()
