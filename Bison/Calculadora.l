%{
#include "Calculadora.tab.h"
%}

%%

[0-9]+  { yylval = atoi(yytext); return NUMBER; }
"+"     { return ADD; }
"-"     { return SUB; }
"*"     { return MUL; }
"/"     { return DIV; }
"ABS"   { return ABS; }
"("     { return LPAREN; }
")"     { return RPAREN; }
"\n"    { return EOL; }
[ \t]   { /* Ignorar espacios en blanco */ }
[a-zA-Z]+ { return ERROR; } // Detectar letras y manejar como error
.       { printf("Carácter desconocido: %c\n", *yytext); }

%%
int yywrap() { return 1; }
