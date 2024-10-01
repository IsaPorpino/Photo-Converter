import streamlit as st
from functions import *

def conversorFormatoPage():
    st.title('Conversor de Imagens')
    options = ["-","PNG", "BMP", "JPEG"]
    uploadedFile = st.file_uploader('Insira a sua imagem:')

    if uploadedFile is not None:
        photoChange(uploadedFile, options)