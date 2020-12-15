import random
import time

jugarDeNuevo = True

def mostrarIntroducción():

  print('Estás en una tierra llena de dragones. Frente a tí')
  print('hay dos cuevas. En una de ellas, el dragón es generoso y')
  print('amigable y compartirá su tesoro contigo. El otro dragón')
  print('es codicioso y está hambriento, y te devorará inmediatamente.')
  print()

def elegirCueva():
  cueva = ''

  while cueva != '1' and cueva != '2':  
    cueva = input('¿A qué cueva quieres entrar? (1 ó 2)')
  return cueva

def explorarCueva(cuevaElegida):
  print('Te aproximas a la cueva...')
  time.sleep(2)
  print('Es oscura y espeluznante...')
  time.sleep(2)
  print('¡Un gran dragon aparece súbitamente frente a tí! Abre sus fauces y...')
  print()
  time.sleep(2)
  cuevaAmigable = random.randint(1, 2)
  if cuevaElegida == str(cuevaAmigable):
    print('¡Te regala su tesoro!')
  else:
    print('¡Te engulle de un bocado!')
    

while jugarDeNuevo:
  mostrarIntroducción()
  númeroDeCueva = elegirCueva()
  explorarCueva(númeroDeCueva)
  
  otroJuego = input('¿Quieres jugar de nuevo? (sí o no)')
  if otroJuego== 'sí' or otroJuego == 's':
    jugarDeNuevo = True
  else:
    jugarDeNuevo = False
