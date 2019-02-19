# comentario oneline

"""
Comentario de 
varias lineas
"""

a = "hola"

# Arrays

b = ["hola","adios"]
b[1]
b[2]

# Agregamos elementos

b + ["quetal"]

b[3]

# Diccionarios

c = {"nombre":"daniel"}
c["nombre"]

# Sets. Solo muestran uno de cada elemento repetido

d = {1,2,3,3,3,3,4,5,5,5}

# Condicionales

if 1 == 1:
  print("verdadero")
  
if 0 == 1:
  print("falso")
  
# recorrer una lista

vengadores=["thor","ironman","hulk"]
for personaje in vengadores:
  print(personaje)

# Con rangos

for i in range(0,10):
  print(i)

# Whiles

x=10
while x > 0:
  print(x)
  x-=1
  
# Bloques try-catch

try
  print(vengadores[3]
Except IndexError:
  print("No existe el elemento")
  
# Funciones

def bondia():
  print("Bon dia tot lo dia")
  
# Llamamos a la función con bondia()

# Crear clases
# Método init es el constructor de la clase

Class Persona:
  def __init__(self):
    print("Soy una persona")
    
# Para crear objetos a partir de una clase

peter_parker = Persona()

# A partir de una clase se puede crear otra que la incluya

Class Superheroe(Persona):
  def __init__(self):
    super().__init__()
    print("Tengo superpoderes")

# Crear objetos

spiderman = Superheroe()





