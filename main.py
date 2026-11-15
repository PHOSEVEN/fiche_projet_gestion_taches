def saisir_N():
    n = int(input("donner le nombre les tâches"))
    while not(n > 0):
        n = int(input("donner le nombre les tâches"))
    return n


def saisir_les_taches(n):
    ch = ""
    for i in range(n):
        ch += f"la NOTE N°{i} est : " + input(f"donner la tâche N°{i} ") + "\n"
    return ch


def service(ch):
    print("pour N ° 0 : NON")
    print("pour N ° 1 : afficher ")
    print("pour N ° 2 : rechercher ")
    print("pour N ° 3 : modifier")
    print("pour N ° 4 : supprimer")
    print("pour N ° 5 :  marquer")
    nb = 0
    while nb <= 5:
        num = int(input("taper votre commande."))
        if num == 0:
            return False
        elif num == 1:
            afficher(ch)
        elif num == 2:
            rechercher(ch)
        elif num == 3:
            modifier(ch)
        elif num == 4:
            supprimer(ch)
        else:
            marquer(ch)
        nb += 1


def afficher(ch):
    print(ch)


def rechercher(ch):
    note = int(input("donner le N ° de la note "))
    list = ch.split("\n")
    if list[note - 1] != "":
        print(f"la Note N ° {note} existe")
    else:
        print(f"la Note N ° {note} n'existe pas")


def modifier(ch):
    note = int(input("donner le N ° de la note "))
    nv_note = input("écris la nouvelle note tu veux modifier")
    list = ch.split("\n")
    list[note - 1] = f"la NOTE N°{note-1} est : " + nv_note
    ch = "\n".join(list)
    print("modification avec succès")
    print(ch)
    return ch


def supprimer(ch):
    note = int(input("donner le N ° de la note "))
    list = ch.split("\n")
    list[note - 1] = ""
    ch = "\n".join(list)
    print("suppression avec succès")
    print(ch)
    return ch


def marquer(ch):
    note = int(input("donner le N ° de la note "))
    list = ch.split("\n")
    list[note - 1] = list[note - 1] + "    *****épingler*****"
    ch = "\n".join(list)
    print(ch)
    return ch


n = saisir_N()
ch = saisir_les_taches(n)
service(ch)
