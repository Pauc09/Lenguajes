
# Clasificación de Números Complejos con LEX

Este proyecto contiene un programa en LEX que permite la clasificación de números complejos en diferentes categorías: números reales, imaginarios y complejos. El programa está diseñado para reconocer varios formatos de números complejos, incluyendo formas rectangulares y polares.

## Descripción del Programa

El programa en LEX define patrones que permiten identificar y clasificar los siguientes tipos de números:

- **Números Reales**: Ej. `3.14`, `-2`, `2.5e10`
- **Números Imaginarios**: Ej. `4i`, `-3.14i`
- **Números Complejos**: Ej. `2.5+4.3i`, `-1.5e2-3.7e2i`
- **Forma Polar**: Ej. `3∠45`, `exp(iπ)`

## Instrucciones para Compilación

Por consola, diríjase a la carpeta donde se encuentra almacenado el ejercicio `Ej5.l`. Si no sabe cómo llegar allí, simplemente en la consola ingrese el comando `ls`, y este le mostrará todas las carpetas. Al observar dónde está su archivo, ingrese el siguiente comando para acceder a la carpeta deseada: `cd CARPETA` (reemplazando `CARPETA` con el nombre de la carpeta a la que desea ingresar). Repita el proceso hasta llegar a la carpeta donde está el archivo.

Ya en la carpeta correcta, haga lo siguiente:

- Para compilar el archivo LEX ingrese el siguiente comando:  
  ```bash
  lex Ej5.l
  ```

- Para compilar el código C generado:  
  ```bash
  gcc lex.yy.c -o Ejecutable5 -lm
  ```

- Para la ejecución:  
  ```bash
  ./Ejecutable5
  ```

### Ejemplos de Entrada:

- `3.14` -> Número real
- `4i` -> Número imaginario
- `2.5+4.3X10e4i` -> Número complejo
- `3∠45` -> Forma polar

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras un problema o tienes una mejora, no dudes en abrir un *issue* o enviar un *pull request*.
