# Hum... ok

# Generateur pour rechercher des utilisateur 
# Nicolas.M

import collections #importation de la bibliotheque collections

fichier_connexion = "/home/nono/python/projet_1/connexion.log"# liste des connexions avec ip nom et heures
fichier_utilisateurs = "/home/nono/python/utilisateurs.txt"# liste des utilisateurs
fichier_warning = "/home/nono/python/projet_1/warning.txt"
fichier_suspect = "/home/nono/python/suspect.txt"
list_user = [] # liste contenant les donnée a traité
names=[] # listes des noms
heures=[] #listes des heures avec minutes
resultats = []
list_suspect = {}
list_ip = []
list_uniq_user = [] #liste des utilisateurs unique
fichier_inter = "/home/nono/python/inter.txt"

# def compteur_lignes(nomfichier):
#     compteur = 0
#     for ligne in open(nomfichier):
#         compteur += 1
#     return compteur

# print(compteur_lignes('wc.py'))


#parcourez le fichier pour trouver 
# la liste de tous les utilisateurs 
# qui se sont connectés, 
# enregistrez cette liste dans 
# un fichier utilisateurs.txt

with open(fichier_connexion, 'r') as f:
    with open("utilisateurs.txt", 'w' ) as e:
        for line in f:
            names=line.split(";") # separations des donnees dans la liste
            # affecte les donnees chercher a une liste
            # ouverture du fichier 
            e.write(names[1]+"\n")  # ecriture des donnees recuperes avec retour chariot

# On soupçonne qu’une personne se connecte
# en dehors des heures d’ouverture des bureaux (8h-19h),
# peut-être depuis un poste distant. 
# Utilisez un script pour retrouver l’identifiant de cette personne,
# et afficher l’ip à la laquelle elle se connectait

with open(fichier_connexion, 'r') as l:
    with open("resultat.txt", 'w') as r:
        for colonnes  in l:
            heure=colonnes.split(" ") # pour separer les heures des autres informations
            resultat=colonnes.split(";") # pour separer les colonnes
            if heure[1] <= str("08:00") or heure[1] >= str("19:00"): # pour determiner les connexions en dehors des heures de bureau  
                for value in resultat :
                    r.write((resultat[0]+" "+resultat[1])+"\n")
                    print(resultat[0]+" "+resultat[1])  # imprimer les resultats 

# Le service de sécurité informatique a fournit une liste d’ip dangereuse :
#  warning.txt. Lisez ce fichier pour construire une liste contenant toutes les ip dangereuses.
#  A l’aide de cette liste, relevez dans le fichier connexion.log tous les utilisateurs qui se sont connectés sur une de ces ip, on produira un fichier suspect.txt 
# #avec une ligne par utilisateur et le nombre de fois qu’il s’est connecté à une ip interdite :  

with open(fichier_warning, "r") as w :
    for wuser in w :
        list_ip.append(wuser.strip())
#permet de creer la la liste des ip dangereuses

with open(fichier_connexion, "r") as g :
    with open(fichier_inter, "w") as inter :# sauvegarde intermediaire des utilisateurs dont l ip est en doublons ou plus
        for muser in g :
            list_user = muser.split(";")# permet de separer les donnees separes par ;
            if list_user[0] in list_ip :# permet de comparer la liste des ip et des utilisateurs
                inter.write(list_user[1] + '\n')
# permet de determiner les utilisateur qui ce sont connecte 
# sur les ip dangereuses

with open(fichier_inter, "r") as h :
    for suser in h :
        suser = suser.strip()
        list_suspect[suser] = list_suspect.get(suser, 0) +1
# permet de creer une liste d'utilisateurs en enlevant les doublons

list_suspect = collections.OrderedDict(sorted(list_suspect.items()))

# permet de compter les connexions de chaque utilisateur par un dictionnaire 
# dont l'ip fait parti des ip dangereuses
# creation d un fichier reunissants les personne connecte sur des ip dangereuses
# et le nombre de connexion

with open(fichier_suspect, "w") as suspects :
    for key, value in list_suspect.items() :
        suspects.write(key + ";" + str(value) + "\n")

    print(suspects.write(key + ";" + str(value)))
