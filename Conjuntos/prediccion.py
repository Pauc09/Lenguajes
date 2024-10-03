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

# Función para calcular el conjunto de PRIMEROS de una cadena o símbolo
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

# Función para calcular el conjunto de SIGUIENTES de un no terminal
def calcular_siguientes(producciones, no_terminal, primeros, cache=None):
    if cache is None:
        cache = {}  # Crear caché local para cada cálculo
    
    if no_terminal in cache:
        return cache[no_terminal]  # Retorna el resultado almacenado
    
    siguientes = set()
    if no_terminal == 'S':  # Suponiendo que 'S' es el símbolo inicial
        siguientes.add('$')  # '$' es el símbolo de fin de entrada
    
    for nt, reglas in producciones.items():
        for regla in reglas:
            if no_terminal in regla:
                pos = regla.index(no_terminal)
                if pos + 1 < len(regla):  # Si hay un símbolo después
                    siguiente = regla[pos + 1]
                    if siguiente.islower():  # Si es un terminal
                        siguientes.add(siguiente)
                    else:  # Si es un no terminal
                        primeros_siguiente = calcular_primeros(producciones, siguiente)
                        siguientes.update(primeros_siguiente - {'ε'})
                if pos + 1 == len(regla) or 'ε' in primeros.get(siguiente, set()):
                    siguientes.update(calcular_siguientes(producciones, nt, primeros, cache))
    
    cache[no_terminal] = siguientes  # Almacenar el resultado en caché
    return siguientes

# Función para calcular el conjunto de predicción
def calcular_prediccion(producciones, primeros, siguientes):
    predicciones = {}
    
    for no_terminal, reglas in producciones.items():
        for regla in reglas:
            prediccion = set()
            
            # Iterar por cada símbolo de la regla
            for simbolo in regla:
                primeros_simbolo = primeros[simbolo] if simbolo in primeros else {simbolo}
                prediccion.update(primeros_simbolo - {'ε'})
                
                # Si el símbolo no contiene ε, no seguimos con los siguientes símbolos
                if 'ε' not in primeros_simbolo:
                    break
            else:
                # Si todos los símbolos de la producción pueden derivar ε, agregar SIGUIENTES
                prediccion.update(siguientes[no_terminal])
            
            # Guardar la predicción para la producción completa
            predicciones[f'{no_terminal} → {" ".join(regla)}'] = list(prediccion)
    
    return predicciones

# Cargar la gramática desde el archivo
archivo_gramatica = 'gramatica.txt'
producciones = cargar_gramatica(archivo_gramatica)

# Calcular PRIMEROS
primeros = {nt: calcular_primeros(producciones, nt) for nt in producciones}

# Calcular SIGUIENTES
siguientes = {nt: calcular_siguientes(producciones, nt, primeros) for nt in producciones}

# Calcular PREDICCIONES
predicciones = calcular_prediccion(producciones, primeros, siguientes)

# Imprimir las predicciones
for produccion, prediccion in predicciones.items():
    print(f'{produccion}: {sorted(prediccion)}')
