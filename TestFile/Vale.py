import os
import pandas as pd

def guardar_hello_world_en_excel():
    palabra = "Hello World"
    
    # Crear un DataFrame con la palabra "Hello World"
    df = pd.DataFrame({'Palabra': [palabra]})

    # Verificamos si la carpeta "/ruta/del/workspace/mi_proyecto/C:\Test" existe, si no, la creamos
    if not os.path.exists("/ruta/del/workspace/mi_proyecto/C:\\Test"):
        os.makedirs(os.path.join(os.environ['WORKSPACE'], "C:\\Test"), exist_ok=True)


    # Guardar el DataFrame en un archivo Excel en la carpeta "/ruta/del/workspace/mi_proyecto/C:\Test"
    archivo_excel = "/ruta/del/workspace/mi_proyecto/C:\\Test\\Hello_World.xlsx"
    df.to_excel(archivo_excel, index=False)
    print(f"El archivo '{archivo_excel}' ha sido creado y la palabra 'Hello World' ha sido guardada en él.")

if __name__ == "__main__":
    guardar_hello_world_en_excel()
