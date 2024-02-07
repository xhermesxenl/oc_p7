import streamlit as st
import requests

# Définissez le titre de l'application
st.title("Interface Streamlit pour l'API de prédiction de crédit")

# Créez une entrée de texte pour saisir l'ID du client
client_id = st.text_input("Entrez l'ID du client (ex: 124782):")

# Créez un bouton pour interroger l'API
if st.button("Obtenir la prédiction"):
    if client_id:
        # Faites la requête à l'API Flask en local
        api_url = f"http://127.0.0.1:5000/credit/{client_id}/predict"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            st.write("Résultat de la prédiction :")
            st.write(f"Probabilité : {data['probability']}%")
            st.write(f"Classe : {data['classe']}")
        elif response.status_code == 404:
            st.write("ID inconnu.")
        else:
            st.write("Erreur lors de la requête à l'API.")
    else:
        st.write("Veuillez entrer un ID de client.")
