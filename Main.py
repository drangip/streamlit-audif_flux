import streamlit as st
import pandas as pd

st.set_page_config(page_title="Audit de flux produits", page_icon="📡", layout="centered")

st.image("./images/audit_flux_banner.png", use_column_width=True)

st.write("""This application allows you to audit your shopping product feed.""")
st.write("To import your feed, please follow the steps below:")
st.write("In your Merchant Center, go to Settings > Data sources > View update history.")

st.image("./images/MC-histo_maj.png", use_column_width=True)

st.write("Then click 'Download the data source file' to upload your feed.")

st.image("./images/MC-histo_upload.png", use_column_width=True)

st.write("Finally, upload the file to the sidebar on the right.")

st.sidebar.write("## Upload de flux produit")

uploaded_file = st.sidebar.file_uploader("📥 Upload your product feed.")

if uploaded_file:
    try:
        flux = pd.read_csv(uploaded_file, sep="|", engine='python')
        st.session_state["flux_data"] = flux  # 🔹 Stockage dans la session
        st.success("✅ Flux chargé et enregistré en mémoire.")
        st.dataframe(flux.head())
        st.info("Tu peux maintenant aller dans les pages d’analyse via la barre latérale.")
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier : {e}")
else:
    st.info("💡 En attente d’un fichier CSV.")
