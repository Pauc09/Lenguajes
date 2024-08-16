# Traductor de Inglés a Español con LEX

Este proyecto contiene un programa en LEX diseñado para traducir un texto en inglés al español. El programa fue trabajado desde la consola de Kali Linux y está configurado para reconocer y traducir un conjunto específico de palabras en inglés a sus correspondientes traducciones en español. También maneja números y otros caracteres que no forman parte del vocabulario definido.

## Descripción del Programa

El programa en LEX define patrones para identificar y traducir las siguientes palabras en inglés:

- **cat** -> gato
- **dog** -> perro
- **book** -> libro
- **apple** -> manzana
- **school** -> escuela
- **house** -> casa
- **car** -> coche
- **water** -> agua
- **computer** -> computadora
- **food** -> comida
- **moon** -> luna
- **sea** -> mar
- **fire** -> fuego
- **star** -> estrella
- **farm** -> granja

El programa también maneja números y otros caracteres que no se encuentran en el vocabulario definido.

## Instrucciones para Compilación

1. Coloque el archivo LEX `ejercicio2.l` en la carpeta deseada.

2. Para compilar el archivo LEX, ingrese el siguiente comando:

    ```bash
    lex ejercicio2.l
    ```

3. Para compilar el código C generado, ingrese:

    ```bash
    gcc lex.yy.c -o ejercicio2 -lfl
    ```

4. Para ejecutar el programa, utilice:

    ```bash
    ./Traductor Ej2.txt
    ```

   Donde `Ej2.txt` es el archivo de texto en inglés que desea traducir al español.

## Ejemplos de Entrada y Salida

### Entrada (Ej2.txt):

```
cat
dog
book
apple
school
house
car
water
computer
food
moon
sea
fire
star
farm
525258370
sun
planet
```

### Salida Esperada:

```
gato
perro
libro
manzana
escuela
casa
coche
agua
computadora
comida
luna
mar
fuego
estrella
granja
TOKEN NO RECONOCIDO
sun
planet
```

