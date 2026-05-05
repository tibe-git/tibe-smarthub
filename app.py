import streamlit as st

# Configuration de la page
st.set_page_config(page_title="TIBE SMART-HUB", layout="wide")

# Titre principal
st.title("💎 TIBE SMART-HUB")
st.write("Bienvenue, KOLANI Tibe. Gérez vos ventes et votre stock ici.")

# Menu latéral
menu = ["Boutique", "Gestion Admin", "Facturation"]
choix = st.sidebar.selectbox("Menu Principal", menu)

if choix == "Boutique":
    st.header("🚀 Boutique en ligne")
    st.info("Section pour les vêtements et le bétail.")
    # Simulation d'un article
    st.subheader("Article : Poulet local")
    if st.button("Commander via WhatsApp"):
        numero = "92498837"
        message = "Bonjour Tibe, je souhaite commander un poulet."
        whatsapp_url = f"https://wa.me/{numero}?text={message}"
        st.write(f"[Cliquez ici pour envoyer la commande]({whatsapp_url})")

elif choix == "Gestion Admin":
    st.header("🛠️ Suivi des stocks")
    # Ici vous pourrez ajouter vos tableaux de gestion plus tard
    st.write("Statistiques de ventes sécurisées en cours de configuration.")

elif choix == "Facturation":
    st.header("📄 Génération de reçus")
    nom_client = st.text_input("Nom du client")
    montant = st.number_input("Montant (FCFA)", min_value=0)
    if st.button("Générer reçu"):
        st.success(f"Reçu généré pour {nom_client} - Montant : {montant} FCFA")
      
