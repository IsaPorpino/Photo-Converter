from PIL import Image
import io
import streamlit as st

def loadImage(file):
    photo = Image.open(file)
    photoFormat = photo.format

    return photoFormat

def convertImage(file, format):
    photo = Image.open(file)
    selectedFormat = format
    buffer = io.BytesIO()
    photo.save(buffer, format=selectedFormat)

    convertedPhoto = buffer.getvalue()

    return convertedPhoto

def photoChange(uploadedFile, options):
    photoFormat = loadImage(uploadedFile)
    st.write(f"O formato da imagem inserida é: {photoFormat}")
    if photoFormat == "PNG" or photoFormat == "JPEG" or photoFormat == "BMP":
        options.remove(photoFormat)
        selectedFormat = st.selectbox("Selecione formato para conversão", options)

        if selectedFormat != "-":
            st.write(f"Faça o download da foto em {selectedFormat}:")
            convertedPhoto = convertImage(uploadedFile, selectedFormat)
            st.download_button('download', convertedPhoto, mime=f"image/{selectedFormat}")

    else:
        st.write(f"O formato {photoFormat} não é suportado para conversão")