%{
#include <stdio.h>
%}

%%

cat           printf("gato ");
dog           printf("perro ");
book          printf("libro ");
apple         printf("manzana ");
school        printf("escuela ");
house         printf("casa ");
car           printf("coche ");
water         printf("agua ");
computer      printf("computadora ");
food          printf("comida ");
moon          printf("luna ");
sea           printf("mar ");
fire          printf("fuego ");
star          printf("estrella ");
farm          printf("granja ");

[0-9]+        printf("TOKEN NO RECONOCIDO ");   /* Números */


.|\n          ECHO;        /* Cualquier otro caracter se imprime tal cual */

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

    if (yyin != stdin) {
        fclose(yyin);
    }

    return 0;
}

int yywrap() {
    return 1;
}
