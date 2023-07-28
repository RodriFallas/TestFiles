import os
import pandas as pd

def guardar_hello_world_en_excel():
    palabra = "Hello World"
    
    # Crear un DataFrame con la palabra "Hello World"
    df = pd.DataFrame({'Palabra': [palabra]})

    # Verificamos si la carpeta "C:\Test" existe, si no, la creamos
    if not os.path.exists("C:\Test"):
        os.makedirs("C:\Test")

    # Guardar el DataFrame en un archivo Excel en la carpeta "C:\Test"
    archivo_excel = f"C:\\Test\\Hello_World.xlsx"
    df.to_excel(archivo_excel, index=False)
    print(f"El archivo '{archivo_excel}' ha sido creado y la palabra 'Hello World' ha sido guardada en él.")

if __name__ == "__main__":
    guardar_hello_world_en_excel()
