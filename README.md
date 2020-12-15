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
