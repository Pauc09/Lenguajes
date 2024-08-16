%{
# include <stdio.h>
%}

/* Expresiones regulares para números y operadores */
DIGITO      [0-9]
LETRA       [a-zA-Z]
NUMBER      {DIGITO}+(\.{DIGITO}*)?([eE][-+]?{DIGITO}+)?
OPERATOR    [+\-*/=]
PARENTHESIS [\(\)]

%%

{NUMBER}      { printf("Número: %s\n", yytext); }
{OPERATOR}    { printf("Operador: %s\n", yytext); }
{PARENTHESIS} { printf("Paréntesis: %s\n", yytext); }
{LETRA}+      { printf("Identificador: %s\n", yytext); }

[ \t\n]+      ; /* Ignorar espacios, tabs y nuevas líneas */
.             { printf("Caracter desconocido: %s\n", yytext); }

%%

int main(void) {
    printf("Introduce una expresión:\n");
    yylex(); /* Llama al lexer para procesar la entrada */
    return 0;
}

int yywrap() {
    return 1;
}
