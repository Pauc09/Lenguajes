# Contador de Líneas, Palabras y Caracteres con LEX

Este proyecto contiene un programa en LEX que permite contar el número de líneas, palabras y caracteres en un archivo de texto. El programa está diseñado para manejar diferentes tipos de entradas, incluidos caracteres especiales y signos de puntuación.

## Descripción del Programa

El programa en LEX define patrones que permiten identificar y contar los siguientes elementos en un archivo de texto:

- **Líneas**: Se cuenta cada vez que se encuentra un salto de línea (`
`).
- **Palabras**: Se cuentan secuencias de caracteres alfanuméricos.
- **Caracteres**: Se cuenta cada carácter individual, incluidos espacios en blanco, tabulaciones y signos de puntuación.

## Instrucciones para Compilación y Ejecución

Para compilar y ejecutar el programa, siga los siguientes pasos:

1. **Compilación del archivo LEX:**
   - Diríjase a la carpeta donde se encuentra almacenado el archivo `Ej1.l`. 
   - Compile el archivo LEX con el siguiente comando:  
     ```bash
     lex Ej1.l
     ```

2. **Compilación del código C generado:**
   - Compile el código C generado con el comando:  
     ```bash
     gcc lex.yy.c -o ContadorEj1 -lm
     ```

3. **Ejecución del programa:**
   - Ejecute el programa proporcionando un archivo de texto como argumento:  
     ```bash
     ./ContadorEj1 archivo.txt
     ```

   - Asegúrese de que el archivo de texto `archivo.txt` contenga el texto que desea analizar.

## Ejemplos de Entrada y Salida:

### Archivo de texto (`archivo.txt`):
```
Hola mundo!
Este es un archivo de prueba.
Para el ejercicio numero 1
de lenguajes de programacion

12345
543_21

fin.
```

### Salida del programa:
```
Número de líneas: 9
Número de palabras: 21
Número de caracteres: 118
```

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras un problema o tienes una mejora, no dudes en abrir un *issue* o enviar un *pull request*.
