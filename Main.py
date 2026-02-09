import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Product Feed Audit", 
    page_icon="📡", 
    layout="centered"
)

# ═══════════════════════════════════════════════════════════════
# 🎯 HEADER - Banner and main title
# ═══════════════════════════════════════════════════════════════
st.image("./images/audit_flux_banner.png", use_column_width=True)

st.title("📡 Product Feed Audit")
st.markdown("""
    <p style='font-size: 18px; color: #555;'>
        Analyze and optimize your Google Shopping product feed in just a few clicks.
    </p>
""", unsafe_allow_html=True)

st.divider()

# ═══════════════════════════════════════════════════════════════
# 📋 USER GUIDE
# ═══════════════════════════════════════════════════════════════
st.subheader("🚀 How to import your feed?")

with st.expander("📖 View step-by-step guide", expanded=True):
    
    # Step 1
    st.markdown("### **Step 1**: Access update history")
    st.markdown("""
        In your **Merchant Center**, navigate to:  
        `Settings` → `Data sources` → `View update history`
    """)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image("./images/MC-histo_maj.png", use_column_width=True)
    
    st.markdown("---")
    
    # Step 2
    st.markdown("### **Step 2**: Download the source file")
    st.markdown("""
        Click on the **"Download the data source file"** button  
        to retrieve your feed in CSV format.
    """)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image("./images/MC-histo_upload.png", use_column_width=True)
    
    st.markdown("---")
    
    # Step 3
    st.markdown("### **Step 3**: Upload your file")
    st.markdown("""
        Once downloaded, **upload the file** in the sidebar on the right 👉  
        The analysis will start automatically!
    """)

st.divider()

# ═══════════════════════════════════════════════════════════════
# 📤 SIDEBAR - File upload
# ═══════════════════════════════════════════════════════════════
st.sidebar.markdown("## 📤 Feed Import")
st.sidebar.markdown("Upload your CSV file to start the analysis.")

uploaded_file = st.sidebar.file_uploader(
    "Select your file",
    type=["csv"],
    help="Accepted format: CSV with '|' separator"
)

# ═══════════════════════════════════════════════════════════════
# 🔄 FILE PROCESSING
# ═══════════════════════════════════════════════════════════════
if uploaded_file:
    try:
        # Loading file
        with st.spinner("⏳ Loading feed..."):
            flux = pd.read_csv(uploaded_file, sep="|", engine='python')
            st.session_state["flux_data"] = flux
        
        # Success confirmation
        st.success("✅ **Feed loaded successfully!**")
        
        # Quick metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📦 Products", f"{len(flux):,}")
        with col2:
            st.metric("📊 Columns", len(flux.columns))
        with col3:
            st.metric("💾 Size", f"{uploaded_file.size / 1024:.1f} KB")
        
        # Data preview
        st.markdown("### 👀 Data Preview")
        st.dataframe(
            flux.head(10), 
            use_container_width=True,
            height=300
        )
        
        # Call to action
        st.info("💡 **Ready for analysis?** Use the sidebar menu to access the different audit pages.")
        
    except Exception as e:
        st.error(f"❌ **Error loading file**: {e}")
        st.warning("Please verify that your file is in CSV format with '|' separator")

else:
    # Waiting message
    st.info("💡 **Waiting for your file...**")
    st.markdown("""
        👈 Upload your product feed in the sidebar to start the audit.
    """)

# ═══════════════════════════════════════════════════════════════
# 📌 FOOTER
# ═══════════════════════════════════════════════════════════════
st.divider()
st.markdown("""
    <p style='text-align: center; color: #888; font-size: 12px;'>
        📡 Product Feed Audit | Optimize your Google Shopping performance
    </p>
""", unsafe_allow_html=True)
