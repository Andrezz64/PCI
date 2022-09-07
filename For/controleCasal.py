boysum = 0
girlsum = 0
timemid = 0
control  = 0
for i in range(2500):
    control +=1
    boy = int(input("Digite a idade de seu namorado: "))
    girl = int(input("Digite a idade de seua namorada: "))
    time = int(input("Quanto tempo estão juntos ? --> "))
    print(2*"-\n")
    boysum += boy
    girlsum += girl
    if time < 2:
        timemid += 1

boymid = boysum/control
girlmid = girlsum/control

print(f"A média de homems foi de {boymid} e de mulheres {girlmid}\nO numero de casais com menos de dois anos juntos é {timemid}")

