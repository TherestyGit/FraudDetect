# -- Import des librairies -- #
import pandas as pd
from sklearn.model_selection import train_test_split
from lightgbm import LGBMRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score

def lightgbm(fraud_file_path):

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

    y = fraud_data.isFraud


    print("Prédictions en cours...")

    # -- Création du modèle -- #
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=1)
    fraud_model = LGBMRegressor(random_state=1)

    # -- Entrainement du modèle -- #
    fraud_model.fit(X_train, y_train)

    # -- Prédiction -- #
    predictions = fraud_model.predict(X_test)

    # -- Évaluation la performance du modèle -- #
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    perf_df = pd.DataFrame({'MSE': [mse], 'R2': [r2]})

    print(f'Mean Squared Error: {mse}')
    print(f'R-squared: {r2}')


    # -- Affichage des résultats -- #
    # Création du DataFrame avec les prédictions
    predictions_df = pd.DataFrame({'Vraies valeurs': y_test, 'Prédictions': predictions})

    # -- Enregistrement du DataFrame dans un fichier CSV -- #
    predictions_df.to_csv("Results/lightgbm_results.csv", index=False)
    perf_df.to_csv("Results/lightgbm_performance.csv", index=False)
    print("Voici les prédictions :")
    print(predictions_df)
    print("\nLes prédictions ont été sauvegardées dans le dossier Results et le fichier lightgbm_results.csv")
    print("Les performances du modèle ont été sauvegardées dans le dossier Results et le fichier lightgbm_performance.csv")