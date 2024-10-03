# Función para leer el archivo de texto y cargar las producciones en un diccionario
def leer_gramatica():
    archivo = 'gramatica.txt'  # Archivo fijo para la gramática
    producciones = {}
    with open(archivo, 'r') as file:
        for linea in file:
            linea = linea.strip()
            if '->' in linea:
                no_terminal, produccion = linea.split('->')
                no_terminal = no_terminal.strip()
                produccion = produccion.strip()
                # Dividimos las producciones por el símbolo '|'
                if no_terminal not in producciones:
                    producciones[no_terminal] = []
                producciones[no_terminal].extend([p.strip() for p in produccion.split('|')])
    return producciones

# Función para verificar si un símbolo es terminal
def es_terminal(simbolo):
    return simbolo.islower() and simbolo != 'ε'

# Cálculo del conjunto de PRIMEROS
def calcular_primeros(producciones):
    primeros = {}
    calculando = set()

    # Inicializamos el conjunto de PRIMEROS para cada no terminal vacío
    for no_terminal in producciones:
        primeros[no_terminal] = set()

    # Función recursiva para obtener PRIMEROS de un símbolo dado
    def primeros_de(alpha):
        if es_terminal(alpha):
            return {alpha}
        elif alpha == 'ε':
            return {'ε'}
        if alpha in calculando:
            return set()  # Evita la recursión infinita devolviendo un conjunto vacío temporalmente

        if primeros[alpha]:
            return primeros[alpha]  # Si ya está calculado, devolver el resultado

        calculando.add(alpha)  # Marcar que estamos calculando PRIMEROS de este símbolo
        conjunto_primeros = set()

        for produccion in producciones[alpha]:
            for simbolo in produccion.split():
                simbolo_primeros = primeros_de(simbolo)
                conjunto_primeros.update(simbolo_primeros - {'ε'})
                if 'ε' not in simbolo_primeros:
                    break
            else:
                conjunto_primeros.add('ε')
        calculando.remove(alpha)  # Termina el cálculo de PRIMEROS de este símbolo
        primeros[alpha] = conjunto_primeros
        return conjunto_primeros

    for no_terminal in producciones:
        primeros[no_terminal] = primeros_de(no_terminal)

    return primeros

# Cálculo del conjunto de SIGUIENTES
def calcular_siguientes(producciones, primeros):
    siguientes = {}
    calculando_siguientes = set()

    # Inicializamos SIGUIENTES de todos los no terminales como conjuntos vacíos
    for no_terminal in producciones:
        siguientes[no_terminal] = set()

    # El símbolo inicial siempre tiene el símbolo '$' en su conjunto de SIGUIENTES
    simbolo_inicial = list(producciones.keys())[0]
    siguientes[simbolo_inicial].add('$')

    # Función recursiva para obtener SIGUIENTES de un símbolo dado
    def siguientes_de(no_terminal):
        if no_terminal in calculando_siguientes:
            return siguientes[no_terminal]  # Evita la recursión infinita

        calculando_siguientes.add(no_terminal)  # Marcar como en cálculo
        for producciones_no_terminal in producciones:
            for produccion in producciones[producciones_no_terminal]:
                simbolos = produccion.split()
                for i, simbolo in enumerate(simbolos):
                    if simbolo == no_terminal:
                        # Caso 1: Si hay algo después del símbolo
                        if i + 1 < len(simbolos):
                            siguiente_simbolo = simbolos[i + 1]
                            # Si es terminal, agregarlo directamente y detener la propagación
                            if es_terminal(siguiente_simbolo):
                                siguientes[no_terminal].add(siguiente_simbolo)
                                break  # No seguir propagando después de un terminal
                            else:
                                # Agregar PRIMEROS del siguiente símbolo (excepto ε)
                                primeros_siguiente_simbolo = primeros[siguiente_simbolo]
                                siguientes[no_terminal].update(primeros_siguiente_simbolo - {'ε'})
                                # Si el PRIMEROS del siguiente contiene ε, agregar SIGUIENTES del no terminal
                                if 'ε' in primeros_siguiente_simbolo:
                                    siguientes[no_terminal].update(siguientes_de(producciones_no_terminal))
                        # Caso 2: Si es el último símbolo, agregar SIGUIENTES del no terminal
                        elif i + 1 == len(simbolos):
                            siguientes[no_terminal].update(siguientes_de(producciones_no_terminal))
        calculando_siguientes.remove(no_terminal)
        return siguientes[no_terminal]

    # Calculamos SIGUIENTES para cada no terminal
    for no_terminal in producciones:
        siguientes[no_terminal] = siguientes_de(no_terminal)

    return siguientes

# Función para ordenar correctamente SIGUIENTES
def ordenar_siguientes(siguientes_conjunto):
    # Ordenamos alfabéticamente y garantizamos que $ esté al final
    elementos = sorted([s for s in siguientes_conjunto if s != '$'])
    if '$' in siguientes_conjunto:
        elementos.append('$')  # Colocamos el símbolo $ al final
    return elementos

# Función principal
def main():
    # Leer archivo de gramática
    producciones = leer_gramatica()
    
    # Calcular PRIMEROS
    primeros = calcular_primeros(producciones)
    
    # Calcular SIGUIENTES
    siguientes = calcular_siguientes(producciones, primeros)
    
    # Mostrar solo los conjuntos de SIGUIENTES en orden
    print("\nSIGUIENTES:")
    for no_terminal, conjunto_siguientes in siguientes.items():
        elementos_ordenados = ordenar_siguientes(conjunto_siguientes)
        elementos = ", ".join(elementos_ordenados)
        print(f"SIGUIENTES({no_terminal}) = {{ {elementos} }}")

# Ejecutar el programa
if __name__  == "__main__":
    main()
