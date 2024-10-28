from primera_capa import tokenize
from analizador_sintactico import AnalizadorSintactico

def leer_archivo(archivo_ruta):
    try:
        with open(archivo_ruta, 'r') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_ruta}' no se encontró.")
        exit(1)

def escribir_en_archivo(resultado, archivo_salida):
    with open(archivo_salida, 'w') as archivo:
        archivo.write(f"{resultado}\n")

def main():
    archivo_ruta = 'archivo_fuente.py'
    archivo_salida = 'resultado_sintactico.txt'
    
    codigo = leer_archivo(archivo_ruta)
    tokens, errores = tokenize(codigo, [])
    
    if errores:
        escribir_en_archivo("Errores léxicos encontrados", archivo_salida)
        return
    
    analizador = AnalizadorSintactico(tokens)
    resultado = analizador.analizar()
    
    escribir_en_archivo(resultado, archivo_salida)
    print(f"Análisis sintáctico completado. Resultado guardado en {archivo_salida}")

if __name__ == "__main__":
    main()
