i = int(input("digite o numero de pessoas do grupo: "))
lista = []
media = 0
maior = 0
control = 0
for o in range(i):
    control += 1
    idade = int(input(f"digte a idade da {control}° pessoa: "))
    media = 0 + idade
    lista.append(idade)
    if idade >= 18:
        maior+=1

if maior == 0:
    text = "não tiveram maiores de idade "
else:
    text = f"{maior} pessoa(s) maiores de idade" 
idademax = max(lista)
idademin = min(lista)
mediaFinal = media/i
print(f"A maior ideade registrada foi {idademax} anos e a menor {idademin} anos \n a media das idades foi {mediaFinal} e {text}")

