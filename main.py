import streamlit as st
from functions import *

def interface():
    st.title('Conversor de Imagens')
    uploadedFile = st.file_uploader('Insira a sua imagem:')

    if uploadedFile is not None:

        photoFormat = loadImage(uploadedFile)
        st.write(f"O formato da imagem inserida é: {photoFormat}")

        if photoFormat == "PNG":
            convertedPhoto = convertImage(uploadedFile)
            st.download_button('download BMP', convertedPhoto, mime="image/bmp")
            st.download_button('download JPG', convertedPhoto, mime="image/jpg")

        elif photoFormat == "JPG":
            convertedPhoto = convertImage(uploadedFile)
            st.download_button('download PNG', convertedPhoto, mime="image/png")
            st.download_button('download BMP', convertedPhoto, mime="image/bmp")

        elif photoFormat == "BMP":
            convertedPhoto = convertImage(uploadedFile)
            st.download_button('download PNG', convertedPhoto, mime="image/png")
            st.download_button('download JPG', convertedPhoto, mime="image/jpg")

        else:
            st.write(f"O formato {photoFormat} não é suportado para conversão")

if __name__ == '__main__':
    #loadImage()
    interface()


