"""Sujet

Dans ce projet, tu vas devoir créer un programme en ligne de commande qui permet de manipuler une liste de courses.

Déroulé du script

Le programme doit permettre de réaliser 5 actions :

Ajouter un élément à la liste de courses

Retirer un élément de la liste de courses

Afficher les éléments de la liste de courses

Vider la liste de courses

Quitter le programme"""


def menum():
    print("Gestionnaire de liste")
    print("----------------------------menu options----------------------------")
    print("\t\t1. Ajouter un élément à la liste de courses")
    print("\t\t2. Retirer un élément de la liste de courses")
    print("\t\t3. Afficher les éléments de la liste de courses")
    print("\t\t4. Vider la liste de courses")
    print("\t\t5. Quitter le programme")
    print("---------------------------------------------------------------------")

liste_course = []

def main():
    while True:
        menum()
        choix = int(input('Please select...'))
        if choix in [1,2,3,4,5]:
            if choix == 5:
                repons = input("Etes-vous sûr de vouloir quitter l'application o/n")
                if repons =='o' or repons == 'O':
                    print('Merci, et à bientôt !')
                    break
                else:
                    continue
            elif choix == 1:
                    while True:
                        liste_c = input('Entrer un nouvel élément dans la liste')
                        liste_course.append(liste_c)

                        print(f"L'élément {liste_c} a été ajouté avec succès.") 
                        #print(liste_course)

                        answer = input("Voulez-vous continuer l'ajout ? o/n")
                        if answer =='o' or answer =='O':
                            continue
                        else:
                            break  
            elif choix == 2:
                    print(liste_course)
                    element_del=input("Entrer l'élément à rétirer de la liste!")
                    if element_del !='':
                        if element_del in liste_course:

                            liste_course.remove(element_del)
                            print(f"L'élément {element_del} a été retiré de la liste avec succès.")
                        else:
                            print(f"L'élément {element_del} n'existe pas dans la liste.")
            elif choix == 3:
                    print(f"Il y a {len(liste_course)} éléments dans la liste : {liste_course}")
            elif choix == 4:
                    #print(liste_course)
                    if len(liste_course) != 0:
                        liste_course.clear()
                        print(f"La liste a été vidé succès : {liste_course}.")
                    else:
                        print(f"La liste ne contient aucun élément.")
                            
    
if __name__ == '__main__':
    main()