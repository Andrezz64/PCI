try:
    num = int(input('Digite seu numero: '))
except:
    print("Não foi possivel calcular, verifique se digitou um numero válido")

parOrImpar = num%2
if parOrImpar == 0:
    print("É par")
else:
    print("É ímpar")