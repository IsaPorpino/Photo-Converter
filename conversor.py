import streamlit as st
from functions import *

def conversorFormatoPage():
    st.title('Conversor de Formato de Imagens')
    formatOptions = ["-","PNG", "BMP", "JPEG"]
    uploadedFile = st.file_uploader('Insira a sua imagem:')

    if uploadedFile is not None:
        photoChangeFormato(uploadedFile, formatOptions)

def conversorCorPage():
    st.title('Conversor de Cor de Imagens')
    colorOptions = ["-", "RGB", "L", "RGBA", "CMYK", "1"]
    uploadedFile = st.file_uploader('Insira a sua imagem:')

    if uploadedFile is not None:
        photoChangeCor(uploadedFile, colorOptions)
