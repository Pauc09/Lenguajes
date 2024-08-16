%{
#include <stdio.h>
#include <string.h>

void classify_number(const char* number);

int yywrap(void) {  // Actualización aquí para que coincida con la declaración esperada
    return 1;
}
%}

%%

[+-]?[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?[ ]*[+-]?[ ]*[0-9]+(\.[0-9]+)?([Xx][0-9]+[eE][+-]?[0-9]+)?[ ]*[iI] { classify_number(yytext); }
[+-]?[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?[ ]*[iI]                                                            { classify_number(yytext); }
[+-]?[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?[ ]*∠[ ]*[+-]?[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?                   { classify_number(yytext); }
[+-]?[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?[ ]*exp\([ ]*[+-]?[iIjJ][ ]*[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?[ ]*\) { classify_number(yytext); }
[+-]?[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?                                                                     { classify_number(yytext); }

\n|\t|\r                                                                                                     { /* Ignorar saltos de línea y tabulaciones, pero no espacios */ }
.                                                                                                            { printf("Entrada no válida: %s\n", yytext); }

%%

void classify_number(const char* number) {
    if (strstr(number, "i") || strstr(number, "I")) {
        if (strstr(number, "+") || strstr(number, "-")) {
            if (strstr(number, "∠") || strstr(number, "exp")) {
                printf("Forma polar reconocida: %s\n", number);
            } else {
                printf("Número complejo: %s\n", number);
            }
        } else {
            printf("Número imaginario: %s\n", number);
        }
    } else if (strstr(number, "∠") || strstr(number, "exp")) {
        printf("Forma polar reconocida: %s\n", number);
    } else {
        printf("Número real: %s\n", number);
    }
}

int main(int argc, char** argv) {
    yylex();
    return 0;
}
