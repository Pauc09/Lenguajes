primeros = {
    'Programa': {'print'},
    'Instruccion': {'print'},
    'Expresion': {'id', 'tk_entero', 'tk_cadena'},  # Agregado tk_cadena
    'Expresion\'': {'+', 'ε'},
    'Termino': {'id', 'tk_entero', 'tk_cadena'},  # Agregado tk_cadena
}

siguientes = {
    'Programa': {'$', 'print'},
    'Instruccion': {'$', 'print'},
    'Expresion': {')'},
    'Expresion\'': {')'},
    'Termino': {'+', ')'}
}

class AnalizadorSintactico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.indice = 0
        self.error = None
        self.variables_definidas = set()  # Para llevar un registro de variables definidas

    def token_actual(self):
        return self.tokens[self.indice] if self.indice < len(self.tokens) else None

    def avanzar(self):
        self.indice += 1

    def error_sintactico(self, esperado):
        actual = self.token_actual()
        linea, col, lexema = (actual[1], actual[2], actual[0]) if actual else ("EOF", "EOF", "EOF")
        self.error = f'<{linea},{col}> Error sintactico: se encontro: "{lexema}"; se esperaba: {", ".join(f"{e}" for e in esperado)}'

    def coincidir(self, tipo):
        actual = self.token_actual()
        if actual and actual[0] == tipo:
            self.avanzar()
            return True
        return False

    def Programa(self):
        while self.token_actual() and self.token_actual()[0] in primeros['Instruccion']:
            self.Instruccion()
            if self.error:
                return  # Terminar si hay error
        if self.token_actual() is None:
            return  # Fin del análisis

    def Instruccion(self):
        if self.coincidir('print'):
            if self.coincidir('tk_par_izq'):
                self.Expresion()
                if not self.error:
                    if self.coincidir('tk_par_der'):
                        # Permitir instrucción sin ';'
                        self.coincidir('tk_punto_coma')  # Se ignora el error si no hay ';'
                    else:
                        self.error_sintactico([')'])
            else:
                self.error_sintactico(['('])
        else:
            self.error_sintactico(['print'])

    def Expresion(self):
        self.Termino()
        if not self.error:
            self.Expresion_()

    def Expresion_(self):
        if self.coincidir('tk_suma'):
            self.Termino()
            if not self.error:
                self.Expresion_()
        # Si no coincide con '+', entonces es ε (epsilon), no hacer nada y regresar.

    def Termino(self):
        actual = self.token_actual()
        if actual and actual[0] in ['id', 'tk_entero', 'tk_cadena']:
            if self.coincidir('id'):
                if actual[0] not in self.variables_definidas:
                    self.error_sintactico(['id definida'])  # Error si la variable no está definida
                return
            elif self.coincidir('tk_entero') or self.coincidir('tk_cadena'):
                return  # Aceptar enteros y cadenas sin necesidad de verificar
        self.error_sintactico(['id', 'tk_entero', 'tk_cadena'])  # Error si no coincide

    def analizar(self):
        self.Programa()
        if not self.error:
            return "El análisis sintáctico ha finalizado exitosamente."
        return self.error
