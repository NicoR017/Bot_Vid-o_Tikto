import os

def List_url(video_url):
    
    list_fichier = "list.txt"
    
    if not os.path.exists(list_fichier):
        with open(list_fichier, 'w'):
            pass
    with open(list_fichier,'a') as list:
        list.write(f"{video_url}\n")
        
def recherche_video(nom_fichier, video_rechercher):
    try:
        # Ouvrir le fichier en mode lecture
        with open(nom_fichier, 'r') as fichier:
            # Lire tout le contenu du fichier
            contenu = fichier.read()

        # Divisez le contenu en liens en utilisant l'espace comme séparateur
        liens = contenu.split("\n")

        # Parcourir chaque liens et vérifier s'il correspond au liens recherché
        for lien in liens :
            if lien== video_rechercher:   
                 return False
            else:
                 # Ajouter le liens à l'historique
                List_url(video_rechercher)
                return True
       
        

    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' n'a pas été trouvé.")
        return "", []

def compter_lignes_fichier(nom_fichier):
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        nombre_lignes = sum(1 for ligne in fichier)
    return nombre_lignes