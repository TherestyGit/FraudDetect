# -- Import des librairies -- #
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import LabelEncoder

def hierarchical_clustering(fraud_file_path):

    # -- Lecture du fichier csv  -- #
    fraud_data = pd.read_csv(fraud_file_path)

    # -- Encodage des données pour faciliter le calcul -- #
    label_encoder = LabelEncoder()
    fraud_data['type'] = label_encoder.fit_transform(fraud_data['type'])
    fraud_data['nameOrig'] = label_encoder.fit_transform(fraud_data['nameOrig'])
    fraud_data['nameDest'] = label_encoder.fit_transform(fraud_data['nameDest'])

    # -- Définition des features et de la target -- #
    fraud_features = ['step', 'type', 'amount', 'nameOrig', 'oldbalanceOrg', 'newbalanceOrig', 'nameDest', 'oldbalanceDest', 'newbalanceDest']
    X = fraud_data[fraud_features]

    print("Prédictions en cours...")

    # -- Création du modèle -- #
    X_train, X_test = train_test_split(X, test_size=0.01, random_state=1)
    fraud_model = AgglomerativeClustering(n_clusters=3)

    # -- Entrainement du modèle -- #
    fraud_model.fit(X_train)

    # -- Labels des clusters -- #
    labels= fraud_model.labels_


    # -- Affichage des résultats -- #

    # Création du DataFrame avec les prédictions
    fraud_data['Cluster'] = labels

    # -- Enregistrement du DataFrame dans un fichier CSV -- #
    fraud_data.to_csv("Results/hierarchical_clustering_results.csv", index=False)
    print("Voici les prédictions :")
    print(fraud_data)
    print("\nLes prédictions ont été sauvegardées dans le dossier Results et le fichier hierarchical_clustering_results.csv")