# Reconocimiento de Tokens con LEX

Este proyecto contiene un programa en LEX que permite el reconocimiento de tokens específicos en una cadena de entrada. El programa está diseñado para identificar y mostrar los valores de los tokens reconocidos, así como manejar casos en los que se encuentren tokens no reconocidos.

## Descripción del Programa

El programa en LEX define patrones que permiten identificar y clasificar los siguientes tokens en una cadena de entrada:

- **NUMBER**: Números enteros (Ej. `3`, `7`, `42`)
- **ADD**: Símbolo de adición `+`
- **SUB**: Símbolo de sustracción `-`
- **MUL**: Símbolo de multiplicación `*`
- **DIV**: Símbolo de división `/`
- **ABS**: Palabra clave `abs` que representa valor absoluto
- **EOL**: Fin de línea (representado por `\n`)

## Instrucciones para Compilación y Ejecución

Para compilar y ejecutar el programa, siga los siguientes pasos:

1. **Compilación del archivo LEX:**
   - Diríjase a la carpeta donde se encuentra almacenado el archivo `Ej4.l`.
   - Compile el archivo LEX con el siguiente comando:  
     ```bash
     lex Ej4.l
     ```

2. **Compilación del código C generado:**
   - Compile el código C generado con el comando:  
     ```bash
     gcc lex.yy.c -o Ejecutable4 -lm
     ```

3. **Ejecución del programa:**
   - Ejecute el programa proporcionando un archivo de texto como argumento:  
     ```bash
     ./Ejecutable4 archivo.txt
     ```

   - Asegúrese de que el archivo de texto `archivo.txt` contenga la cadena que desea analizar.

## Ejemplos de Entrada y Salida:

### Archivo de texto (`archivo.txt`):
```
3+7(4-9) - abs
```

### Salida del programa:
```
TOKEN: NUMBER, VALUE: 3
TOKEN: ADD, VALUE: +
TOKEN: NUMBER, VALUE: 7
TOKEN NO RECONOCIDO: (
TOKEN: NUMBER, VALUE: 4
TOKEN: SUB, VALUE: -
TOKEN: NUMBER, VALUE: 9
TOKEN NO RECONOCIDO: )
TOKEN: SUB, VALUE: -
TOKEN: ABS, VALUE: abs
```

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras un problema o tienes una mejora, no dudes en abrir un *issue* o enviar un *pull request*
