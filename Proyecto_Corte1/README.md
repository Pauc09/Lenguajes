
# Proyecto de Analizador Léxico en Python

## Integrantes:
##### Daniela López Rincón
##### Ana Maria Amador León 
##### Alan Steve OSorio Zuluaga 
##### Paula Caballero 


Este proyecto implementa un analizador léxico en Python para procesar un código fuente, identificando y clasificando los diferentes tokens presentes en el archivo.

## ¿Qué hace?

El analizador léxico lee un archivo fuente en Python y genera una lista de tokens con su tipo y posición (línea y columna) dentro del código. Los tokens reconocidos incluyen:
- Palabras clave (como `def`, `class`, `if`)
- Identificadores
- Operadores
- Cadenas de texto
- Paréntesis, puntos, comas, etc.

Además, también detecta errores como cadenas de texto no cerradas.

## ¿Cómo funciona?

1. El código fuente se carga desde un archivo.
2. El analizador recorre línea por línea el archivo, identificando los diferentes tokens.
3. Cada token se clasifica y se guarda con su información de línea y columna.
4. Los resultados del análisis se escriben en un archivo de salida.

## Archivos

- `analizador_lexico.py`: Implementación del analizador léxico que realiza la identificación de tokens.
- `archivo_fuente.py`: Archivo fuente de ejemplo que se analizará con el analizador léxico.
- `primera_capa.py`: Módulo adicional utilizado en el análisis léxico o como parte de la lógica del proyecto.
- `resultado_lexico.txt`: Archivo de salida que contiene el resultado del análisis léxico con la lista de tokens identificados.
- `primera_capa.cpython-311.pyc`: Archivo compilado de Python (bytecode) generado por el intérprete Python.

## ¿Cómo ejecutar el proyecto?

1. Clona el repositorio o descarga los archivos a tu máquina local.
2. Asegúrate de tener Python 3 instalado.
3. Coloca el archivo fuente a analizar en la misma carpeta que el analizador léxico.
4. Ejecuta el analizador con el siguiente comando:

   ```bash
   python3 analizador_lexico.py archivo_fuente.py
   ```

5. El resultado del análisis léxico se guardará en `resultado_lexico.txt`.

## Ejemplo de salida

```txt
<class,1,1>
<id,Animal,1,7>
<tk_par_izq,1,13>
<object,1,14>
<tk_par_der,1,20>
<tk_dos_puntos,1,21>
<id,makes_noise,2,5>
<tk_dos_puntos,2,16>
```

## Notas

- Asegúrate de que los archivos estén en la misma carpeta para evitar problemas de rutas.
- El código puede extenderse fácilmente para soportar más tokens o lenguajes.
