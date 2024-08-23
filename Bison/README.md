
# Calculadora Usando Bison y Flex

Este proyecto es una calculadora simple implementada utilizando Bison (Yacc) y Flex (Lex). La calculadora puede realizar operaciones aritméticas básicas y manejar errores de sintaxis simples.

## Características
- **Operaciones Aritméticas:** Suma, resta, multiplicación, división y valor absoluto.
- **Manejo de Errores:** 
  - Detecta y reporta errores de sintaxis cuando se ingresan caracteres inválidos.
  - Maneja la división por cero con un mensaje de error específico.
  - Reporta expresiones incompletas con un mensaje de error específico.
- **Soporte para Paréntesis:** Soporta expresiones anidadas con paréntesis.

## Archivos
- **Calculadora.y**: El archivo Bison que contiene las reglas gramaticales y el manejo de errores.
- **Calculadora.l**: El archivo Flex para el análisis léxico y la generación de tokens.

## Instrucciones de Compilación

### Requisitos
- Bison instalado
- Flex instalado
### si no tienes instalado Bison sigue los siguientes pasos desde la terminal de linux:
1. **actualizar la lista de paquetes**
   ```sh
    sudo apt-get update
    ```

2. **Instalar Bison:**
    ```sh
    sudo apt-get install bison
    ```

3. **Verificar la instalación:**
   ```sh
    bison --version
    ```
**-----------------Fin de la instalación--------------------**


### Pasos a seguir para compilación correcta:
1. **Compilar el archivo Flex**: 
    ```sh
    flex Calculadora.l
    ```

2. **Compilar el archivo Bison**: 
    ```sh
    bison -d Calculadora.y
    ```

3. **Compilar los archivos C generados**: 
    ```sh
    gcc lex.yy.c Calculadora.tab.c -o calculadora -ll
    ```

4. **Ejecutar la calculadora**:
    ```sh
    ./calculadora
    ```

## Uso

Una vez que el programa esté en ejecución, te pedirá que ingreses una expresión aritmética. Puedes ingresar expresiones como:
- `2 + 2`
- `3 * (4 + 5)`
- `ABS(-7)`

Si ingresas una expresión inválida, el programa te notificará del error y te pedirá que ingreses otra expresión.

### Ejemplo

```sh
Ingrese una expresión: 2 + 2
-->Respuesta: = 4
Ingrese una expresión: 3 / 0
-->Respuesta: Error: división por cero
Ingrese una expresión: 3gyr+4
-->Respuesta: Error: syntax error
Ingrese una expresión: 2 +
-->Respuesta: Error: Expresión incompleta
Ingrese una expresión:
```

