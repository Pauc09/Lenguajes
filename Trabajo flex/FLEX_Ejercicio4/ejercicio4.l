%{
#include <stdio.h>
%}

/* Definición de tokens */
NUMBER      [0-9]+
ADD         \+
SUB         \-
MUL         \*
DIV         \/    
ABS         abs
EOL         \n

%% 

{NUMBER}    { printf("TOKEN: NUMBER, VALUE: %s\n", yytext); }
{ADD}       { printf("TOKEN: ADD, VALUE: %s\n", yytext); }
{SUB}       { printf("TOKEN: SUB, VALUE: %s\n", yytext); }
{MUL}       { printf("TOKEN: MUL, VALUE: %s\n", yytext); }
{DIV}       { printf("TOKEN: DIV, VALUE: %s\n", yytext); }
{ABS}       { printf("TOKEN: ABS, VALUE: %s\n", yytext); }
{EOL}       { printf("TOKEN: EOL\n"); }
.           { printf("TOKEN NO RECONOCIDO: %s\n", yytext); }

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

