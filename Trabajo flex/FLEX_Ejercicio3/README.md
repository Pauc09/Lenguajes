# Proyecto de Analizador Léxico con LEX

Este proyecto implementa un analizador léxico en lenguaje C utilizando LEX. El analizador está diseñado para reconocer y clasificar los tokens en expresiones matemáticas, como los que se encuentran en una calculadora básica. A continuación, se proporcionan los pasos detallados para clonar el repositorio, verificar los archivos, compilar el código y ejecutar el programa en un entorno Linux.

## Requisitos
Antes de comenzar, asegúrate de que tu sistema cumpla con los siguientes requisitos:


•	Sistema operativo: Linux.

•	FLEX: Herramienta necesaria para procesar el archivo LEX y generar el código en C.


•	gcc: Compilador de C para compilar el código generado y crear el ejecutable.

•	Acceso a la terminal: Para ejecutar los comandos necesarios.


### Nota:
Si FLEX o GCC no están instalados, puedes instalarlos con los siguientes comandos:

•	Para instalar FLEX: sudo apt-get install flex.

•	Para instalar GCC: sudo apt-get install gcc.


## Clonar el Repositorio
Primero, necesitas clonar el repositorio que contiene el proyecto. Abre la terminal y ejecuta el siguiente comando:

`git clone <URL_DEL_REPOSITORIO>`

### Nota: Reemplaza <URL_DEL_REPOSITORIO> con la URL real del repositorio que deseas clonar.
## Navegar al Directorio del Proyecto
Una vez que el repositorio esté clonado, debes navegar al directorio del proyecto. Usa el siguiente comando:
`cd <NOMBRE_DEL_DIRECTORIO>`

### Nota: Reemplaza '<NOMBRE_DEL_DIRECTORIO>'con el nombre del directorio que contiene los archivos del proyecto.
## Verificar los Archivos
Asegúrate de que los archivos necesarios estén presentes en el directorio. Deberías ver los siguientes archivos:


•	calculadora.l: Archivo LEX que define las reglas de reconocimiento para los distintos tokens (números, operadores, paréntesis).

•	lex.yy.c: Archivo C generado automáticamente por FLEX a partir de calculadora.l.


•	calculadora: Ejecutable que se generará después de compilar el archivo lex.yy.c.

•	README.md: Este archivo con las instrucciones.


Para verificar esto, utiliza el siguiente comando:
`ls`

## Compilar el Código Fuente

Primero, debes generar el archivo C a partir del archivo LEX utilizando FLEX. Ejecuta el siguiente comando en la terminal:
`flex calculadora.l`
Esto creará un archivo llamado  `lex.yy.c` en el mismo directorio.
A continuación, compila el archivo `lex.yy.c` utilizando `gcc`:
`gcc lex.yy.c -o calculadora -lfl`
Este comando generará un archivo ejecutable llamado 'calculadora'.
## Ejecutar el Programa
Una vez que hayas compilado el código, puedes ejecutar el programa utilizando el archivo ejecutable `calculadora`. Ejecuta el siguiente comando:
`./calculadora`

El programa ahora estará listo para procesar y reconocer los tokens en las expresiones matemáticas que introduzcas.
##Probar el Programa
Cuando ejecutes el programa, podrás ingresar expresiones matemáticas. El analizador léxico reconocerá y clasificará los diferentes tokens, como números, operadores aritméticos y paréntesis.
## Ejemplo
`Ingrese una expresión: 3 + (4 * 5)`
El programa mostrará una clasificación de cada token que encuentra en la expresión.




