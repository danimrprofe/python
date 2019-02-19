nombre = raw_input("Dime tu nombre: ")
edad = raw_input("Dime tu edad: ")

anyo=2019-int(edad)+100


print ("Tendras 100 anyos en el " + str(anyo))

with open("archivo.txt","w" ) as open_file:
	open_file.write(str(nombre) + " tendra 100 anyos en " + str(anyo))

