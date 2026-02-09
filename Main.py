import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title="Audit de flux produits", 
    page_icon="📡", 
    layout="centered"
)

# ═══════════════════════════════════════════════════════════════
# 🎯 HEADER - Banner et titre principal
# ═══════════════════════════════════════════════════════════════
st.image("./images/audit_flux_banner.png", use_column_width=True)

st.title("📡 Audit de Flux Produits")
st.markdown("""
    <p style='font-size: 18px; color: #555;'>
        Analysez et optimisez votre flux produits Google Shopping en quelques clics.
    </p>
""", unsafe_allow_html=True)

st.divider()

# ═══════════════════════════════════════════════════════════════
# 📋 GUIDE D'UTILISATION
# ═══════════════════════════════════════════════════════════════
st.subheader("🚀 Comment importer votre flux ?")

with st.expander("📖 Voir le guide étape par étape", expanded=True):
    
    # Étape 1
    st.markdown("### **Étape 1** : Accéder à l'historique des mises à jour")
    st.markdown("""
        Dans votre **Merchant Center**, naviguez vers :  
        `Paramètres` → `Sources de données` → `Afficher l'historique des mises à jour`
    """)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image("./images/MC-histo_maj.png", use_column_width=True)
    
    st.markdown("---")
    
    # Étape 2
    st.markdown("### **Étape 2** : Télécharger le fichier source")
    st.markdown("""
        Cliquez sur le bouton **"Télécharger le fichier de source de données"**  
        pour récupérer votre flux au format CSV.
    """)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image("./images/MC-histo_upload.png", use_column_width=True)
    
    st.markdown("---")
    
    # Étape 3
    st.markdown("### **Étape 3** : Uploader votre fichier")
    st.markdown("""
        Une fois téléchargé, **uploadez le fichier** dans la barre latérale à droite 👉  
        L'analyse démarrera automatiquement !
    """)

st.divider()

# ═══════════════════════════════════════════════════════════════
# 📤 SIDEBAR - Upload du fichier
# ═══════════════════════════════════════════════════════════════
st.sidebar.markdown("## 📤 Import de flux")
st.sidebar.markdown("Uploadez votre fichier CSV pour commencer l'analyse.")

uploaded_file = st.sidebar.file_uploader(
    "Sélectionnez votre fichier",
    type=["csv"],
    help="Format accepté : CSV avec séparateur '|'"
)

# ═══════════════════════════════════════════════════════════════
# 🔄 TRAITEMENT DU FICHIER
# ═══════════════════════════════════════════════════════════════
if uploaded_file:
    try:
        # Chargement du fichier
        with st.spinner("⏳ Chargement du flux en cours..."):
            flux = pd.read_csv(uploaded_file, sep="|", engine='python')
            st.session_state["flux_data"] = flux
        
        # Confirmation de succès
        st.success("✅ **Flux chargé avec succès !**")
        
        # Métriques rapides
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📦 Produits", f"{len(flux):,}")
        with col2:
            st.metric("📊 Colonnes", len(flux.columns))
        with col3:
            st.metric("💾 Taille", f"{uploaded_file.size / 1024:.1f} Ko")
        
        # Aperçu des données
        st.markdown("### 👀 Aperçu des données")
        st.dataframe(
            flux.head(10), 
            use_container_width=True,
            height=300
        )
        
        # Call to action
        st.info("💡 **Prêt pour l'analyse ?** Utilisez le menu latéral pour accéder aux différentes pages d'audit.")
        
    except Exception as e:
        st.error(f"❌ **Erreur lors du chargement** : {e}")
        st.warning("Vérifiez que votre fichier est bien au format CSV avec séparateur '|'")

else:
    # Message d'attente
    st.info("💡 **En attente de votre fichier...**")
    st.markdown("""
        👈 Uploadez votre flux produit dans la barre latérale pour démarrer l'audit.
    """)

# ═══════════════════════════════════════════════════════════════
# 📌 FOOTER
# ═══════════════════════════════════════════════════════════════
st.divider()
st.markdown("""
    <p style='text-align: center; color: #888; font-size: 12px;'>
        📡 Audit de Flux Produits | Optimisez vos performances Google Shopping
    </p>
""", unsafe_allow_html=True)
