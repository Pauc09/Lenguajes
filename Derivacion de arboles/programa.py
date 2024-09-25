import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

# Función para leer las reglas gramaticales del archivo
def leer_gramatica(archivo):
    reglas = {}
    with open(archivo, 'r') as f:
        for linea in f:
            linea = linea.strip()
            if '->' in linea:
                parte_izquierda, parte_derecha = linea.split('->')
                parte_izquierda = parte_izquierda.strip()
                parte_derecha = [token.strip() for token in parte_derecha.split('|')]
                
                if parte_izquierda in reglas:
                    reglas[parte_izquierda].extend(parte_derecha)
                else:
                    reglas[parte_izquierda] = parte_derecha
    return reglas

# Función para generar el árbol basado en las reglas y la cadena ingresada
def generar_arbol(reglas, nodo_inicio, tokens):
    arbol = nx.DiGraph()  # Grafo dirigido para el árbol
    derivacion = []  # Guardar la derivación para validar la entrada
    token_idx = 0  # Índice para recorrer los tokens ingresados por el usuario
    
    def expandir(nodo, profundidad):
        nonlocal token_idx
        if nodo in reglas and token_idx < len(tokens):  # Verificamos si hay más tokens por procesar
            # Verificamos las posibles producciones de la gramática para el nodo
            for produccion in reglas[nodo]:
                simbolos = produccion.split()
                sub_arbol_valido = True
                for simbolo in simbolos:
                    if token_idx >= len(tokens):
                        break  # Salimos si ya no quedan más tokens que procesar
                    
                    # Agregar el símbolo al árbol y verificar si es un no terminal o un terminal
                    if simbolo == tokens[token_idx]:
                        arbol.add_node(simbolo, layer=profundidad)
                        arbol.add_edge(nodo, simbolo)
                        derivacion.append(simbolo)
                        token_idx += 1
                    elif simbolo in reglas:
                        arbol.add_node(simbolo, layer=profundidad)
                        arbol.add_edge(nodo, simbolo)
                        derivacion.append(simbolo)
                        expandir(simbolo, profundidad + 1)
                    else:
                        sub_arbol_valido = False
                        break
                
                # Si generamos un subárbol válido que cubre la parte de la cadena, dejamos de expandir más
                if sub_arbol_valido and token_idx == len(tokens):
                    break

    arbol.add_node(nodo_inicio, layer=0)
    derivacion.append(nodo_inicio)
    expandir(nodo_inicio, 1)
    return arbol, derivacion

# Función para visualizar el árbol
def mostrar_arbol(arbol):
    pos = graphviz_layout(arbol, prog='dot')  # 'dot' tiende a ser bueno para árboles
    plt.figure(figsize=(8, 6))
    nx.draw(arbol, pos, with_labels=True, node_color='lightblue', font_size=10, node_size=3000, font_weight='bold')
    plt.title("Árbol de derivación gramatical")
    plt.show()

# Función para validar si la cadena ingresada corresponde a la derivación
def validar_cadena(tokens, derivacion, reglas):
    derivacion_sin_terminales = [token for token in derivacion if token not in reglas]
    return tokens == derivacion_sin_terminales[:len(tokens)]

# Función principal
def main():
    archivo_gramatica = 'grammar.txt'  # Nombre y ruta del archivo de gramática
    reglas = leer_gramatica(archivo_gramatica)
    
    # Definir el nodo de inicio (variable inicial de la gramática)
    nodo_inicio = 'S'  # Esto puede cambiar dependiendo de tu gramática
    
    # Solicitar al usuario la cadena a analizar
    entrada_usuario = input("Ingrese una cadena para analizar: ")
    tokens = entrada_usuario.split()  # Dividir la cadena en tokens
    
    # Generar el árbol sintáctico
    arbol, derivacion = generar_arbol(reglas, nodo_inicio, tokens)
    
    # Validar la cadena ingresada
    if validar_cadena(tokens, derivacion, reglas):  # Pasar reglas como argumento
        print("La cadena es válida según la gramática.")
        mostrar_arbol(arbol)
    else:
        print("La cadena no es válida según la gramática.")
        mostrar_arbol(arbol)  # Aún se mostrará el árbol para visualizar la derivación

if __name__ == "__main__":
    main()
