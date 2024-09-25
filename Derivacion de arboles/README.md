
# Árboles de Derivación para Gramáticas

Este programa permite generar y visualizar árboles de derivación basados en reglas gramaticales definidas por el usuario. El árbol se construye a partir de una cadena de entrada y las reglas de la gramática, y se muestra gráficamente.

## Funcionalidades
1. **Lectura de Gramática**: Se leen las reglas de una gramática desde un archivo (`grammar.txt`).
2. **Generación de Árbol de Derivación**: Genera un árbol a partir de una cadena ingresada por el usuario, basado en las reglas gramaticales.
3. **Validación de la Cadena**: Verifica si la cadena ingresada es válida según la gramática.
4. **Visualización del Árbol**: Muestra un árbol gráfico que representa la derivación de la cadena ingresada.
   
## Requisitos Previos
- Python 3.x
- `networkx`: `pip install networkx`
- `matplotlib`: `pip install matplotlib`
- `pygraphviz`: `pip install pygraphviz`

## Instrucciones de Instalación

### Clonar el Repositorio
Para descargar el código desde GitHub, utiliza el siguiente comando:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
```

Esto descargará el proyecto en tu máquina local.

### Instalar las Dependencias
Una vez que hayas clonado el repositorio, debes instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` debe contener las siguientes dependencias:
```txt
networkx
matplotlib
pygraphviz
```

### Ejecución del Programa
Para ejecutar el programa, sigue los siguientes pasos:

1. Coloca un archivo llamado `grammar.txt` en la misma carpeta donde está el código. Este archivo debe contener las reglas gramaticales en el formato:

```
Variable -> Producción
```

2. Abre una terminal y navega al directorio del proyecto:

```bash
cd tu_repositorio
```

3. Ejecuta el programa:

```bash
python main.py
```

4. Cuando se te solicite, ingresa una cadena que desees analizar según las reglas de la gramática.

### Ejemplos de Gramáticas:

1. **Gramática 1:**
```
S -> x S y | y S x | ε
```
   - Cadenas válidas: `xy`, `yx`, `xxyy`, `yyxx`, `xyxy`.

2. **Gramática 2:**
```
S -> D S | D
D -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```
   - Cadenas válidas: `0`, `1`, `99`, `123`, `567`.

3. **Gramática 3:**
```
S -> a S | A
A -> b A | ε
```
   - Cadenas válidas: `a`, `ab`, `aab`, `aaab`, `aaabb`.

## Visualización del Árbol
Si la cadena es válida, se mostrará un árbol gráfico que representa la derivación. Si la cadena no es válida, se indicará, pero el árbol aún se mostrará para entender cómo fue la derivación fallida.

## Contribución
Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu nueva funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`).
4. Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Abre un pull request y describe tus cambios.
