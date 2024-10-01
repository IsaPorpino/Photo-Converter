import streamlit as st
from conversor import conversorFormatoPage, conversorCorPage
from home import homePage

pages = {
    "Informações": [
        st.Page(homePage, title="Home")
    ],
    "Conversores":  [
        st.Page(conversorFormatoPage, title="Conversor de Formato"),
        st.Page(conversorCorPage, title="Conversor de Cor")
    ]
    }
nav = st.navigation(pages)
nav.run()





