from PIL import Image
import io
import streamlit as st

def loadImage(file):
    photo = Image.open(file)
    photoFormat = photo.format
    st.write(f"O formato da imagem inserida é: {photoFormat}")

    return photoFormat
    #photo.show()
    #photo.save('./img/Taytay.bmp', 'BMP')

def convertImageToBMP(file):
    photo = Image.open(file)
    buffer = io.BytesIO()
    photo.save(buffer, format="BMP")

    convertedPhotoBmp = buffer.getvalue()

    return convertedPhotoBmp

def convertImageToPNG(file):
    photo = Image.open(file)
    buffer = io.BytesIO()
    photo.save(buffer, format="PNG")

    convertedPhotoPng = buffer.getvalue()
    buffer.close()

    return convertedPhotoPng

def convertImageToJPEG(file):
    photo = Image.open(file)
    buffer = io.BytesIO()
    photo = photo.convert("RGB")
    photo.save(buffer, format="JPEG")

    convertedPhotoJpeg = buffer.getvalue()
    buffer.close()

    return convertedPhotoJpeg
def interface():
    st.title('Conversor de Imagens')
    uploadedFile = st.file_uploader('Insira a sua imagem:')

    if uploadedFile is not None:

        photoFormat = loadImage(uploadedFile)
        st.write(f"O formato da imagem inserida é: {photoFormat}")

        if photoFormat == "PNG":
            bmpPhoto = convertImageToBMP(uploadedFile)
            jpegPhoto = convertImageToJPEG(uploadedFile)

            st.download_button('download BMP', bmpPhoto)
            st.download_button('download JPG', jpegPhoto)


if __name__ == '__main__':
    #loadImage()
    interface()


