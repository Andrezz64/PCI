from random import randint
print(30*"-")
print("Bem vindo a jogo da adivinhação")
print(30*"-")
print('')
num = randint(1,100)
controle = 0
for i in range(10):
    controle += 1
    num_enter = int(input('Digite um numeroa:'))
    if num_enter > num:
        print('Muito alto\n')
    elif num_enter == num:
        print(f"Parabens vc acertou na {controle} tentativa")
        
    elif num_enter < num:
        print("muito baixo \n")
