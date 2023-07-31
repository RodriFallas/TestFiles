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
    repo = Repo(directorio_trabajo)
    repo.git.add(archivo_excel)

    # Hacer el commit con un mensaje
    commit_message = "Agregando archivo Excel generado por Jenkins"
    repo.index.commit(commit_message)

    # Cambiar a la rama "Rodrigo" y asegurarnos de que esté actualizada
    repo.git.pull('origin', 'Rodrigo')

    # Hacer push al repositorio remoto en GitHub
    remote_origin = repo.remote(name="origin")
    remote_origin.push()

    print(f"Se ha hecho el commit y el push al repositorio remoto en GitHub.")

if __name__ == "__main__":
    guardar_hello_world_en_excel()
