from sklearn.linear_model import LogisticRegression
import random


X = [[0], [1], [2], [3], [4], [5], [6], [7], [8]]

y = [0, 0, 0, 0, 0, 1, 1, 1, 1]



model = LogisticRegression()
model.fit(X, y)


def decision_ia(heures):
    proba_reussite = model.predict_proba([[heures]])[0][1]

    
    tirage = random.random()

    if tirage <= proba_reussite:
        return f"✅ Réussite ({proba_reussite*100:.1f}%)"
    else:
        return f"❌ Échec ({(1 - proba_reussite)*100:.1f}%)"


nombre_tests = 99999
i = 0

while i < nombre_tests:
    heures = int(input("Donne un nombre d'heures : "))
    print(f"{heures} heures → {decision_ia(heures)}")
    i += 1
print(p)
