""" This code will resize & open a image file and give some info using Image"""
from PIL import Image

image = Image.open('image.jpg')
print("Image format:",image.format)
print("Image mode:",image.mode)
image.resize((400,400)).show()