primeros = {
    'Programa': {'print'},
    'Instruccion': {'print'},
    'Expresion': {'id', 'tk_entero'},
    'Expresion\'': {'+', 'ε'},
    'Termino': {'id', 'tk_entero'}
}

siguientes = {
    'Programa': {'$', 'print'},
    'Instruccion': {'$', 'print'},
    'Expresion': {')'},
    'Expresion\'': {')'},
    'Termino': {'+', ')'}
}
