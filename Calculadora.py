import time
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
menu = 0

while menu != 5:
    time.sleep(1)
    menu = int(input('Qual opção operação você quer realizar:\n [1]soma '
                     '\n [2]Multiplicar \n [3]Divisão \n [4]Novos Números \n [5]Sair \n'))
    if menu == 1:
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')
        time.sleep(1)
    elif menu == 2:
       multiplicar =  num1 * num2
       print(f'{num1} X {num2} = {multiplicar}')
       time.sleep(1.5)
    elif menu == 3:
       divisao =  num1 / num2
       print(f'{num1} / {num2} = {divisao}')
       time.sleep(1.5)
    elif menu == 4:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        time.sleep(1)
print('Fim do Programa')