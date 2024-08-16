%{
/* Código C que se incluirá en el archivo generado por flex */
#include <stdio.h>

/* Variables globales para contar líneas, palabras y caracteres */
int num_lineas = 0;
int num_palabras = 0;
int num_caracteres = 0;
%}

%%

\n          { num_lineas++; num_caracteres++; }  /* Contar líneas y caracteres para saltos de línea */
[ \t]+      { num_caracteres += yyleng; }  /* Contar caracteres para espacios en blanco y tabulaciones */
[a-zA-Z0-9]+ { num_palabras++; num_caracteres += yyleng; }  /* Contar palabras y caracteres para palabras */
.           { num_caracteres++; }  /* Contar cualquier otro carácter */

%%

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *file = fopen(argv[1], "r");
        if (!file) {
            perror("No se puede abrir el archivo");
            return 1;
        }
        yyin = file;
    }

    yylex();  /* Llama al analizador léxico generado por flex */

    /* Imprime los resultados */
    printf("Número de líneas: %d\n", num_lineas);
    printf("Número de palabras: %d\n", num_palabras);
    printf("Número de caracteres: %d\n", num_caracteres);

    if (yyin != stdin) {
        fclose(yyin);
    }

    return 0;
}

int yywrap() {
    return 1;
}
