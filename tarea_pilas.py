class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None

    def push(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def pop(self):
        if self.cima == None:
            return None
        dato = self.cima.valor
        self.cima = self.cima.siguiente
        return dato

    def esta_vacia(self):
        if self.cima == None:
            return True
        else:
            return False

    def mostrar(self):
        actual = self.cima
        while actual != None:
            print(actual.valor)
            actual = actual.siguiente

    def contar(self):
        contador = 0
        actual = self.cima
        while actual != None:
            contador = contador + 1
            actual = actual.siguiente
        return contador


# Programa principal

pila_principal = Pila()

# Leer archivo
archivo = open("datos.csv", "r")
lineas = archivo.readlines()
archivo.close()

# Quitar encabezado
for i in range(1, len(lineas)):
    linea = lineas[i].strip()
    partes = linea.split(",")
    nombre = partes[0]
    artista = partes[1]
    asiste = partes[2]

    if asiste == "True":
        asiste = True
    else:
        asiste = False

    pila_principal.push((nombre, artista, asiste))


# Crear las 3 pilas
pila_bts_si = Pila()
pila_bad_no = Pila()
pila_taylor_si = Pila()

pila_aux = Pila()

# Recorrer pila principal
while pila_principal.esta_vacia() == False:

    registro = pila_principal.pop()
    nombre = registro[0]
    artista = registro[1]
    asiste = registro[2]

    if artista == "BTS" and asiste == True:
        pila_bts_si.push(registro)

    if artista == "Bad Bunny" and asiste == False:
        pila_bad_no.push(registro)

    if artista == "Taylor Swift" and asiste == True:
        pila_taylor_si.push(registro)

    pila_aux.push(registro)


# Regresar datos a la pila principal
while pila_aux.esta_vacia() == False:
    pila_principal.push(pila_aux.pop())


# Resultados

print("----- BTS que SI asisten -----")
pila_bts_si.mostrar()
print("Cima:", pila_bts_si.cima.valor)
print("Cantidad:", pila_bts_si.contar())

print("\n----- Bad Bunny que NO asisten -----")
pila_bad_no.mostrar()
print("Cima:", pila_bad_no.cima.valor)
print("Cantidad:", pila_bad_no.contar())

print("\n----- Taylor Swift que SI asisten -----")
pila_taylor_si.mostrar()
print("Cima:", pila_taylor_si.cima.valor)
print("Cantidad:", pila_taylor_si.contar())