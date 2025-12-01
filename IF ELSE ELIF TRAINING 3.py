
print("-----------------------")
print("| Inverse d'un nombre |")
print("-----------------------")
try:
    demand = float(input("Donnez un nombre décimal : "))
except ValueError:
    print("Entrée invalide")
    exit()
try:
    inverse = 1 / demand
except ZeroDivisionError:
    print("Divison impossible par 0")
    exit()
if inverse:
    print(f"L'inverse du nombre {demand} est {inverse}.")

    