print("------------------------------------")
print("| Vérification Chaine de caractère |")
print("------------------------------------")



essai = 10
for i in range(10):
    list1 = input("Saississez une chaine de caractère quelconque : ")
    list2 = input("Saississez une seconde chaine de caractère quelconque : ")
    if list1 == list2:
        print("Les chaines de caractère sont identiques !")
        break
    else:
        print("Les chaines de caractère ne sont pas identiques !")
        print("Réessayer !")