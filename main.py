import streamlit as st
from functions import *

def interface():
    st.title('Conversor de Imagens')
    options = ["-","PNG", "BMP", "JPEG"]
    uploadedFile = st.file_uploader('Insira a sua imagem:')

    if uploadedFile is not None:
        photoChange(uploadedFile, options)


if __name__ == '__main__':
    #loadImage()
    interface()


