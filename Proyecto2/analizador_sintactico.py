# Diccionario que almacena los conjuntos de primeros para cada no terminal.
# El conjunto "primeros" de un no terminal representa los tokens con los que 
# puede comenzar una producción de dicho no terminal.
primeros = {
    'Programa': {'print', 'for', 'if'},
    'Instruccion': {'print', 'for', 'if'},
    'Expresion': {'id', 'tk_entero', 'tk_cadena'},
    'Expresion\'': {'+', 'ε'},
    'Termino': {'id', 'tk_entero', 'tk_cadena'},
    'Rango': {'range'},
    'Bloque': {'print', 'for', 'if', 'ε'}
}

# Diccionario que almacena los conjuntos de siguientes para cada no terminal.
# El conjunto "siguientes" de un no terminal contiene los tokens que pueden
# aparecer después de una producción del no terminal.
siguientes = {
    'Programa': {'$', 'print', 'for', 'if'},
    'Instruccion': {'$', 'print', 'for', 'if'},
    'Expresion': {')', ':'},
    'Expresion\'': {')', ':'},
    'Termino': {'+', ')'},
    'Rango': {':'},
    'Bloque': {'$', 'print', 'for', 'if'}
}

# Conjunto de palabras reservadas que no pueden ser utilizadas como identificadores.
palabras_reservadas = {'for', 'if', 'print', 'range'}

class AnalizadorSintactico:
    def __init__(self, tokens):
        # Lista de tokens a analizar
        self.tokens = tokens
        # Índice del token actual en la lista de tokens
        self.indice = 0
        # Variable para almacenar el mensaje de error sintáctico, si se produce alguno
        self.error = None
        # Conjunto de variables definidas hasta el momento
        self.variables_definidas = set()
        # Nivel actual de indentación en el código
        self.nivel_indentacion = 0
        # Nivel de indentación esperado para bloques de código
        self.esperado_indentacion = 0

    def token_actual(self):
        # Retorna el token actual o None si se alcanzó el final de la lista de tokens
        return self.tokens[self.indice] if self.indice < len(self.tokens) else None

    def avanzar(self):
        # Incrementa el índice para avanzar al siguiente token
        self.indice += 1

    def error_sintactico(self, esperado):
        # Genera un mensaje de error si el token actual no coincide con el esperado
        actual = self.token_actual()
        linea, col, lexema = (actual[1], actual[2], actual[0]) if actual else ("EOF", "EOF", "EOF")
        self.error = f'<{linea},{col}> Error sintactico: se encontró: "{lexema}"; se esperaba: {", ".join(f"{e}" for e in esperado)}'

    def error_indentacion(self):
        # Genera un mensaje de error si el nivel de indentación es incorrecto
        actual = self.token_actual()
        linea, col = actual[1], actual[2]
        self.error = f'<{linea},{col}> Error de indentación: se esperaba un nivel de indentación de {self.esperado_indentacion}, pero se encontró {self.nivel_indentacion}'

    def coincidir(self, tipo):
        # Verifica si el token actual coincide con el tipo esperado y avanza si es así
        actual = self.token_actual()
        if actual and actual[0] == tipo:
            self.avanzar()
            return True
        return False

    def Programa(self):
        # Producción inicial que analiza el programa completo
        while self.token_actual() and self.token_actual()[0] in primeros['Instruccion']:
            self.Instruccion()
            if self.error:
                return  # Termina si hay un error
        if self.token_actual() is None:
            return  # Fin del análisis

    def Instruccion(self):
        # Analiza una instrucción específica según el token actual
        actual = self.token_actual()
        if self.coincidir('print'):
            # Verifica la sintaxis de la instrucción print
            if self.coincidir('tk_par_izq'):
                self.Expresion()
                if not self.error:
                    if self.coincidir('tk_par_der'):
                        # Permite ';' opcional al final
                        self.coincidir('tk_punto_coma')
                    else:
                        self.error_sintactico([')'])
            else:
                self.error_sintactico(['('])
        
        elif self.coincidir('for'):
            # Verifica la sintaxis de la instrucción for
            if self.coincidir('id'):
                id_token = self.tokens[self.indice - 1]
                if id_token[0] in palabras_reservadas:
                    self.error_sintactico(['identificador no reservado'])
                    return

                if self.coincidir('in'):
                    self.Rango()
                    if not self.error:
                        if self.coincidir('tk_dos_puntos'):
                            self.esperado_indentacion += 4
                            self.Bloque()
                            self.esperado_indentacion -= 4
                        else:
                            self.error_sintactico([':'])
                else:
                    self.error_sintactico(['in'])
            else:
                self.error_sintactico(['id'])

        elif self.coincidir('if'):
            # Verifica la sintaxis de la instrucción if
            self.Expresion()
            if not self.error:
                if self.coincidir('tk_dos_puntos'):
                    self.esperado_indentacion += 4
                    self.Bloque()
                    self.esperado_indentacion -= 4
                else:
                    self.error_sintactico([':'])
        else:
            self.error_sintactico(['print', 'for', 'if'])

    def Expresion(self):
        # Analiza una expresión
        self.Termino()
        if not self.error:
            self.Expresion_()

    def Expresion_(self):
        # Maneja expresiones adicionales (recursión)
        if self.coincidir('tk_suma'):
            self.Termino()
            if not self.error:
                self.Expresion_()

    def Termino(self):
        # Verifica términos en la expresión
        actual = self.token_actual()
        if actual and actual[0] in ['id', 'tk_entero', 'tk_cadena']:
            if self.coincidir('id'):
                if actual[0] in palabras_reservadas:
                    self.error_sintactico(['identificador no reservado'])
                elif actual[0] not in self.variables_definidas:
                    self.error_sintactico(['id definida'])
                return
            elif self.coincidir('tk_entero') or self.coincidir('tk_cadena'):
                return  # Aceptar enteros y cadenas
        self.error_sintactico(['id', 'tk_entero', 'tk_cadena'])

    def Rango(self):
        # Analiza la sintaxis de la función range
        if self.coincidir('range'):
            if self.coincidir('tk_par_izq'):
                if self.coincidir('tk_entero'):
                    if self.coincidir('tk_coma'):
                        if not self.coincidir('tk_entero'):
                            self.error_sintactico(['entero'])
                        elif self.coincidir('tk_coma'):
                            if not self.coincidir('tk_entero'):
                                self.error_sintactico(['entero'])
                    if not self.coincidir('tk_par_der'):
                        self.error_sintactico([')'])
                else:
                    self.error_sintactico([':'])
            else:
                self.error_sintactico(['('])
        else:
            self.error_sintactico(['range'])

    def Bloque(self):
        # Analiza un bloque de instrucciones con verificación de indentación
        while self.token_actual() and self.token_actual()[0] in primeros['Instruccion']:
            actual = self.token_actual()
            if actual[0] == 'tk_indentacion':
                self.nivel_indentacion = len(actual[1])

                if self.nivel_indentacion != self.esperado_indentacion:
                    self.error_indentacion()
                    return
            
            self.Instruccion()
            if self.error:
                return

    def analizar(self):
        # Inicia el análisis sintáctico del programa
        self.Programa()
        if not self.error:
            return "El analisis sintactico ha finalizado exitosamente."
        return self.error

