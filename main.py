import streamlit as st

# Importar aplicaciones externas
from eda import eda_app
from ml import ml_app

st.set_page_config("App Principal")

def main():
    st.title("Aplicación principal")
    menu = ["Home","EDA","ML","Acerca de"]
    opcion = st.sidebar.selectbox("Menú",menu)
    
    if opcion == "Home":
        st.subheader("Home")
    elif opcion == "EDA":
        eda_app()
    elif opcion == "ML":
        ml_app()
    else:
        st.subheader("Acerca de ..")
    

main()
    