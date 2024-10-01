//(), *, /, -, +
%{
#include <stdio.h>
#include <stdlib.h>

int yylex();  // Declaración de yylex
void yyerror(const char *s);  // Declaración de yyerror
%}

%token <dval> NUMBER
%token ADD SUB MUL DIV EOL OP CP
%union {
    double dval;
}

%type <dval> exp factor term

%left ADD SUB
%left MUL DIV
%left '(' ')'

%% 

calclist: 
    /* empty */
    | calclist exp EOL { printf("= %g\n", $2); }
    ;

exp: 
    factor
    | exp ADD factor { $$ = $1 + $3; }
    | exp SUB factor { $$ = $1 - $3; }
    ;

factor: 
    term
    | factor MUL term { $$ = $1 * $3; }
    | factor DIV term { 
        if ($3 == 0) {
            yyerror("división por cero");
            $$ = 0;
        } else {
            $$ = $1 / $3; 
        }
    }
    ;

term: 
    NUMBER
    | OP exp CP { $$ = $2; }
    ;

%% 

int main() {
    printf("> ");
    yyparse();
    return 0;
}

void yyerror(const char *s) {
    fprintf(stderr, "error: %s\n", s);
}

