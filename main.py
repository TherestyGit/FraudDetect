# main.py
# Ceci est le menu principal du programme. Il permet à l'utilisateur de choisir le scénario
# de nettoyage des données et le modèle de Machine Learning qu'il souhaite utiliser.

# -- IMPORT DES LIBRAIRIES -- #
import os
import time

# -- MENU PRINCIPAL -- #

print("╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
print("║                                                                                                                ║")
print("║   ________                                   __  _______              __                            __         ║")
print("║   |        \                                 |  \|       \            |  \                          |  \       ║")
print("║   | $$$$$$$$______   ______   __    __   ____| $$| $$$$$$$\  ______  _| $$_     ______    _______  _| $$_      ║")
print("║   | $$__   /      \ |      \ |  \  |  \ /      $$| $$  | $$ /      \|   $$ \   /      \  /       \|   $$ \     ║")
print("║   | $$  \ |  $$$$$$\ \$$$$$$\| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$\\$$$$$$  |  $$$$$$\|  $$$$$$$ \$$$$$$      ║")
print("║   | $$$$$ | $$   \$$/      $$| $$  | $$| $$  | $$| $$  | $$| $$    $$ | $$ __ | $$    $$| $$        | $$ __    ║")
print("║   | $$    | $$     |  $$$$$$$| $$__/ $$| $$__| $$| $$__/ $$| $$$$$$$$ | $$|  \| $$$$$$$$| $$_____   | $$|  \   ║")
print("║   | $$    | $$      \$$    $$ \$$    $$ \$$    $$| $$    $$ \$$     \  \$$  $$ \$$     \ \$$     \   \$$  $$   ║")
print("║    \$$     \$$       \$$$$$$$  \$$$$$$   \$$$$$$$ \$$$$$$$   \$$$$$$$   \$$$$   \$$$$$$$  \$$$$$$$    \$$$$    ║")
print("║                                                                                                                ║")
print("║                                                                          Fraud Prediction by Theresty          ║")
print("╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
print("Bienvenue dans le programme de prediction de fraude !")
print("Que souhaitez-vous faire ?")
print("1 : Lancer les prédictions")
print("2 : Quitter le programme")
choix = input("Votre choix : ")

if choix == "1":

    # -- MENU DE SELECTION DU SCENARIO DE NETTOYAGE -- #
    print("Quel Scénario de nettoyage souhaitez-vous utiliser ?")
    print("1 : Nettoyage des données brutes et supprime toutes les lignes avec des valeurs manquantes")
    print("2 : Nettoyage des données brutes et remplace les valeurs manquantes par la moyenne")
    print("3 : Nettoyage des données brutes et remplace les valeurs manquantes par la médiane")
    choix_scenario = input("Votre choix : ")

    # -- SI L'UTILISATEUR CHOISIT LE SCENARIO 1 -- #
    if choix_scenario == "1":
        from Cleaner import brut_cleaner
        if os.path.exists("Cleaned_Data/Fraud_brutcleaned.csv"):
            print("Un DataSet avec le scénario existe déjà dans le dossier Cleaned_Data.\nSupprimer le et relancer l'application si vous souhaitez refaire le nettoyage des données.\n ")
            time.sleep(5)
            fraud_file_path = "Cleaned_Data/Fraud_brutcleaned.csv"

        else:
            brut_cleaner.clean_data("Fraud.csv", "Cleaned_Data/Fraud_brutcleaned.csv")
            print("Les données ont été nettoyées, le fichier Fraud_brutcleaned.csv a été créé dans le dossier Cleaned_Data\n")
            time.sleep(5)
            fraud_file_path = "Cleaned_Data/Fraud_brutcleaned.csv"

    # -- SI L'UTILISATEUR CHOISIT LE SCENARIO 2 -- #
    if choix_scenario == "2":
        from Cleaner import impute_cleaner
        if os.path.exists("Cleaned_Data/Fraud_imputecleaned.csv"):
            print("Un DataSet avec le scénario existe déjà dans le dossier Cleaned_Data.\nSupprimer le et relancer l'application si vous souhaitez refaire le nettoyage des données. \n")
            time.sleep(5)
            fraud_file_path = "Cleaned_Data/Fraud_imputecleaned.csv"

        else:
            impute_cleaner.clean_data("Fraud.csv", "Cleaned_Data/Fraud_imputecleaned.csv")
            print("Les données ont été nettoyées, le fichier Fraud_imputecleaned.csv a été créé dans le dossier Cleaned_Data\n")
            time.sleep(5)
            fraud_file_path = "Cleaned_Data/Fraud_imputecleaned.csv"

    # -- SI L'UTILISATEUR CHOISIT LE SCENARIO 3 -- #
    if choix_scenario == "3":
        from Cleaner import median_cleaner
        if os.path.exists("Cleaned_Data/Fraud_mediancleaned.csv"):
            print("Un DataSet avec le scénario existe déjà dans le dossier Cleaned_Data.\nSupprimer le et relancer l'application si vous souhaitez refaire le nettoyage des données.\n ")
            time.sleep(5)
            fraud_file_path = "Cleaned_Data/Fraud_mediancleaned.csv"

        else:
            median_cleaner.clean_data("Fraud.csv", "1Cleaned_Data/Fraud_mediancleaned.csv")
            print("Les données ont été nettoyées, le fichier Fraud_mediancleaned.csv a été créé dans le dossier Cleaned_Data\n")
            time.sleep(2)
            fraud_file_path = "Cleaned_Data/Fraud_mediancleaned.csv"

    # -- MENU DE SELECTION DU MODELE DE ML -- #
    print("Quel modèle de Machine Learning souhaitez-vous utiliser ?")
    print("1 : Linear Regression")
    print("2 : Logistic Regression")
    print("3 : Ridge Regression")
    print("4 : Lasso Regression")
    print("5 : Decision Tree")
    print("6 : Random Forest")
    print("7 : Gradient Boosting Regression")
    print("8 : XGBoost")
    print("9 : LightGBM Regressor")
    print("10 : K-Means")
    print("11 : Hierarchical Clustering")
    print("12 : Gaussian Mixture Model")
    print("13 : Aprirori algorithm")
    choix_model_ml= input("Votre choix : ")

    # -- SI L'UTILISATEUR CHOISIT LE MODELE 1 -- #
    if choix_model_ml == "1":
        from ML_Model import linear_regression
        linear_regression.linear_regression(fraud_file_path)

    # -- SI L'UTILISATEUR CHOISIT LE MODELE 2 -- #
    if choix_model_ml == "2":
        from ML_Model import logistic_regression
        logistic_regression.logistic_regression(fraud_file_path)

    # -- SI L'UTILISATEUR CHOISIT LE MODELE 3 -- #
    if choix_model_ml == "3":
        from ML_Model import ridge_regression
        ridge_regression.ridge_regression(fraud_file_path)

    # -- SI L'UTILISATEUR CHOISIT LE MODELE 4 -- #
    if choix_model_ml == "4":
        from ML_Model import lasso_regression
        lasso_regression.lasso_regression(fraud_file_path)

    # -- SI L'UTILISATEUR CHOISIT LE MODELE 5 -- #
    if choix_model_ml == "5":
        from ML_Model import decision_tree
        decision_tree.decision_tree(fraud_file_path)

    # -- SI L'UTILISATEUR CHOISIT LE MODELE 6 -- #
    if choix_model_ml == "6":
        from ML_Model import random_forest
        random_forest.random_forest(fraud_file_path)

    # -- SI L'UTILISATEUR CHOISIT LE MODELE 7 -- #
    if choix_model_ml == "7":
        from ML_Model import gradient_boosting_regression
        gradient_boosting_regression.gradient_boosting_regression(fraud_file_path)

    # -- SI L'UTILISATEUR CHOISIT LE MODELE 8 -- #
    if choix_model_ml == "8":
        from ML_Model import xgboost
        xgboost.xgboost(fraud_file_path)

    # -- SI L'UTILISATEUR CHOISIT LE MODELE 9 -- #
    if choix_model_ml == "9":
        from ML_Model import lightgbm
        lightgbm.lightgbm(fraud_file_path)

    # -- SI L'UTILISATEUR CHOISIT LE MODELE 10 -- #
    if choix_model_ml == "10":
        from ML_Model import kmeans
        kmeans.kmeans(fraud_file_path)

    # -- SI L'UTILISATEUR CHOISIT LE MODELE 11 -- #
    if choix_model_ml == "11":
        from ML_Model import hierarchical_clustering
        hierarchical_clustering.hierarchical_clustering(fraud_file_path)

    # -- SI L'UTILISATEUR CHOISIT LE MODELE 12 -- #
    if choix_model_ml == "12":
        from ML_Model import gaussian_mixture_model
        gaussian_mixture_model.gaussian_mixture_model(fraud_file_path)

    # -- SI L'UTILISATEUR CHOISIT LE MODELE 13 -- #
    if choix_model_ml == "13":
        from ML_Model import apriori
        apriori.apriori_model(fraud_file_path)

    print("\nMerci d'avoir utilisé notre programme !")
    exit()


if choix == "2":
    print("\nVous avez quitté le programme, à bientôt !")
    exit()