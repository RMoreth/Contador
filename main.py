from time import sleep

contador = int(input("informe um número inteiro: "))
while contador >= 0:
    print(contador)
    contador -= 1
    sleep(0.2)
print('fim')
