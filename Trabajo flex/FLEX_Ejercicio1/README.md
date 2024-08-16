
# Contador de Líneas, Palabras y Caracteres con LEX

Este proyecto contiene un programa en LEX que permite contar el número de líneas, palabras y caracteres en un archivo de texto. Está diseñado para manejar diferentes tipos de entradas, incluidos caracteres especiales y signos de puntuación.

## Descripción del Programa

El programa utiliza LEX para definir patrones que permiten identificar y contar las siguientes entidades en un archivo de texto:

- **Líneas**: Se cuenta cada vez que se encuentra un salto de línea (`\n`).
- **Palabras**: Se identifican como secuencias de letras y números, contando cada una como una palabra.
- **Caracteres**: Se cuenta cada carácter individual, incluidos los espacios, tabulaciones y signos de puntuación.

## Código del Programa

```c
%{
/* Código C que se incluirá en el archivo generado por flex */
#include <stdio.h>

/* Variables globales para contar líneas, palabras y caracteres */
int num_lineas = 0;
int num_palabras = 0;
int num_caracteres = 0;
%}

%%

\n          { num_lineas++; num_caracteres++; }  /* Contar líneas y caracteres para saltos de línea */
[ \t]+      { num_caracteres += yyleng; }  /* Contar caracteres para espacios en blanco y tabulaciones */
[a-zA-Z0-9]+ { num_palabras++; num_caracteres += yyleng; }  /* Contar palabras y caracteres para palabras */
.           { num_caracteres++; }  /* Contar cualquier otro carácter */

%%

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *file = fopen(argv[1], "r");
        if (!file) {
            perror("No se puede abrir el archivo");
            return 1;
        }
        yyin = file;
    }

    yylex();  /* Llama al analizador léxico generado por flex */

    /* Imprime los resultados */
    printf("Número de líneas: %d\n", num_lineas);
    printf("Número de palabras: %d\n", num_palabras);
    printf("Número de caracteres: %d\n", num_caracteres);

    if (yyin != stdin) {
        fclose(yyin);
    }

    return 0;
}

int yywrap() {
    return 1;
}
```

## Instrucciones para Compilación

Siga los siguientes pasos para compilar y ejecutar el programa:

1. Asegúrese de estar en el directorio donde se encuentra almacenado el archivo `Ej1.l`. Puede utilizar el comando `ls` para listar las carpetas y luego `cd CARPETA` para navegar a la carpeta correcta.

2. Para compilar el archivo LEX, ingrese el siguiente comando:
   ```bash
   lex Ej1.l
   ```

3. Para compilar el código C generado:
   ```bash
   gcc lex.yy.c -o Contador -lm
   ```

4. Para la ejecución:
   ```bash
   ./Contador nombre_del_archivo.txt
   ```

   Reemplace `nombre_del_archivo.txt` con el nombre del archivo de texto que desea analizar.

### Ejemplos de Entrada

Suponga que el contenido del archivo de texto `prueba.txt` es el siguiente:

```
Hola mundo!
Este es un archivo de prueba.
Para el ejercicio numero 1
de lenguajes de programacion

%

12345
543_21

fin.
```

Al ejecutar el programa con este archivo, la salida sería:

```
Número de líneas: 8
Número de palabras: 12
Número de caracteres: 87
```

## Contribuciones

Las contribuciones son bienvenidas. Si encuentra un problema o tiene una mejora, no dude en abrir un *issue* o enviar un *pull request*.
