# -- Import des librairies -- #
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules


def apriori_model(fraud_file_path):

    # -- Lecture du fichier csv  -- #
    fraud_data = pd.read_csv(fraud_file_path)

    # -- Convertir les colonnes en valeurs booléennes si nécessaire -- #
    fraud_data['step'] = fraud_data['step'].astype(bool)
    fraud_data['type'] = fraud_data['type'].astype(bool)
    fraud_data['amount'] = fraud_data['amount'].astype(bool)
    fraud_data['nameOrig'] = fraud_data['nameOrig'].astype(bool)
    fraud_data['oldbalanceOrg'] = fraud_data['oldbalanceOrg'].astype(bool)
    fraud_data['newbalanceOrig'] = fraud_data['newbalanceOrig'].astype(bool)
    fraud_data['nameDest'] = fraud_data['nameDest'].astype(bool)
    fraud_data['oldbalanceDest'] = fraud_data['oldbalanceDest'].astype(bool)
    fraud_data['newbalanceDest'] = fraud_data['newbalanceDest'].astype(bool)

    # -- Définition des features et de la target -- #
    fraud_features = ['step', 'type', 'amount', 'nameOrig', 'oldbalanceOrg', 'newbalanceOrig', 'nameDest', 'oldbalanceDest', 'newbalanceDest']
    X = fraud_data[fraud_features]

    print("Prédictions en cours...")

    # -- Création des ensembles fréquents avec l'algorithme Apriori -- #
    frequent_itemsets = apriori(X, use_colnames=True)

    # -- Règles d'association -- #
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

    # -- Affichage des résultats -- #
    # -- Enregistrement du DataFrame dans un fichier CSV -- #
    rules.to_csv("Results/apriori_results.csv", index=False)
    print("Voici les prédictions :")
    print(rules)
    print("\nLes prédictions ont été sauvegardées dans le dossier Results et le fichier apriori_results.csv")


if __name__ == '__main__':
    apriori_model("../Cleaned_Data/Fraud_imputecleaned.csv")