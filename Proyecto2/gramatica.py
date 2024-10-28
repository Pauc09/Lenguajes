class Programa:
    def __init__(self):
        self.instrucciones = []

    def agregar_instruccion(self, instruccion):
        self.instrucciones.append(instruccion)

    def analizar(self):
        while self.instrucciones:
            instruccion = self.instrucciones.pop(0)
            instruccion.analizar()


class Instruccion:
    def __init__(self, expresion, tiene_punto_y_coma=True):
        self.expresion = expresion
        self.tiene_punto_y_coma = tiene_punto_y_coma

    def analizar(self):
        # Verificar que la instrucción sea un print y que la expresión sea válida
        if isinstance(self.expresion, Expresion):
            print("Instrucción válida:", self.expresion)
        else:
            raise SyntaxError("Error en la instrucción")


class Expresion:
    def __init__(self, termino, expresion_siguiente=None):
        self.termino = termino
        self.expresion_siguiente = expresion_siguiente

    def __str__(self):
        if self.expresion_siguiente:
            return f"{self.termino} + {self.expresion_siguiente}"
        return str(self.termino)


class Termino:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return str(self.valor)


# Ejemplo de uso
# Crear términos
termino1 = Termino("tk_entero")
termino2 = Termino("id")

# Crear expresiones
expresion1 = Expresion(termino1)
expresion2 = Expresion(termino2, expresion1)

# Crear instrucciones
instruccion1 = Instruccion(expresion1)
instruccion2 = Instruccion(expresion2, tiene_punto_y_coma=False)

# Crear un programa y agregar instrucciones
programa = Programa()
programa.agregar_instruccion(instruccion1)
programa.agregar_instruccion(instruccion2)

# Analizar el programa
programa.analizar()
