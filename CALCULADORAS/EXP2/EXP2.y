//(), +, -, /, *
%{
    #include <stdio.h>
    #include <stdlib.h>
    void yyerror(const char *s); // Declaración de yyerror
    int yylex();                // Declaración de yylex
%}

/* Declaración de los tokens */
%token <dval> NUMBER
%token ADD SUB MUL DIV POW ABS OP CP EOL

%union {
    double dval;
}

%type <dval> exp factor term

%left DIV MUL
%left SUB ADD
%right POW
%left ABS

%% 

calclist: 
    /* empty */ 
    | calclist exp EOL { printf("= %g\n> ", $2); }
    | calclist EOL { printf("> "); } 
    ;

exp: 
    factor
    | exp MUL exp { $$ = $1 * $3; }
    | exp DIV exp { 
        if ($3 == 0) {
            printf("error: division por cero no existe\n");
            $$ = 0;
        } else {
            $$ = $1 / $3; 
        }
    }
    | exp SUB exp { $$ = $1 - $3; }
    | exp ADD exp { $$ = $1 + $3; }
    | exp POW exp {
        double base = $1;
        int exponent = (int) $3;
        double result = 1;
        for (int i = 0; i < exponent; i++) {
            result *= base;
        }
        $$ = result;
    }
    | ABS exp { $$ = $2 >= 0 ? $2 : -$2; }
    | SUB exp { $$ = -$2; }
    ;

factor: 
    term
    | OP exp CP { $$ = $2; }
    ;

term: 
    NUMBER
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
