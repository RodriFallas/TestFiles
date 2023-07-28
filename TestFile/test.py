import os
import pandas as pd

def guardar_hello_world_en_excel():
    # Crear un DataFrame con la palabra "Hello World"
    df = pd.DataFrame({'Palabra': ['Hello World']})

    # Verificamos si la carpeta "test" existe, si no, la creamos
    if not os.path.exists("test"):
        os.makedirs("test")

    # Guardar el DataFrame en un archivo Excel en la carpeta "test"
    archivo_excel = "test/Hello_World.xlsx"
    df.to_excel(archivo_excel, index=False)
    print(f"El archivo '{archivo_excel}' ha sido creado y la palabra 'Hello World' ha sido guardada en él.")

if __name__ == "__main__":
    guardar_hello_world_en_excel()
