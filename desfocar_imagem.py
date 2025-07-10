from PIL import Image, ImageFilter

imagem = Image.open('pucca.webp')
nova_imagem = imagem.filter(ImageFilter.CONTOUR)
imagem.show()
nova_imagem.show()