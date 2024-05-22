from time import sleep
import os
# Usuario informa um numero
contador = int(input("informe um número inteiro: "))
os.system('cls')

# conta a partir do numero informado ate 0
while contador >= 0:
    print(f"contagem regressiva: {contador}...")
    contador -= 1
    sleep(1)
    os.system('cls')
print('BOOM')
