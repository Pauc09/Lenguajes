#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Estructura para representar una transición del DFA
typedef struct {
    char estado_actual[10];   // Estado actual
    char simbolo;             // Símbolo de entrada
    char estado_siguiente[10];// Estado siguiente
} Transicion;

// Estructura para representar el DFA completo
typedef struct {
    char estados[10][10];            // Conjunto de estados
    int num_estados;                 // Número de estados
    char alfabeto[10];               // Conjunto de símbolos del alfabeto
    int num_simbolos;                // Número de símbolos del alfabeto
    char estado_inicial[10];         // Estado inicial
    char estados_aceptacion[10][10]; // Conjunto de estados de aceptación
    int num_estados_aceptacion;      // Número de estados de aceptación
    Transicion transiciones[100];    // Conjunto de transiciones
    int num_transiciones;            // Número de transiciones
} DFA;

// Función para leer el archivo de configuración y configurar el DFA
void leer_configuracion(const char *nombre_archivo, DFA *dfa) {
    FILE *archivo = fopen(nombre_archivo, "r");
    if (!archivo) {
        perror("Error al abrir el archivo");
        exit(EXIT_FAILURE);
    }

    char buffer[100];

    // Leer la primera línea: Conjunto de estados
    fgets(buffer, sizeof(buffer), archivo);
    buffer[strcspn(buffer, "\n")] = 0;
    dfa->num_estados = 0;
    char *token = strtok(buffer, ",");
    while (token) {
        strcpy(dfa->estados[dfa->num_estados], token);
        token = strtok(NULL, ",");
        dfa->num_estados++;
    }

    // Leer la segunda línea: Alfabeto
    fgets(buffer, sizeof(buffer), archivo);
    buffer[strcspn(buffer, "\n")] = 0;
    strcpy(dfa->alfabeto, buffer);
    dfa->num_simbolos = strlen(dfa->alfabeto);

    // Leer la tercera línea: Estado inicial
    fgets(buffer, sizeof(buffer), archivo);
    buffer[strcspn(buffer, "\n")] = 0;
    strcpy(dfa->estado_inicial, buffer);

    // Leer la cuarta línea: Conjunto de estados de aceptación
    fgets(buffer, sizeof(buffer), archivo);
    buffer[strcspn(buffer, "\n")] = 0;
    dfa->num_estados_aceptacion = 0;
    token = strtok(buffer, ",");
    while (token) {
        strcpy(dfa->estados_aceptacion[dfa->num_estados_aceptacion], token);
        token = strtok(NULL, ",");
        dfa->num_estados_aceptacion++;
    }

    // Leer las siguientes líneas: Transiciones
    dfa->num_transiciones = 0;
    while (fgets(buffer, sizeof(buffer), archivo)) {
        buffer[strcspn(buffer, "\n")] = 0;
        sscanf(buffer, "%[^,],%c,%s", dfa->transiciones[dfa->num_transiciones].estado_actual,
                                      &dfa->transiciones[dfa->num_transiciones].simbolo,
                                      dfa->transiciones[dfa->num_transiciones].estado_siguiente);
        dfa->num_transiciones++;
    }

    fclose(archivo);
}

// Función de transición: Dado un estado actual y un símbolo, devuelve el estado siguiente
char* obtener_estado_siguiente(DFA *dfa, const char *estado_actual, char simbolo) {
    // Recorrer todas las transiciones para encontrar una coincidencia
    for (int i = 0; i < dfa->num_transiciones; i++) {
        if (strcmp(dfa->transiciones[i].estado_actual, estado_actual) == 0 && dfa->transiciones[i].simbolo == simbolo) {
            return dfa->transiciones[i].estado_siguiente;
        }
    }
    return NULL; // Si no se encuentra una transición válida, devolver NULL
}

// Función principal
int main() {
    DFA dfa;
    char nombre_archivo[100];
    char cadena_entrada[100];
    char continuar[10];

    // Leer el nombre del archivo de configuración
    printf("Ingrese el nombre del archivo de configuracion: ");
    scanf("%s", nombre_archivo);

    // Leer la configuración del DFA desde el archivo
    leer_configuracion(nombre_archivo, &dfa);

    // Ciclo para seguir probando cadenas
    do {
        // Solicitar la cadena de entrada al usuario
        printf("Ingrese la cadena de entrada: ");
        scanf("%s", cadena_entrada);

        // Inicializar el estado actual como el estado inicial
        char estado_actual[10];
        strcpy(estado_actual, dfa.estado_inicial);

        // Procesar la cadena de entrada carácter por carácter
        int rechazada = 0;
        for (int i = 0; i < strlen(cadena_entrada); i++) {
            char simbolo = cadena_entrada[i];
            char *estado_siguiente = obtener_estado_siguiente(&dfa, estado_actual, simbolo);
            if (estado_siguiente == NULL) {
                // Si no hay una transición válida, la cadena es rechazada
                rechazada = 1;
                break;
            }
            // Actualizar el estado actual al estado siguiente
            strcpy(estado_actual, estado_siguiente);
        }

        // Verificar si la cadena fue rechazada
        if (rechazada) {
            printf("Resultado: La cadena fue RECHAZADA.\n");
        } else {
            // Verificar si el estado final es uno de los estados de aceptación
            int aceptada = 0;
            for (int i = 0; i < dfa.num_estados_aceptacion; i++) {
                if (strcmp(estado_actual, dfa.estados_aceptacion[i]) == 0) {
                    // Si el estado final es de aceptación, la cadena es aceptada
                    aceptada = 1;
                    printf("Resultado: La cadena fue ACEPTADA.\n");
                    break;
                }
            }
            if (!aceptada) {
                printf("Resultado: La cadena fue RECHAZADA.\n");
            }
        }

        // Preguntar al usuario si quiere continuar probando cadenas
        printf("Desea probar otra cadena? (si/no): ");
        scanf("%s", continuar);
    } while (strcmp(continuar, "si") == 0);

    return 0;
}
