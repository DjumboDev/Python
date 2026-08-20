import sqlite3

connexion = sqlite3.connect("tasks.db")
curseur = connexion.cursor()
curseur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    termine INTEGER
)
""")
connexion.commit()

while True:
    print("\n--- MENU ---")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Supprimer une tâche")
    print("4. Marquer une tâche comme terminée")
    print("5. Quitter")

    try:
        choix = int(input("Choix : "))
    except ValueError:
        print("Erreur : veuillez entrer un nombre !")
        continue
    

    if choix == 1:
        task = input("Nouvelle tâche : ")

        curseur.execute(
            "INSERT INTO tasks (nom, termine) VALUES (?, ?)",
            (task, 0)
        )
        connexion.commit()

        print("Une tâche à été ajoutée avec succès !")


    elif choix == 2:

        curseur.execute("SELECT * FROM tasks")
        resultats = curseur.fetchall()

        if not resultats:
            print("La liste est vide !")

        else:
            for task in resultats:

                identifiant = task[0]
                nom = task[1]
                termine = task[2]

                if termine:
                    print(f"{identifiant}. [✓] {nom}")
                else:
                    print(f"{identifiant}. [ ] {nom}")

    elif choix == 3:

        try:
            demande_suppression = int(
                input("Quel numéro de tâche voulez-vous supprimer ? ")
            )

            curseur.execute(
                "DELETE FROM tasks WHERE id = ?",
                (demande_suppression,)
            )

            connexion.commit()

            if curseur.rowcount == 0:
                print("Cette tâche n'existe pas !")
            else:
                print("Tâche supprimée avec succès !")

        except ValueError:
            print("Erreur : veuillez entrer un nombre !")



    elif choix == 4:

        try:
            print("1. Marquée comme terminée")
            print("2. Décochez")

            demande_modif = int(
                input("Quel option voulez-vous optée ?")
                )
        
            if demande_modif == 1:

                demande_modification = int(
                    input("Quel numéro de tâche voulez-vous terminer ? ")
                )


                curseur.execute(
                    "UPDATE tasks SET termine = 1 WHERE id = ?",
                    (demande_modification,)
                )
            
                connexion.commit()

            elif demande_modif == 2:

                demande_modification = int(
                    input("Quel numéro de tâche voulez-vous terminer ?")
                )
                curseur.execute(
                    "UPDATE tasks SET termine = 0 WHERE id = ?",
                    (demande_modification,)
                )

                connexion.commit()

            if curseur.rowcount == 0:
                print("Cette tâche n'existe pas !")
            elif termine == 1:
                print("Cette tâche est déjà terminée !")
            else:
                print("Tâche marquée comme terminée !")

        except ValueError:
            print("Erreur : veuillez entrer un nombre !")

    elif choix == 5:
        connexion.close()
        print("Au revoir")
        break

    else:
        print("Incorrect ! Veulliez entrer les options indiqué au menu.")