# impute_cleaner.py
# Ce script nettoie les données brutes et  remplace les valeurs manquantes par la moyenne

# -- IMPORT DES LIBRAIRIES -- #
import pandas as pd
from sklearn.impute import SimpleImputer

# -- FONCTION DE NETTOYAGE DES DONNEES -- #
def clean_data(input_file, output_file):
    # Charger les données
    data = pd.read_csv(input_file)

    # Identifier les colonnes numériques
    numeric_features = data.select_dtypes(include=['int64', 'float64']).columns

    # Appliquer SimpleImputer sur chaque colonne individuellement
    for index, row in data.iterrows():
        if row.isnull().any():
            imputer = SimpleImputer(strategy='mean')
            data.loc[index, numeric_features] = imputer.fit_transform(row[numeric_features].values.reshape(1, -1))

    # Sauvegarder les données imputées
    data.to_csv(output_file, index=False)


# Ceci sert pour les test d'utilisation du script seul
if __name__ == "__main__":
    # Spécifier le chemin du fichier d'entrée et de sortie
    input_file_path = '../Fraud.csv'
    output_file_path = '../Cleaned_Data/Fraud_imputecleaned.csv'

    # Appeler la fonction de nettoyage des données
    clean_data(input_file_path, output_file_path)