import random
import json
import os # Para borrar la pantalla        

listaPalabras = json.load( open( "diccionario.json" ) )
puntos = 0

def eligeCategoria():
  categoria = random.choice(list(listaPalabras.keys()))
  return categoria

def eligePalabra(categoria): 
  numPalabra = random.randint(0, len(listaPalabras[categoria]) - 1)
  return listaPalabras[categoria][numPalabra]
  

def eligeLetra():
  letraCorrecta = False  
  while not letraCorrecta:
    letra = input('Adivina una letra o resuelve (re):') 
    if letra == "re":
      return "re"
    if len(letra) != 1:
      print("Solo se puede una letra a la vez")  
    else:
      if letra not in 'abcdefghijklmnopqrstuvwxyz':
        print("Tiene que ser una letra del alfabeto")  
      else:
        letraCorrecta = True     
  return letra

def resolver(palabraSecreta):
  
  palabraResuelta = input("¿Cual es la palabra?")
  if palabraResuelta == palabraSecreta:
    input("Enhorabuena, has resuelto la palabra <enter>")
    return True    
  else:
    input("Esa no es la palabra secreta")
    return False

def jugarOtra():
  print('¿Quieres jugar otra partida? (Sí o no)')
  return input().lower().startswith('s')

def actualizaPuntos(puntos,puntosNuevos):
  if (puntos + puntosNuevos) <= 0:
    return 0
  else:
    return puntos + puntosNuevos

AHORCADO ="AHORCADO"
juegoNuevo = True
# Lista de las letras

nombreJugador = input("Bienvenido al ahorcado, ¿cómo te llamas?")
input(f"hola {nombreJugador}, vamos a jugar al ahorcado <Pulsa enter>")


while juegoNuevo:

  letraIncorrecta = []
  letraCorrecta = []

  categoria = eligeCategoria()  
  palabraSecreta = eligePalabra(categoria)
  
  longitudPalabra = len(palabraSecreta)

  print ('A H O R C A D O')

  juegoTerminado = False
  
  while not juegoTerminado:
      
      _ = os.system('cls')    
          
      # Mostrar las letras incorrectas

      print(f"Puntos {nombreJugador}: {puntos}\n")

      print ('\nLetras incorrectas: ', end = '')
      for letra in letraIncorrecta:
          print (letra, end = '') 
      print ("")
      
      # Creamos un string con todo "_"  

      espacio = '_' * longitudPalabra
      for i in range(longitudPalabra): # Remplaza los espacios en blanco por la letra bien escrita
          if palabraSecreta[i] in letraCorrecta:
              espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]

      print(f"La categoria es {categoria} ")
      # Mostramos la palabra como está ahora

      for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
          print (letra+" ", end = '')
      print ("")
      
      # Elegir una letra
      
      
      letra = eligeLetra()

      if letra == "re":
        resuelto = resolver(palabraSecreta)
        letrasSobrantes = len(palabraSecreta) - len(letraCorrecta)
        puntosResolver = letrasSobrantes * 20
        if resuelto:
          juegoTerminado = True
          print(f"Has ganado {letrasSobrantes} x 20 puntos =  {puntosResolver}")
          puntos = actualizaPuntos(puntos,puntosResolver)
          break
        else:          
          print(f"Has perdido {letrasSobrantes} x 20 puntos =  {puntosResolver}")
          puntos = actualizaPuntos(puntos,-puntosResolver)
          break
      elif letra in palabraSecreta:
          letraCorrecta.append(letra)
          puntos =actualizaPuntos(puntos,10)
          # Se fija si el jugador ganó
          letrasEncontradas = True
          for i in range(longitudPalabra):
              if palabraSecreta[i] not in letraCorrecta:
                  letrasEncontradas = False
                  break
          if letrasEncontradas:
              print ('¡Muy bien! La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
              juegoTerminado = True
      else:
          puntos = actualizaPuntos(puntos,-15)
          if letra in letraIncorrecta:
            input ('Esta letra ya la habías dicho <pulsa enter>')
          else:
            letraIncorrecta.append(letra)
          # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
          if len(letraIncorrecta) == len(AHORCADO) - 1:            
              print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
              juegoTerminado = True

  juegoNuevo = jugarOtra()
