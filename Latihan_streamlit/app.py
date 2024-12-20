import streamlit as st

dashboard = st.Page("./fitur/dashboard.py", title= "Dashboar")
nabung = st.Page("./fitur/nabung.py", title= "Menabung")

pg = st.navigation(
    {
      "Menu Utama" : [dashboard],
      "Transaksi"  : [nabung],


    }
)

if "total_semua" not in st.session_state:
    st.session_state["total_semua"] = []


# CSS to Streamlit 
st.markdown(
    """
    <style>
    /* Warna latar belakang aplikasi */
    .stApp {
        background-color: #fffff;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #8D0B41;
        color: white;
        padding: 5px;
    }

    /* Teks pada sidebar */
    [data-testid="stSidebar"] * {
        color: white !important;
        font-size: 16px;
        margin-bottom: 5px;
        margin-top: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

pg.run()