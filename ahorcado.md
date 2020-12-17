# 1. Ahorcado base

Importamos la libreria os para poder utilizar la función de limpiar pantalla:

```python
import os # Para borrar la pantalla
```
Lista de las letras

Tenemos que guardar la lista de las letras que hemos dicho, tanto correctas como incorrectas. Para ello, utilizaremos dos listas, de momento vacías:

```python
letraIncorrecta = []
letraCorrecta =  []
```

Guardaremos en una variable la palabra que tenemos que adivinar, y en otra una copia de la misma palabra, pero vacía (con _ en lugar de letras), que iremos modificando, cambiando los _ por letras, a medida que se vayan acertando:

```python
palabraSecreta = list("navidad") # Palabra original, la guardamos 
longitudPalabra = len(palabraSecreta)
palabraResuelta = ['_'] * longitudPalabra # Creamos una lista para resolver con todo "_"  
``` 
Una vez declarado esto, entraremos en un bucle de pedir letras, hasta que el juego termine. De momento, el bucle será infinito, aunque después deberemos modificar esto:

```python
while True:
``` 
Podemos pintar un poco de texto informando del juego, que podremos personalizar:

```python
print ("") # pinta una línea en blanco
print ('A H O R C A D O (Ramon Llull Edition)')
print ("--------------------------------------\n\n") Cada # \n añade un salto de línea
```
Antes de pedir letras, mostramos las incorrectas, para evitar que se repitan:

```python
print ('Letras incorrectas: ', end = '')
for letra in letraIncorrecta:
  print (letra, end = '')  # end = '' evita que se haga un salto de línea despues del print
  print ("") 
```
Ahora mostraremos la palabra tal como está, con las letras que hayan sido acertadas en su posición, y las que quedan con un _:

```python
  print ("--------------------------------------\n")
  print("PALABRA:          ")
    
    for i in range(longitudPalabra): # Remplaza los espacios en blanco por la letra bien escrita
        if palabraSecreta[i] in letraCorrecta:
            palabraResuelta[i] = palabraSecreta[i] 

    # Mostramos la palabra como está ahora

    for letra in palabraResuelta: # Mostrará la palabra secreta con espacios entre letras
        print (letra+" ", end = '')
    print ("\n")

```

Por último, pedimos al usuario que introduzca una letra:    

```python
print ('Adivina una letra:')
letra = input()
```

Si la letra está en la palabra, la meteremos en la lista **letraCorrecta**. Sino, en la lista **letraIncorrecta**:

```python
if letra in palabraSecreta:        
  letraCorrecta.append(letra)
else:
  letraIncorrecta.append(letra)
```

# 2. Mejoras ahorcado

## 2.1. Permitir elegir entre varias palabras

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
    posicion = random.randint(0, len(palabras) - 1)
    palabraSecreta = palabras[posicion]
```

En un lugar del programa, deberemos llamar a la función **buscarPalabraAleat** y asignarle el valor devuelto a la variable que tiene la palabra con la que vamos a jugar.

## 2.2. Filtrar el tipo de letra permitido

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

# 2.3 Ganar y perder

Podemos crear una variable booleana finJuego que sea True si ha terminado el juego, y falso si no es así.

El juego puede terminar bajo dos condiciones:

## Partida ganada: que hayamos resuelto la palabra antes de agotar nuestras oportunidades.

Para ello podemos comprobar que no quedan huecos de letras vacías en la palabra resuelta:

```python
if "_" not in palabraResuelta
```
## Partida perdida: que hayamos fallado un número suficiente de veces

Podemos ayudarnos de una variable que contenga el máximo número de vidas o "errores" permitidos. Si hemos fallado tantas letras como vidas,el juego tiene que terminar.

```python
vidas = 6
if len(letraIncorrecta) == vidas:
```

El bucle principal se tiene que cambiar:

```python
juegoTerminado = False
while not juegoTerminado:

  if ganado:
    juegoTerminado = True
    mostrarFraseGanado
  if perdido:
    juegoTerminado = True
    mostrarFrasePerdido (y la palabra)
```    

# 2.4 Jugar otra vez

```python
def jugarOtra():
  print('¿Quieres jugar otra partida? (Sí o no))
  return input().lower().startswith('s')
```
 
# 2.5 Categorías de palabras

Otra mejora del programa consiste en cambiar la lista de palabras por un diccionario que permita agrupar por categorías. En este caso, **listaPalabras** es un diccionario que contiene claves (keys) y valores (values). Cada categoría será una clave (ej:formas), y su valor una lista de elementos (rectangulo,circulo,cuadrado, ...).

- colores
  - rojo
  - verde
- formas
  - rectangulo
  - circulo
  - cuadrado
  - ...

```python
import random

listaPalabras = { 'colores': 'rojo verde azul naranja'.split(),
             'formas': 'rectangulo circulo cuadrado'.split(),
             'animales': 'perro oso gato'.split()
           }

categoria = random.choice(list(listaPalabras.keys()))

numPalabra = random.randint(0, len(listaPalabras[categoria]) - 1)
palabraElegida = listaPalabras[categoria][numPalabra]

print([categoria,palabraElegida])
```

# 2.6. Clasificación

Podríamos hacer el juego más competitivo creando una clasificación. Para ello, tendríamos que pensar en algún sistema de puntuación para poder comparar los resultados de las diferentes partidas.

Creamos un diccionario ```tablaClasificacion```, que contendrá el nombre del jugador y su puntuación.

tablaClasificacion = {  'Dani': 4000,
                        'Pepe: 2000,
                        'Manolo: 1000,
                        }

## Añadir puntuación

Tendríamos que pedir el nombre al jugador en una variable ```nombre``` al comenzar la partida y guardarlo en alguna variable, como ```jugador```.
Al final de la partida, calculamos la puntuación y la guardamos en el diccionario:

```python
tablaClasificacion[nombre] = puntuacion
```

## Mostrar clasificación

La función mostrarClasificación podría ser:

```python
def mostrarClasificacion(tablaClasificacion):
    print("--------------------------------")
    print("            CLASIFICACION       ")
    print("--------------------------------")
 
    jugadores = list(tablaClasificacion.keys())
    for nombreJugador in jugadores:
        print("   ", nombreJugador, "    ", tablaClasificacion[nombreJugador])  
    print("--------------------------------\n")
```
