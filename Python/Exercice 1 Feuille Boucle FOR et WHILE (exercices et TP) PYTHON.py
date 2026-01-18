from random import randint
demande1 = randint(1,10)
demande2 = randint(1,10)

partie = 0
while demande1 != demande2:
    demande1 = randint(1,10)
    demande2 = randint(1,10)
    partie += 1
print(partie)
