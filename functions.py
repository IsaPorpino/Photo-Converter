from PIL import Image
import io
import streamlit as st

def loadImage(file):
    photo = Image.open(file)
    photoFormat = photo.format

    return photoFormat

def convertImage(file):
    photo = Image.open(file)
    buffer = io.BytesIO()
    photo.save(buffer, format="BMP")

    convertedPhoto = buffer.getvalue()

    return convertedPhoto
'''
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
    '''