%{
#include "EXP1.tab.h"  // Asegúrate de que este sea el nombre correcto
#include <stdlib.h>
void yyerror(const char *s);  // Declaración de yyerror
%}

%% 

[0-9]+         { yylval.dval = atof(yytext); return NUMBER; }
"+"            { return ADD; }
"-"            { return SUB; }
"*"            { return MUL; }
"/"            { return DIV; }
\n             { return EOL; }
"("            { return OP; }
")"            { return CP; }
[ \t]+         { /* Ignorar espacios y tabulaciones */ }
.              { yyerror("Carácter no reconocido"); }

%%

// Función para indicar el fin de entrada
int yywrap() {
    return 1;
}
