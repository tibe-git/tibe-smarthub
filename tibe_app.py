import streamlit as st

# Configuration de la page
st.set_page_config(page_title="TIBE SMART-HUB", page_icon="💎")

# Titre principal
st.title("💎 TIBE SMART-HUB")

# Texte de présentation
st.markdown("""
Bienvenue sur l'application officielle de gestion et de vente de TIBE.

### 🚀 Fonctionnalités :
* **Boutique en ligne** : Consultation des articles (vêtements, bétail, etc.).
* **Panier intelligent** : Commande directe envoyée par WhatsApp.
* **Gestion Admin** : Suivi des stocks et statistiques de ventes sécurisés.
* **Facturation** : Génération de reçus professionnels.
""")

st.info("Développé par KOLANI Tibe Mankenam - Lomé, Togo")

# --- LA PARTIE À MODIFIER POUR LE CONTACT ---
st.subheader("📱 Passer une commande")

# On crée le lien avec l'indicatif du Togo (228)
numero_togo = "22892498837"
lien_wa = f"https://wa.me/{numero_togo}"

# Ce bouton est magique : il ouvre WhatsApp tout seul !
st.link_button("🚀 Nous contacter sur WhatsApp", lien_wa)
