from primera_capa import tokenize

def leer_archivo(archivo_ruta):
    """Lee el contenido de un archivo de código fuente."""
    try:
    	#Abre el archivo en modo lectura 
        with open(archivo_ruta, 'r') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_ruta}' no se encontró.")
        exit(1)

def analizar_lexico(codigo):
    """Aplica el análisis léxico sobre el código fuente y maneja errores."""
    tokens = []
    errores = []
    
    try:
    	#Tokenisar el codigo y captura errores 
        tokens = tokenize(codigo, errores)
        return tokens, errores
    except RuntimeError as e:
        print(e)
        exit(1)

def escribir_en_archivo(tokens, errores, archivo_salida):
    """Escribe los tokens y errores en un archivo de texto."""
    with open(archivo_salida, 'w') as archivo:
        for token in tokens:
            archivo.write(f"{token}\n")
        for error in errores:
            archivo.write(f"{error}\n")

def main():
    """Función principal que gestiona el flujo del análisis léxico."""
    archivo_ruta = 'archivo_fuente.py'
    archivo_salida = 'resultado_lexico.txt'
    
    codigo = leer_archivo(archivo_ruta)
    tokens, errores = analizar_lexico(codigo)
    
    # Guardar los tokens y errores en el archivo de salida
    escribir_en_archivo(tokens, errores, archivo_salida)
    print(f"Análisis léxico completado. Los tokens y errores se han guardado en {archivo_salida}")

if __name__ == "__main__":
    main()
