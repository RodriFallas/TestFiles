import os
import pandas as pd

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

if __name__ == "__main__":
    guardar_hello_world_en_excel()
