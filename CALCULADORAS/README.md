# Gramáticas de Calculadora

Este proyecto contiene tres calculadoras implementadas usando Bison y Flex, cada una con diferentes reglas de precedencia para las operaciones aritméticas. Las calculadoras están diseñadas para evaluar expresiones matemáticas y demostrar cómo las diferentes precedencias afectan los resultados.

## Gramáticas Implementadas

1. **EXP1**: 
   - Precedencia: `(), *, /, -, +`
   - Ejemplo: `2 + 3 * 4` → Resultado: `14`

2. **EXP2**: 
   - Precedencia: `(), +, -, /, *`
   - Ejemplo: `2 + 3 * 4` → Resultado: `20`

3. **EXP3**: 
   - Precedencia: `*, /, -, +, ()`
   - Ejemplo: `2 + 3 * 4` → Resultado: `14`

## Instalación

### Instalación de Bison y Flex

Antes de compilar y ejecutar el proyecto, debes asegurarte de tener instalados **Bison** y **Flex**. 

### En Linux:

```bash
sudo apt update
sudo apt install bison flex
```
## Instrucciones de Compilación
Al ingresar se encuentran 3 carpetas nombradas ```'EXP1', 'EXP2', 'EXP3'``` dentro de cada una de ellas se encuentran los archivos referentes a cada gramatica es decir esta el ```.y``` y el ```.l``` para poder hacer la respectiva compilación.

Para compilar el proyecto, ejecuta los siguientes comandos en la terminal:

#### Para EXP1
```bash
bison -d EXP1.y
flex calculator.l
gcc EXP1.tab.c lex.yy.c -o EXP1
```
#### Para EXP2
```bas
bison -d EXP2.y
flex calculator.l
gcc EXP2.tab.c lex.yy.c -o EXP2
```

#### Para EXP3
```bash
bison -d EXP3.y
flex calculator.l
gcc EXP3.tab.c lex.yy.c -o EXP3
```

## Ejecución:
Dentro de cada carpeta se creara su respectivo ejecutable despues de la compilacion correcta.
Una vez compiladas, puedes ejecutar cada calculadora de la siguiente manera:
```bash
./EXP1
./EXP2
./EXP3
```

## Ejemplo de Uso:
```bash
> 2 + 3 * 4
= 14  # Para EXP1 y EXP3
> 2 + 3 * 4
= 20  # Para EXP2
```
