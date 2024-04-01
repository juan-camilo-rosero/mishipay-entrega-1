import time
import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Cola:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertar(self, valor):
        new_node = Nodo(valor)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def imprimir(self):
        actual = self.head
        while actual:
            print(actual.valor, end=" ")
            actual = actual.next
            
    def obteneruno(self):
        a = self.head
        self.head = self.head.next
        return a

    def borrar(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head is None:
                self.tail = None


# Función para generar una lista de 100,000 datos aleatorios
def generar_datos_aleatorios(n):
    return [random.randint(0, 1000) for _ in range(n)]

# Función para probar el código con una lista de datos aleatorios
def probar_con_datos_aleatorios(datos):
    inicio = time.time()
    cola = Cola()
    for dato in datos:
        cola.insertar(dato)
    fin_insercion = time.time()
    
    # cola.imprimir()  # Comentar esta línea si no deseas imprimir los datos
    print("\nTiempo de inserción:", fin_insercion - inicio)
    
    while cola.head:
        cola.borrar()
    fin_borrado = time.time()
    print("Tiempo de borrado:", fin_borrado - fin_insercion)

# Generar 100,000 datos aleatorios
# datos_aleatorios = generar_datos_aleatorios(20000000)

# Probar el código con los datos aleatorios
# probar_con_datos_aleatorios(datos_aleatorios)