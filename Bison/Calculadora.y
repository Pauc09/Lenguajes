%{
#include <stdio.h>
#include <stdlib.h>

// Declarar la función yylex generada por Flex
int yylex(void);
// Declarar la función yyerror para manejar errores
void yyerror(const char *s);
%}

/* declare tokens */
%token NUMBER
%token ADD SUB MUL DIV ABS
%token EOL
%token LPAREN
%token RPAREN
%token ERROR // Token para manejar errores de sintaxis

%%

calclist:
  /* nothing */
  | calclist exp EOL {
    printf("= %d\n", $2);
    printf("Ingrese una expresión: ");  // Preguntar de nuevo después de mostrar el resultado
  }
  | calclist error EOL {  // Corregido para manejar el error dentro de calclist
    yyerror("Expresión incompleta");
    printf("Ingrese una expresión: ");  // Volver a preguntar tras un error
    yyerrok; // Recuperar tras un error
  }
;

exp:
  term
  | exp ADD term { $$ = $1 + $3; }
  | exp SUB term { $$ = $1 - $3; }
;

term:
  factor
  | term MUL factor { $$ = $1 * $3; }
  | term DIV factor {
    if ($3 == 0) {
      yyerror("división por cero");
      $$ = 0;
    } else {
      $$ = $1 / $3;
    }
  }
;

factor:
  NUMBER
  | SUB factor { $$ = -$2; } // Manejar números negativos
  | ABS factor { $$ = $2 >= 0 ? $2 : -$2; }
  | LPAREN exp RPAREN { $$ = $2; }
;

%%

/* Función de error */
void yyerror(const char *s) {
  fprintf(stderr, "Error: %s\n", s);
}

int main(void) {
  while (1) {
    printf("Ingrese una expresión: ");
    yyparse();
  }
  return 0;
}
