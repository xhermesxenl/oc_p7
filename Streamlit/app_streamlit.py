import streamlit as st
import requests
import matplotlib.pyplot as plt
import plotly.express as px

# Définissez le titre de l'application
st.image("../logo.png", caption='logo', use_column_width=True)
st.title("Prédiction du Risque de Non-Remboursement")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Constante
seuil = 0.48
couleur_accepte = "#3B782F"
couleur_refuse  = "#B82010"


# Créez une entrée de texte pour saisir l'ID du client
client_id = st.text_input("Entrez l'ID du client (ex: 144194, 58369):")

# Créez un bouton pour interroger l'API
if st.button("Obtenir la prédiction"):
    if client_id:
        # Requête à l'API Flask
        api_url = f"https://ocp7-dc846df71c5b.herokuapp.com/api/predict/{client_id}"

        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()

            if data['classe'] == 'accepte':
                color = couleur_accepte
                message = 'accepté'
            else:
                color = couleur_refuse
                message = 'refusé'

            st.write(f'<p style="background-color:{color}; color:#ffffff; font-size:24px; border-radius:5px; padding:10px; text-align:center;">Le prêt est {message}</p>', unsafe_allow_html=True)

            prediction_details = {
                "Probabilité de Non-Remboursement": f"{data['probability']}%",
                "Classe": data['classe']
            }

            # Affichage des détails de la prédiction dans des colonnes alignées sur la largeur
            col1, col2 = st.columns(2)
            with col1:
                st.write("Détail de la prédiction :")
            with col2:
                for key, value in prediction_details.items():
                    st.write(f"{key} : {value}")





            # Données pour le graphique
            categories = ['Accepté', 'Refusé']
            probability = data['probability']
            values = [probability, 100 - probability]  # Probabilités calculées
            colors = ['green', 'red']  # Couleurs pour chaque catégorie
            seuil_pourc = 0.48 * 100  # Convertir le seuil en pourcentage pour correspondre à l'échelle du graphique

            # Création du graphique à barres
            fig, ax = plt.subplots()
            bars = ax.bar(categories, values, color=colors)

            # Ajout de la ligne de seuil
            ax.axhline(y=seuil_pourc, color='blue', linestyle='--', label=f'Seuil: {seuil_pourc}%')

            # Ajout de titres et étiquettes
            ax.set_ylabel('Pourcentage')
            ax.set_title('Répartition par classe')
            ax.set_ylim(0, 100)
            ax.legend()

            # Afficher les valeurs sur les barres
            for bar in bars:
                height = bar.get_height()
                ax.annotate(f'{height}%',
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 3),  # Décalage vertical pour le label
                            textcoords="offset points",
                            ha='center', va='bottom')


            # Affichage du graphique dans Streamlit
            st.pyplot(fig)








            #
            # plt.pie([data['probability'], 100 - data['probability']], labels=labels, colors=colors, autopct='%1.1f%%')
            # plt.legend(labels)
            # st.pyplot(plt)


        elif response.status_code == 404:
            st.write("ID inconnu.")
        else:
            st.write("Erreur lors de la requête à l'API.")
    else:
        st.write("Veuillez entrer un ID de client.")
