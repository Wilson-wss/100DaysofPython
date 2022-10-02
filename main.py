import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

participantes = {}

while True:
    print(logo)
    nome = input("Qual é seu nome? >>  ")
    lance = int(input("Qual é o seu lance? >> R$ "))
    participantes[nome] = lance
    os.system("cls")
    prox_participante = input("Tem mais participante? S ou N >> ")
    if prox_participante == "S":
        continue
    else:
        break

maior_lance = 0
for lances in participantes:
    x = participantes[lances]

    if x > maior_lance:
        maior_lance = x
        vencedor = lances
print(f"O arrematante é {vencedor}, com o lance de {x}")
