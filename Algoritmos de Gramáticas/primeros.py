# Función para cargar la gramática desde un archivo txt
def cargar_gramatica(archivo):
    producciones = {}
    with open(archivo, 'r') as file:
        for linea in file:
            linea = linea.strip()
            if '->' in linea:
                no_terminal, regla = linea.split('->')
                no_terminal = no_terminal.strip()
                produccion = regla.strip().split()
                
                if no_terminal not in producciones:
                    producciones[no_terminal] = []
                
                producciones[no_terminal].append(produccion)
    return producciones

# Función para calcular el conjunto de PRIMEROS de un no terminal
def calcular_primeros(producciones, no_terminal, cache=None, visitados=None):
    if cache is None:
        cache = {}  # Crear caché local para cada cálculo
    if visitados is None:
        visitados = set()  # Para evitar recursión infinita
    
    if no_terminal in cache:
        return cache[no_terminal]  # Retorna el resultado almacenado
    
    if no_terminal in visitados:  # Detecta la recursión
        return set()  # Evita ciclos
    
    visitados.add(no_terminal)  # Marcar no terminal como visitado
    primeros = set()
    
    if no_terminal not in producciones:  # Si no hay producciones para este no terminal
        return primeros
    
    for produccion in producciones[no_terminal]:
        for simbolo in produccion:  # Iterar por cada símbolo en la producción
            if simbolo.islower():  # Si es un terminal
                primeros.add(simbolo)
                break
            else:  # Si es un no terminal
                primeros_regla = calcular_primeros(producciones, simbolo, cache, visitados)
                primeros.update(primeros_regla - {'ε'})  # Agregar PRIMEROS sin ε
                if 'ε' not in primeros_regla:
                    break  # Si no tiene ε, no seguir con el siguiente símbolo
        else:
            primeros.add('ε')  # Si todos los símbolos de la producción derivan ε
    
    visitados.remove(no_terminal)  # Desmarcar no terminal al final
    cache[no_terminal] = primeros  # Almacenar el resultado en caché
    return primeros

# Cargar la gramática desde el archivo
archivo_gramatica = 'gramatica.txt'
producciones = cargar_gramatica(archivo_gramatica)

# Calcular PRIMEROS
primeros = {nt: calcular_primeros(producciones, nt) for nt in producciones}

# Imprimir los conjuntos de PRIMEROS
print("Conjuntos de PRIMEROS:")
for nt, conjunto in primeros.items():
    print(f"PRIMEROS({nt}) = {sorted(conjunto)}")
