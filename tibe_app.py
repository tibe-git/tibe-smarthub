 import streamlit as st

# Configuration de la page
st.set_page_config(page_title="TIBE SMART-HUB", page_icon="💎")

# Titre principal
st.title("💎 TIBE SMART-HUB")

# Présentation
st.markdown("""
Bienvenue sur l'application officielle de gestion et de vente de TIBE.

### 🚀 Fonctionnalités :
* **Boutique en ligne** : Consultation des articles.
* **Panier intelligent** : Commande directe par WhatsApp.
* **Gestion Admin** : Suivi des stocks sécurisé.
""")

st.info("Développé par KOLANI Tibe Mankenam - Lomé, Togo")

# Section Contact
st.subheader("📱 Passer une commande")

numero_togo = "22892498837"
lien_wa = f"https://wa.me/{numero_togo}"

st.link_button("🚀 Nous contacter sur WhatsApp", lien_wa)
