try:
    num = int(input('Digite seu numero: '))
except:
    print("Não foi possivel calcular, verifique se digitou um numero válido")

calc = num//9

if calc == 0:
    print("é divisivel")
else:
    print("Não é")