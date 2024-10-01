from PIL import Image
import io
import streamlit as st

def getFormat(file):
    photo = Image.open(file)
    photoFormat = photo.format

    return photoFormat

def getColorMode(file):
    photo = Image.open(file)
    photoColor = photo.mode

    return photoColor

def convertImageFormat(file, format):
    photo = Image.open(file)
    selectedFormat = format
    buffer = io.BytesIO()
    photo.save(buffer, format=selectedFormat)

    convertedPhoto = buffer.getvalue()

    return convertedPhoto

def convertColorMode(file, colorMode):
    photo = Image.open(file)
    selectedColorMode = colorMode
    format = photo.format if selectedColorMode != "CMYK" else "JPEG"
    partiallyConvertedPhoto = photo.convert(mode=selectedColorMode)

    buffer = io.BytesIO()
    partiallyConvertedPhoto.save(buffer, format=format)

    finalConvertedPhoto = buffer.getvalue()

    return finalConvertedPhoto

def photoChangeFormato(uploadedFile, formatOptions):
    photoFormat = getFormat(uploadedFile)
    st.write(f"O formato da imagem inserida é: {photoFormat}")
    if photoFormat == "PNG" or photoFormat == "JPEG" or photoFormat == "BMP":
        formatOptions.remove(photoFormat)
        selectedFormat = st.selectbox("Selecione formato para conversão", formatOptions)

        if selectedFormat != "-":
            st.write(f"Faça o download da foto em {selectedFormat}:")
            convertedPhoto = convertImageFormat(uploadedFile, selectedFormat)
            st.download_button('download', convertedPhoto, mime=f"image/{selectedFormat}")

    else:
        st.write(f"O formato {photoFormat} não é suportado para conversão")

def photoChangeCor(uploadedFile,colorOptions):
    photoColor = getColorMode(uploadedFile)
    photoFormat = getFormat(uploadedFile)
    st.write(f"O modo de cor da imagem inserida é: {photoColor}")

    colorOptions.remove(photoColor)
    selectedColorMode = st.selectbox("Selecione formato para conversão", colorOptions)

    if selectedColorMode != "-":
        st.write(f"Faça o download da foto em {selectedColorMode}:")
        convertedPhoto = convertColorMode(uploadedFile, selectedColorMode)

        if selectedColorMode != "CMYK":
            st.download_button('download', convertedPhoto, mime=f"image/{photoFormat}")
        else:
            st.download_button('download', convertedPhoto, mime=f"image/jpeg")

