# Proyecto de Algoritmos de Gramáticas

Este proyecto implementa algoritmos para calcular los conjuntos de **PRIMEROS**, **SIGUIENTES** y **PREDICCIONES** de gramáticas en Python. Las gramáticas se cargan desde un archivo de texto y los resultados se imprimen en la consola.

## Requisitos

- Python 3.6 o superior

## Instalación

1. **Instalar Python:**
   - Descarga la última versión de Python desde [python.org](https://www.python.org/downloads/).
   - Sigue las instrucciones del instalador. Asegúrate de marcar la opción "Add Python to PATH" durante la instalación.

2. **Verificar la Instalación:**
   - Abre una terminal.
   - Escribe el siguiente comando y presiona Enter:
     ```bash
     python --version
     ```
   - Deberías ver la versión de Python instalada.

3. **Clonar el Repositorio:**
   - Clona el repositorio de GitHub (si está disponible) o copia el código fuente a tu máquina local.

4. **Crear un Archivo de Gramática:**
   - Crea un archivo llamado `gramatica.txt` en el mismo directorio que el script de Python y define tu gramática según el formato requerido.

## Uso

Para ejecutar el programa, abre una terminal en el directorio del proyecto y ejecuta el siguiente comando:

```bash
python nombre_del_script.py
```
Reemplaza ```nombre_del_script.py``` con el nombre del archivo que contiene el código.

El archivo `gramatica.txt` se puede modificar por varias gramaticas diferentes, aca mostramos unos ejemplos de gramaticas que se podrian emplear.

## Ejemplos de Gramáticas 
#### 1. Gramatica 1:
```bash
S -> A B | C
A -> a | ε
B -> b
C -> c
```
#### 2. Gramatica 2:
```bash
A -> B C
A -> ant A all
B -> big C
B -> bus A boss
B -> ε
C -> cat
C -> cow
```
#### 3. Gramatica 3:
```bash
S -> A uno B C
S -> S dos
A -> B C D
A -> tres
A -> ε
B -> D cuatro C tres
B -> ε
C -> cinco D B
C -> ε
D -> seis
D -> ε
```
#### 4. Gramatica 4:
```bash
S -> A B uno
A -> dos B
A -> ε
B -> C D
B -> tres
B -> ε
C -> cuatro A B 
C -> cinco
D -> seis
D -> ε
```

Al replazar la gramatica del `gramatica.txt` y dependiendo del algorito que se ejute en el `nombre_del_script.py`, mostrara ya sea el conjunto de **PRIMEROS**, **SIGUIENTES** o **PREDICCIONES**. 
