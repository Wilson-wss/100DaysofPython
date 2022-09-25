 #Password Generator Project
import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao gerador de senha do Python!")
nr_letras= int(input("Quantas letras você gostaria na sua senha?\n")) 
nr_simbolos = int(input(f"Quantos símbolos?\n"))
nr_numeros = int(input(f"Quantos números?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
senha = []
for letra in range(1, nr_letras+1):
   x = random.choice(letras)
   senha.append(x)
                  

for numero in range(1, nr_numeros+1):
  y = random.choice(numeros)   
  senha.append(y) 

for simbolo in range(1, nr_simbolos+1):
  z = random.choice(simbolos)
  senha.append(z)
  
random.shuffle(senha)
senhastr = ' '
senha_final = senhastr.join(senha)

print(senha_final)



  
  
  



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P