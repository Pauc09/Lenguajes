
# Simple Calculator Using Bison and Flex

This project is a simple calculator implemented using Bison (Yacc) and Flex (Lex). The calculator can perform basic arithmetic operations and handle simple syntax errors.

## Features
- **Arithmetic Operations:** Addition, subtraction, multiplication, division, and absolute value.
- **Error Handling:** 
  - Detects and reports syntax errors when invalid characters are entered.
  - Handles division by zero with a specific error message.
  - Reports incomplete expressions with a specific error message.
- **Parentheses Support:** Supports nested expressions with parentheses.

## Files
- **Calculadora.y**: The Bison file containing grammar rules and error handling.
- **Calculadora.l**: The Flex file for lexical analysis and token generation.

## Compilation Instructions

### Requirements
- Bison
- Flex

### Steps
1. **Compile the Flex file**: 
    ```sh
    flex Calculadora.l
    ```

2. **Compile the Bison file**: 
    ```sh
    bison -d Calculadora.y
    ```

3. **Compile the generated C files**: 
    ```sh
    gcc lex.yy.c Calculadora.tab.c -o calculadora
    ```

4. **Run the calculator**:
    ```sh
    ./calculadora
    ```

## Usage

Once the program is running, it will prompt you to enter an arithmetic expression. You can enter expressions like:
- `2 + 2`
- `3 * (4 + 5)`
- `ABS(-7)`

If you enter an invalid expression, the program will notify you of the error and prompt you to enter another expression.

### Example

```sh
Ingrese una expresión: 2 + 2
= 4
Ingrese una expresión: 3 / 0
Error: división por cero
Ingrese una expresión: 3gyr+4
Error: syntax error
Ingrese una expresión: 2 +
Error: Expresión incompleta
Ingrese una expresión:
```

## License
This project is licensed under the MIT License.
