class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Crear un árbol simple
raiz = Nodo("A")
raiz.izquierda = Nodo("B")
raiz.derecha = Nodo("C")
raiz.izquierda.izquierda = Nodo("D")
raiz.izquierda.derecha = Nodo("E")

# Mostrar el árbol
def mostrar_arbol(nodo, nivel=0):
    if nodo:
        print("  " * nivel + str(nodo.valor))
        mostrar_arbol(nodo.izquierda, nivel + 1)
        mostrar_arbol(nodo.derecha, nivel + 1)

print("Árbol Binario:")
mostrar_arbol(raiz)