# Ahorcado base

Importamos la libreria os para poder utilizar la función de limpiar pantalla:

 import os # Para borrar la pantalla

# Lista de las letras

letraIncorrecta = []
letraCorrecta =  []

palabraSecreta = list("navidad") # Palabra original, la guardamos 
longitudPalabra = len(palabraSecreta)
palabraResuelta = ['_'] * longitudPalabra # Creamos una lista para resolver con todo "_"  

while True:
    _ = os.system('cls')
    print ("")

    print ('A H O R C A D O (Ramon Llull Edition)')
    print ("--------------------------------------\n\n")
        
    # Mostrar las letras incorrectas

    print ('Letras incorrectas: ', end = '')
    
    for letra in letraIncorrecta:
        print (letra, end = '') 
    print ("") 
    print ("--------------------------------------\n")
    print("PALABRA:          ")
    
    for i in range(longitudPalabra): # Remplaza los espacios en blanco por la letra bien escrita
        if palabraSecreta[i] in letraCorrecta:
            palabraResuelta[i] = palabraSecreta[i] 

    # Mostramos la palabra como está ahora

    for letra in palabraResuelta: # Mostrará la palabra secreta con espacios entre letras
        print (letra+" ", end = '')
    print ("\n")

    print ("--------------------------------------\n")

    # Elegir una letra
    
    print ('Adivina una letra:')
    letra = input()
    
    if letra in palabraSecreta:        
        letraCorrecta.append(letra)
    else:
        letraIncorrecta.append(letra)

# Mejoras ahorcado

# 1. Permitir elegir entre varias palabras

Necesitaremos en primer lugar crear una lista de palabras:

```python
palabras = 'valoracion aprenderpython comida juego python'.split()
```
La función *split()* nos separará las palabras en una lista, mirando los espacios entrer palabras. 

Podemos crear una función que devuelva una palabra al final, de la lista *listaPalabras*. Para ello utilizaremos una función de la librería random, que deberemos importar al principio de nuestro programa.

```python
import random
```

La función *radint* devuelve un número aleatorio del rango que pidamos.
 
```python
def buscarPalabraAleat(listaPalabras):    
    posicion = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[posicion]
```

En un lugar del programa, deberemos llamar a la función **buscarPalabraAleat** y asignarle el valor devuelto a la variable que tiene la palabra con la que vamos a jugar.

# 2. Filtrar el tipo de letra permitido

Cualquier tecla del teclado puede ser utilizada por el usuario a la hora de elegir la letra, por lo que debemos comprobar que solo están permitidas letras del alfabeto. Para ello, mejor crear una función **elijeLetra()**, puesto que la vamos a utilizar cada vez que pidamos al usuario una letra.

```python
def elijeLetra():
   ...
   ...
  return letra
```

El bloque principal consiste en capturar un input (el funcionamiento que ya tenemos):

```python
print ('Adivina una letra:')
letra = input()
```
Podemos forzar que la letra se convierta a minúsculas:

```python
letra = letra.lower()
```

Podemos comprobar que solo se introduce una letra y no dos o más:

```python
if len(letra) != 1:
```

No tendríamos que poder decir una letra que ya se ha dicho antes. En este caso **algunaLetra** es una lista que contiene todas las letras que ya se han dicho antes.

```python
if letra in algunaLetra:
```

Comprobar que la letra está en el alfabeto:

```python
if letra not in 'abcdefghijklmnopqrstuvwxyz':
```


 
