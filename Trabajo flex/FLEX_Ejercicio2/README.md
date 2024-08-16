# Traductor de Inglés a Español con LEX

Este proyecto contiene un programa en LEX diseñado para traducir un texto en inglés al español. El programa está configurado para reconocer y traducir un conjunto específico de palabras en inglés a sus correspondientes traducciones en español. También maneja números y otros caracteres que no forman parte del vocabulario definido.

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

1. Coloque el archivo LEX `traductor.l` en la carpeta deseada.

2. Para compilar el archivo LEX, ingrese el siguiente comando:

    ```bash
    lex traductor.l
    ```

3. Para compilar el código C generado, ingrese:

    ```bash
    gcc lex.yy.c -o Traductor -lm
    ```

4. Para ejecutar el programa, utilice:

    ```bash
    ./Traductor archivo.txt
    ```

   Donde `archivo.txt` es el archivo de texto en inglés que desea traducir al español.

## Ejemplos de Entrada y Salida

### Entrada (archivo.txt):

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

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras un problema o tienes una mejora, no dudes en abrir un *issue* o enviar un *pull request*.
