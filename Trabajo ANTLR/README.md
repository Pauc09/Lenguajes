# Proyecto de Calculadora en Java con ANTLR

## Introducción

 Este proyecto implementa una calculadora en ANTLR que permite evaluar expresiones matemáticas como `3 + 4` o `5 * 6`, y obtener el resultado en la pantalla. La calculadora es simple, interactiva, y puede manejar operaciones básicas como suma, resta, multiplicación y división entre otras.

## ¿Qué hace este proyecto?

- **Evalúa Expresiones Matemáticas:** Puedes ingresar una expresión como `2 + 3 * 4` y la calculadora te dará el resultado correcto, siguiendo las reglas matemáticas.
- **Muestra el Árbol de Sintaxis:** Después de ingresar una expresión, la calculadora también te mostrará el "árbol de sintaxis", que es una representación visual de cómo la calculadora entiende la expresión.
- **Interactivo y Fácil de Usar:** Solo escribe tu expresión y presiona enter. Si quieres salir, simplemente escribe `salir`.

## ¿Cómo Funciona?

1. **Lexer y Parser:** El proyecto usa ANTLR, una herramienta que convierte la expresión matemática que escribes en un formato que la computadora puede entender.
2. **Visitor :** Este es el "cerebro" de la calculadora. Toma el formato que el Parser crea y realiza las operaciones matemáticas para darte el resultado.

## Pasos para Usar la Calculadora

### 1. Clonar o Descargar el Proyecto

Primero, necesitas tener el código en tu computadora. Puedes descargarlo o clonarlo desde la carpeta del repositorio.

### 2. Compilar el Código

Abre la terminal y asegúrate de estar en la carpeta donde descargaste el proyecto. Luego, ejecuta el siguiente comando para compilar el código:

```bash
javac *.java
```

Esto va a crear los archivos necesarios para que la calculadora funcione.

### 3. Ejecutar la Calculadora

Una vez que el código esté compilado, puedes ejecutar la calculadora con el siguiente comando:

```bash
java Calculadora
```

### 4. Usar la Calculadora

- **Escribe una expresión:** Por ejemplo, `2 + 3 * 4`.
- **Ver el resultado:** La calculadora te mostrará el resultado inmediatamente.
- **Ver el árbol de sintaxis:** También te mostrará cómo la calculadora entiende la expresión.
- **Salir de la calculadora:** Escribe `salir` cuando quieras terminar.

## Ejemplos

- **Suma:** `3 + 5` te dará `8`.
- **Multiplicación:** `2 * 3` te dará `6`.
- **Orden de operaciones:** `2 + 3 * 4` te dará `14` porque la multiplicación se hace antes que la suma.
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