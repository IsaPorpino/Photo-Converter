import streamlit as st

import conversor
from conversor import conversorFormatoPage
from home import homePage

pages = {
    "Informações": [
        st.Page(homePage, title="Home")
    ],
    "Conversores":  [
        st.Page(conversorFormatoPage, title="Conversor de Formato")
    ]
    }
nav = st.navigation(pages)
nav.run()





