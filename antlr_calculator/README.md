# Proyecto de Calculadora en Java con ANTLR

## Introducción

Este proyecto implementa una calculadora en ANTLR que permite evaluar expresiones matemáticas y obtener el resultado en la pantalla. La calculadora es simple, interactiva, y puede manejar operaciones básicas como suma, resta, multiplicación, división y valor absuluto.

## Instalación de ANTLR en Kali Linux
#### 1. Instalar Java:
Asegúrate de tener Java instalado en tu sistema. Puedes instalarlo usando el siguiente comando:
```bash
sudo apt-get update
sudo apt-get install openjdk-11-jdk
```
#### 2. Descargar ANTLR:
Descarga el archivo JAR de ANTLR desde el sitio web oficial:
```bash
wget https://www.antlr.org/download/antlr-4.13.0-complete.jar
```

#### 3. Configurar ANTLR:
Coloca el archivo JAR descargado en un directorio de tu elección y configura la variable de entorno CLASSPATH. Por ejemplo:
```bash
export CLASSPATH=".:/path/to/antlr-4.13.0-complete.jar"
```
Agrega esto a tu archivo ~/.zshrc para que se configure automáticamente cada vez que abras una terminal.

#### 4. Agregar el comando ANTLR:
Crea un alias para el comando ANTLR:
```bash
alias antlr4='java -jar /path/to/antlr-4.13.0-complete.jar'
```
Nuevamente, agrega esto a tu archivo ~/.zshrc para que se configure automáticamente.

#### 5. Instalar el complemento de Java para ANTLR:
Instala el complemento necesario para generar los archivos de código Java desde el archivo de gramática:
````bash
alias grun='java org.antlr.v4.gui.TestRig'
````
Agrega esto a tu archivo ~/.zshrc si es necesario.
------------------------------------FIN DE LA INSTALACIÓN ------------------------------------

## ¿Qué hace este proyecto?

- **Evalúa Expresiones Matemáticas:** Puedes ingresar una expresión como `2 + 3 * 4, 2+(2*2)` y la calculadora te dará el resultado correcto, siguiendo las reglas matemáticas.
- **Muestra el Árbol de Sintaxis:** Después de ingresar una expresión, la calculadora también te mostrará el "árbol de sintaxis", que es una representación visual de cómo la calculadora entiende la expresión.
- **Interactivo y Fácil de Usar:** Solo escribe tu expresión y presiona enter. Si quieres salir, simplemente escribe `salir`.

## ¿Cómo Funciona?

1. **Lexer y Parser:** El proyecto usa ANTLR, una herramienta que convierte la expresión matemática que escribes en un formato que la computadora puede entender.
2. **Visitor :** Este es el "cerebro" de la calculadora. Toma el formato que el Parser crea y realiza las operaciones matemáticas para darte el resultado.

## Pasos para Usar la Calculadora

#### 1. Clonar o Descargar el Proyecto

Primero, necesitas tener el código en tu computadora. Puedes descargarlo o clonarlo desde la carpeta del repositorio.

#### 2. Crear los Archivos de Gramática, Crea un directorio de trabajo:

````bash
mkdir ~/antlr_calculator
cd ~/antlr_calculator
````
Crea el archivo de gramática para la calculadora: Utiliza nano para crear un archivo llamado Calculator.g4.
````bash
nano Calculator.g4
````

#### 3. Generar el Código con ANTLR
Genera el código:
````bash
antlr4 Calculator.g4
````
Esto creará varios archivos Java que ANTLR usa para manejar la gramática.
Compila los archivos generados:
```bash
javac *.java
```
Esto va a crear los archivos necesarios para que la calculadora funcione.

#### 4. Crear el Código para la Calculadora
Crea el archivo de código en Java: Utiliza nano para crear un archivo llamado Calculator.java.
````bash
nano Calculator.java
````
Compila el archivo Calculator.java:
````bash
javac Calculator.java
````

#### 5. Ejecutar la Calculadora
Ejecuta el programa de la calculadora:
````bash
java Calculator
````

#### 6. Usar la Calculadora
- **Escribe una expresión:** Por ejemplo, `2 + 3 * 4`.
- **Ver el resultado:** La calculadora te mostrará el resultado inmediatamente.
- **Ver el árbol de sintaxis:** También te mostrará cómo la calculadora entiende la expresión.
- **Salir de la calculadora:** Escribe `salir` cuando quieras terminar.

## Ejemplos

- **Suma:** `3 + 5` te dará `8`.
- **Multiplicación:** `2 * 3` te dará `6`.
- **Orden de operaciones:** `2 + 3 * 4` te dará `14` porque la multiplicación se hace antes que la suma.
- **Operación con parentesis:** `(2+3)+(12/3)` te dara `8`.
- **División:** `24/2` te dara `12`, pero si dividimos cualquier numero por `0` la respuesta sera de infinito porque matemáticamente no hay un número finito que pueda multiplicarse por 0 para obtener el número original
- **Salir:** Escribe `salir` para cerrar la calculadora.

## Estructura del Código

### `Calculadora.java`

Este archivo es donde empieza todo. Aquí es donde ingresas la expresión, y la calculadora se encarga de todo lo demás.

- **Ingreso de Expresiones:** Te pide que escribas una expresión.
- **Procesamiento:** Usa el Lexer y Parser para entender la expresión.
- **Evaluación:** Usa el Visitor para calcular el resultado.
- **Manejo de Errores:** Si escribes algo que la calculadora no entiende, te avisará.

### `EvalVisitor.java`

Este archivo es el "cerebro" de la calculadora. Aquí es donde se calculan las operaciones matemáticas.

- **Operaciones Básicas:** Suma, resta, multiplicación y división.
- **Manejo de Errores:** Si hay un error en la expresión (como dividir por cero), la calculadora lo maneja.

## Requisitos

- **Java:** Necesitas tener Java instalado en tu computadora para compilar y ejecutar la calculadora.
- **ANTLR:** Esta herramienta es usada para generar el Lexer y Parser.
