from random import randint

test= []
for i in range(100):
    rando  = randint(1,1000)
    test.append(rando)
    #print(test)
maxlist = max(test)
print(maxlist)
