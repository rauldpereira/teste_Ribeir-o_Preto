palavra = str(input("Digite uma palavra que deseja inverter: "))

contador = 0

for caractere in palavra:
    contador +=1

invertida = ""

contador -= 1

while contador >=0:
    invertida += palavra[contador]
    contador -= 1

print(invertida)