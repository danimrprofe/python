import random
import os #erase screen brodeeeeer

palabras = 'hola adios saturno subnautica cyberpunk'.split()
posicion = random.randint(0, len(palabras)-1)
vidas = 7

letraIncorrecta = []
letraCorrecta = []

palabraSecreta = palabras[posicion]
longitudPalabra = len(palabraSecreta)
palabraResuelta = ['_'] * longitudPalabra 

juegoTerminado = False

while not juegoTerminado: 
  _ = os.system('clear') 

  print ('') #decoracion linea vacia
  print ('A H O R C A D O (Editado por MAIRANO)')
  print ('------------------------------------------------\n\n')

  print('Letras Incorrectas: ', end = '\n')

  for letra in letraIncorrecta:
    print(letra, end = '')
    print('')

  print('------------------------------------------------\n')
  print('PALABRA:            ')

  for i in range(longitudPalabra):
    if palabraSecreta[i] in letraCorrecta:
      palabraResuelta[i] = palabraSecreta [i]


  for letra in palabraResuelta: 
    print(letra+" ", end = '')
  print('\n ')

  print('Di una letra. Tienes' , vidas -1, "vidas")
  letra= input()
  letra = letra.lower()

  if letra in palabraSecreta:
    letraCorrecta.append(letra)
  else:
    letraIncorrecta.append(letra)

  if "_" not in palabraResuelta:
    print('Ganaste')
    juegoTerminado = True

  if len(letraIncorrecta) == vidas:
    print('Perdiste, la palabra era', palabraSecreta )
    juegoTerminado = True
