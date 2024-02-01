from flask import Flask, request, jsonify, render_template  
import pandas as pd
import pickle
import shap
import os
from shap import LinearExplainer, KernelExplainer, Explanation, TreeExplainer
from shap.maskers import Independent
shap.initjs()

# Exemple
# http://127.0.0.1:5000/api/predict/124782
# http://127.0.0.1:5000/api/predict/58369
# https://www.younup.fr/blog/heroku-pour-deployer-votre-application-python-flask-dans-le-cloud

app = Flask(__name__)
model_filename = "model.pkl"
data_test = pd.read_csv("test_api.csv")

model_path = os.path.join(os.getcwd(), model_filename)

print(model_path)

# Charger le modèle depuis un fichier
with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

lgbm_model = model.named_steps["LGBMC"]
explainer = shap.TreeExplainer(lgbm_model)


@app.route('/')
def welcome():
    return "Bienvenue dans l'API de prédiction de crédit !"

@app.route('/html')
def home():
   return render_template("index.html")

@app.route("/api", methods=["GET"])
def liste_identifiants():    
    features = data_test.columns.tolist()
    id_client = data_test.index.tolist()
    liste_id = data_test["SK_ID_CURR"].tolist()

    return jsonify({
        "id_client": id_client,       
        "features": features,       
        "liste_id": liste_id,
                })

@app.route("/api/data/<int:id_client>/", methods=["GET"])
def donnees_client(id_client):

    if id_client in data_test["SK_ID_CURR"].tolist():
        data_client = data_test.loc[data_test["SK_ID_CURR"] == id_client]
        return jsonify(data_client.to_dict(orient="records"))
    else:
        return jsonify({"error": "Unknown ID"}), 404
    

@app.route("/api/predict/<int:id_client>", methods=["GET"])
def predict_score_client(id_client):    
    
    if id_client in data_test["SK_ID_CURR"].tolist():
        data_client = data_test.loc[data_test["SK_ID_CURR"] == id_client]
        data_client = data_client.drop(["Unnamed: 0", "SK_ID_CURR"], axis=1)
        proba = model.predict_proba(data_client)
        proba_0 = round(proba[0][0] * 100)

        seuil_optimal = 0.51  
        value_seuil_optimal =   seuil_optimal * 100

        # Classer le client comme "accepté" ou "refusé" en fonction du seuil
        classe = "accepte" if proba_0 > value_seuil_optimal else "refuse"

        return jsonify({"probability": proba_0, "classe": classe})
    else:
        return jsonify({"error": "Unknown ID"}), 404
    
@app.route("/api/shap/<int:id_client>", methods=["GET"])
def shap_values_client(id_client):

    if id_client in data_test["SK_ID_CURR"].tolist():
        data_client = data_test.loc[data_test["SK_ID_CURR"] == id_client]
        data_client = data_client.drop(["Unnamed: 0", "SK_ID_CURR"], axis=1)    
        shap_values = explainer.shap_values(data_client)
        shap_data_flat = [float(val) for val in shap_values[0].ravel()]
        return jsonify({"shap_val": shap_data_flat})
    else:
        return jsonify({"error": "Unknown ID"}), 404

if __name__ == "__main__":
    app.run(debug=True)

