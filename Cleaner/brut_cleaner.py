# brut_cleaner.py
# Ce script nettoie les données brutes et supprime toutes les lignes avec des valeurs manquantes
import pandas as pd


def clean_data(input_file, output_file):
    # Charger les données
    data = pd.read_csv(input_file)

    # Supprimer toutes les lignes avec des valeurs manquantes
    data = data.dropna()

    # Sauvegarder les données nettoyées
    data.to_csv(output_file, index=False)