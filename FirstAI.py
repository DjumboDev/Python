from sklearn.linear_model import LogisticRegression

NombreHeureRevision = [[1], [2], [3], [4], [5], [6], [7], [8]]

Resultat = [0, 0, 0, 0, 1, 1, 1, 1]

model = LogisticRegression()
model.fit(NombreHeureRevision, Resultat) # IA apprend à partir des données.
nombre_utilisateurs = 5
i = 0
heures = []
while i < nombre_utilisateurs:
    heures_utilisateurs = int(input("Donnez un nombre d'heure : "))
    heures.append([[heures_utilisateurs]])
    i = i + 1

predictions = model.predict(heures)

for h, p in zip(heures, predictions):
    if p == 1:
        print(f"{h[0]} heures → Réussite probable")
    else:
        print(f"{h[0]} heures → Échec probable")
print(p)