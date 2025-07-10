# import pyautogui as pg
from PIL import Image
#x,y = pg.size()

#pg.moveTo(0/2,0/2)

#pg.click(30, 1070)

# def abrir_navegador(browser):
#     pg.hotkey('win', 'r')
#     pg.write(browser)
#     pg.press('enter')
#
#
# opcao = pg.prompt('[1]Edge \n[2]Chrome', 'Navegador')
# if opcao == '1':
#     abrir_navegador('msedge')
# elif opcao == '2':
#     abrir_navegador('chrome')
# else:
#     pg.alert('Programa não encontrado')

# pg.hotkey('win','r')
# pg.write('chrome')
# pg.press('enter')


# pg.mouseInfo()
def modificar_pixel(pixel: tuple, percentual: float) -> tuple:
    r,g,b = pixel
    escala = 1+percentual/100
    r, g, b = int(r * escala), int(g * escala), int(b * escala)
    return min(r, 255), min(g, 255), min(b, 255)

imagem = Image.open('pucca.webp')
imagem.show()
pixels = imagem.getdata()
nova_imagem = []
for pixel in pixels:
    nova_imagem.append(modificar_pixel(pixel, 50))
imagem.putdata(nova_imagem)
imagem.show()

# imagem = imagem.convert('L')
# imagem = imagem.rotate(45, fillcolor=(255,0,0))
# imagem = imagem.resize((50,50))
# imagem.save('convertido.png')
#
# # imagem.show()
#
# print(imagem.format)
# print(imagem.size)
# print(imagem.mode)