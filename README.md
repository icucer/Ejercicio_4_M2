# Realizar un programa que codifique la frase entregada por el usuario en base a 2 palabras:
***
### Requerimientos del ejercicio:

1) Pedir al usuario que ingrese dos palabras del mismo largo en las que no coincidan dos letras iguales en la misma posición.
2) También pedir al usuario que ingrese la frase a codificar.
***
## A continuación, dejaré algunos fragmentos del código donde se explica el funcionamiento, ya que los comentarios complican mucho la lectura del código:
***
- 1) Mediante la condicional if, compararemos el carácter de la frase a codificar con el carácter de la palabra número 2 ingresada por el usuario. Si coincide con el carácter en dicha palabra, lo reemplazaremos con el carácter correspondiente de la palabra número 1 y lo guardaremos en la variable frase_codificada.
```
        if caracter == palabra_2[num_car_palabra]:
            frase_codificada += palabra_1[num_car_palabra]
```
***
- 2) En caso contrario, si el carácter que estamos revisando no está presente en la palabra que estamos utilizando para codificar, incrementamos el contador para que pase al siguiente carácter de la palabra.
```
        else:
            num_car_palabra += 1
```
***
- 3) Y, por último, revisamos si el carácter a comparar se ha comparado con todos los caracteres de la palabra número 2 ingresada por el usuario, y si la condición se ha cumplido y hemos llegado al último carácter en la palabra que estamos utilizando para codificar (en otras palabras, si el contador está igual al número de caracteres que contiene la palabra número 2), entonces agregamos el carácter a revisar a la variable frase_codificada.
```
        if num_car_palabra == len(palabra_2):
            frase_codificada += caracter
```