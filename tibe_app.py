import streamlit as st

# Configuration de la page
st.set_page_config(page_title="TIBE SMART-HUB", page_icon="💎")

# Affichage du titre
st.title("💎 TIBE SMART-HUB")

# Ceci est la manière correcte d'afficher votre texte de bienvenue en Python
st.markdown("""
Bienvenue sur l'application officielle de gestion et de vente de TIBE.

### 🚀 Fonctionnalités :
* **Boutique en ligne** : Consultation des articles (vêtements, bétail, etc.).
* **Panier intelligent** : Commande directe envoyée par WhatsApp.
* **Gestion Admin** : Suivi des stocks et statistiques de ventes sécurisés.
* **Facturation** : Génération de reçus professionnels.
""")

st.info("Développé par KOLANI Tibe Mankenam - Lomé, Togo")

# Un bouton test pour WhatsApp
if st.button("Tester le contact WhatsApp"):
    st.write("Lien vers le 92498837 prêt !")
  
