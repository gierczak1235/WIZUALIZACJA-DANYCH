import random
def cos(ile,*cos):
    wynik=0
    for x in range(ile):
        g=random.randrange(1,ile)
        wynik+=g
    print(wynik)
    print(wynik/ile)
cos(6,1,20)