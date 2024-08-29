grammar Calculadora;

expr
    : expr op=('*'|'/') expr
    | expr op=('+'|'-') expr
    | '(' expr ')'
    | ABS '(' expr ')'
    | NUMERO
    ;

NUMERO: [0-9]+('.'[0-9]+)?;
MUL: '*';
DIV: '/';
ADD: '+';
SUB: '-';
ABS: 'abs';
WS: [ \t\r\n]+ -> skip;
