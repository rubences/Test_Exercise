# Literal a

def teclaLetra(letra):
   letra = letra.upper()
   letras = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
   numeros = [2,3,4,5,6,7,8,9]
   tamaño = len(letras)
   for i in range(tamaño):
       if (letra in letras[i]):
           return numeros[i]
   return -1

# Literal b

empresa = input("Ingrese el nombre de una empresa: ")
numTelefonico = "1800-"
digitos = ""

for letra in empresa:
   num = teclaLetra(letra)
   digitos = digitos  + str(num)

#Necesito únicamente los 6 primeros digitos
numTelefonico = numTelefonico + digitos[0:6]
print(numTelefonico)


























































