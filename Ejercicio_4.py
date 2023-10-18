# Encabezado y nombre del programa.
print ("\n+---------------------------------------------------+")
print ("|  Codificación de la frase en base a dos palabras  |")
print ("+---------------------------------------------------+")

# Con la impresion en pantalla indicamos las condiciones del ingreso de los
# datos.
print ("\nCondiciones del funcionamiento:\n")
print ("Ingresar 2 palabras del mismo largo,")
print ("\ndonde no coincidan dos letras iguales en la misma posición.\n")

# Creacion de variable que almacenaran las palabras 1 y 2 ingresadas por el usuario.
palabra_1 = str(input ("\nIngrese primera palabra:\n"))
palabra_2 = str(input ("\nIngrese segunda palabra:\n"))

# Creación de la variable que almacenara la frase a codificar.
frase_a_codificar = str(input ("\nIngresa la frase a codificar:\n"))

# Creación de la variable que almacenara la frase codificada.
frase_codificada = ""

# Creación de la variable que nos servirá como un contador en ciclo while:
num_car_palabra = 0

# Iterar una accion tantas veces cuanto tendremos caracteres en la cadena de la variable frase_a_codificar.
for caracter in frase_a_codificar:

    # Mientras se cumple la condicion que haga la accion
    while num_car_palabra < len(palabra_2):

        # 1) para el funcionamiento revisar README.md
        if caracter == palabra_2[num_car_palabra]:
            frase_codificada += palabra_1[num_car_palabra]
            break # Función para interrupción del ciclo.
        # 2) para el funcionamiento revisar README.md
        else:
            num_car_palabra += 1
        
        # 3) para el funcionamiento revisar README.md
        if num_car_palabra == len(palabra_2):
            frase_codificada += caracter
            break # Función para interrupción del ciclo.
    # Instrucción para reanudar el contador a 0, para proximo ciclo a ejecutar.
    num_car_palabra = 0
# Se imprimira por pantalla el mensaje con la frase codificada.
print (f'\nLa frase codificada es: "{frase_codificada}"\n')