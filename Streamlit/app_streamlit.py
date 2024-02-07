import streamlit as st
import requests
import matplotlib.pyplot as plt

# Définissez le titre de l'application
st.title("Interface Streamlit pour l'API de prédiction de crédit")

# Créez une entrée de texte pour saisir l'ID du client
client_id = st.text_input("Entrez l'ID du client (ex: 124782):")

# Créez un bouton pour interroger l'API
if st.button("Obtenir la prédiction"):
    if client_id:
        # Requête à l'API Flask
        api_url = f"https://ocp7-dc846df71c5b.herokuapp.com/api/predict/{client_id}"

        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            st.write("Résultat de la prédiction :")
            st.write(f"Probabilité : {data['probability']}%")
            st.write(f"Classe : {data['classe']}")

            st.bar_chart({"Accepté": data['probability'], "Refusé": 100 - data['probability']})

            st.text(f"Compteur : {data['probability']}")


            labels = ['accepte', 'refuse']
            colors = ['green' if data['classe'] == 'accepte' else 'red']
            plt.pie([data['probability'], 100 - data['probability']], labels=labels, colors=colors, autopct='%1.1f%%')
            plt.legend(labels)
            st.pyplot(plt)


        elif response.status_code == 404:
            st.write("ID inconnu.")
        else:
            st.write("Erreur lors de la requête à l'API.")
    else:
        st.write("Veuillez entrer un ID de client.")
