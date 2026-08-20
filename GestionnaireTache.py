tasks = []
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
        nouvelle_tache = {
            "nom": task,
            "termine": False
        }
        tasks.append(nouvelle_tache)
        print("Une tâche à été ajoutée avec succès !")

    elif choix == 2:
        for i, task in enumerate(tasks, start=0):
            if task["termine"]:
                print(f"{i}. [✓] {task['nom']}")
            else:
                print(f"{i}. [ ] {task['nom']}")
        if tasks == []:
            print("La liste est vide")

    elif choix == 3:
        demande_suppression = int(input("Qu'est-ce que vous voulez supprimer ? Entrez le numero de rang exacte que vous voulez supprimez : "))
        delete = tasks.pop(demande_suppression)

    elif choix == 4:
        demande_modification = int(input("Quel tâche voulez vous marquée comme terminée ? Entrez le numero de rang exacte que vous voulez supprimez : "))
        tasks[demande_modification]["termine"] = True

    elif choix == 5:
        break

    else:
        print("Type Incorrect ! Veulliez entrer sois A sois B sois C")