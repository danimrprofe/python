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
