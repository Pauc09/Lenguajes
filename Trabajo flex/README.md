# Ejercicios en LEX

En esta carpeta se encuentra 5 ejercicios diferentes para aprender a manejar la herramienta lex. Cada ejercicio está ubicado en su propia carpeta, y debes navegar a cada una de ellas para compilar y ejecutar el programa correspondiente.

## Estructura del Proyecto

El proyecto está organizado en carpetas, cada una conteniendo un ejercicio específico. A continuación, se describe cómo acceder a cada carpeta y ejecutar los programas.

### Ejercicios Disponibles

1. **Ejercicio 1**: Contar líneas, palabras y caracteres.
   - Carpeta: `FLEX_Ejercicio1/`
   - Archivo principal: `ejercicio1.l`

2. **Ejercicio 2**: Traductor de inglés a español.
   - Carpeta: `FLEX_Ejercicio2/`
   - Archivo principal: `ejercicio2.l`

3. **Ejercicio 3**: Reconocer símbolos y caracteres de la calculadora.
   - Carpeta: `FLEX_Ejercicio3/`
   - Archivo principal: `ejercicio3.l`
   
4. **Ejercicio 4**: Reconocimiento de tokens.
   - Carpeta: `FLEX_Ejercicio4/`
   - Archivo principal: `ejercicio4.l`
   
5. **Ejercicio 5**: Clasificación de números complejos.
   - Carpeta: `Ej5./`
   - Archivo principal: `Ej5.l`

## Instrucciones para Compilación y Ejecución

Para cada ejercicio, sigue estos pasos:

1. Abre una terminal y navega a la carpeta del ejercicio deseado:
   ```bash
   cd CARPETA
   Reemplaza `CARPETA` con el nombre de la carpeta correspondiente (por ejemplo, FLEX_Ejercicio1).
   
2. Para compilar cada archivo lex sigue las siguientes instrucciones:
   estando en la carpeta del ejercicio ejecuta el siguiente comando:
   ```bash
   flex NOMBRE_DEL_ARCHIVO.l
   
   Reemplaza NOMBRE_DEL_ARCHIVO.l con el nombre del archivo LEX en la carpeta (por ejemplo, ejercicio1.l).
   
3. Compila el código C generado:
   ```bash
   gcc lex.yy.c -o Ejecutable -lm
   
4. Ejecuta el programa:
   ```bash
   ./Ejecutable

###Contribuciones

Las contribuciones son bienvenidas. Si encuentras un problema o tienes una mejora, no dudes en abrir un issue o enviar un pull request.
