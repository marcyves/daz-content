import os
import tkinter as tk
from tkinter import filedialog, ttk


def lister_categories(chemin):
    dossiers = [nom for nom in os.listdir(chemin) if os.path.isdir(os.path.join(chemin, nom))]
    return dossiers

# Exemple de fonction pour extraire des informations d'un fichier
def extraire_infos_fichier(nom_fichier):
    # Exemple fictif de décomposition d'un nom de fichier
    elements = nom_fichier.split('_')
    
    produit = elements[0] if len(elements) > 0 else "Inconnu"
    categorie = elements[1] if len(elements) > 1 else "Inconnu"
    genre = elements[2] if len(elements) > 2 else "Inconnu"
    personnage = elements[3] if len(elements) > 3 else "Inconnu"
    description = " ".join(elements[4:]) if len(elements) > 4 else "Pas de description"

    return produit, categorie, genre, personnage, description

def parcourir_dossier(categorie):
    # Dossier fixe pour l'exemple (vous pouvez le changer pour `filedialog.askdirectory()` si nécessaire)
    dossier = "/Users/shared/My DAZ 3D Library/" + categorie

    if not dossier:
        return

    # Effacer les lignes existantes dans la table
    for item in table.get_children():
        table.delete(item)

    # Parcourir les fichiers dans le dossier categorie
    extensions = ['.duf']
    for dossier_racine, _, fichiers in os.walk(dossier):
        for fichier in fichiers:
            if any(fichier.lower().endswith(ext) for ext in extensions):
                chemin_complet = os.path.join(dossier_racine, fichier)
                produit, categorie, genre, personnage, description = extraire_infos_fichier(fichier)
                table.insert("", "end", values=(produit, categorie, genre, personnage, description))

repertoire_base = "/Users/shared/My DAZ 3D Library"
categories = lister_categories(repertoire_base)
exclusions = {"Documentation", "Documents", "data", "Runtime", "Templates", "Tools", "DAZ Studio Tutorials", "html", "ReadMe's"}

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("My DAZ 3D Library")

# Créer un cadre pour les boutons
frame_boutons = tk.Frame(fenetre)
frame_boutons.pack(pady=10)

button_count = 0
buttons_per_line = 5

for categorie in categories:
    if categorie not in exclusions:
        bouton_selection = tk.Button(frame_boutons, text=categorie, command=lambda c=categorie: parcourir_dossier(c))
        ligne = button_count // buttons_per_line
        colonne = button_count % buttons_per_line
        bouton_selection.grid(row=ligne, column=colonne, padx=5, pady=5)  # Utiliser grid dans le cadre des boutons
        button_count += 1

# Créer un cadre pour la table
frame_table = tk.Frame(fenetre)
frame_table.pack(pady=10)

# Créer la table avec des colonnes
colonnes = ("Produit", "Catégorie", "Genre", "Personnage", "Description")
table = ttk.Treeview(frame_table, columns=colonnes, show="headings")

# Définir les en-têtes des colonnes
for col in colonnes:
    table.heading(col, text=col)
    table.column(col, width=150)

table.pack(expand=True, fill="both")

# Exécuter l'interface
fenetre.mainloop()
