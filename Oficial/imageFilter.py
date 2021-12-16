import cv2
import numpy as np
import colorFilter

image = cv2.imread('StoriesUploads/teste.png')

class FilterImage():
  def __init__(self):
    def resizeImage(imagem):
      porcetagem_escala = 10
      comprimento = int(imagem.shape[1] * porcetagem_escala / 100)
      altura = int(imagem.shape[0] * porcetagem_escala / 100)
      dimensao_imagem = (comprimento, altura)
      return cv2.resize(imagem, dimensao_imagem, interpolation = cv2.INTER_AREA)

    while(True):
      imageResized = resizeImage(image)

      key = cv2.waitKey(10)

      if key != -1:
        key = chr(key)

      if key == '\x1b':
        break

      if key == '1':
        maskgreyscale = colorFilter.greyscale(imageResized)
        cv2.imshow('Tons de Cinza', maskgreyscale)
        cv2.imwrite('StoriesDownloads/images/maskgreyscale.png', maskgreyscale)
      elif key == '2':      
        radioactive = colorFilter.invertmask(imageResized)
        cv2.imshow('Radioativo', radioactive)
        cv2.imwrite('StoriesDownloads/images/radioactive.png', radioactive)
      elif key == '3':      
        painting = colorFilter.painting(imageResized)
        cv2.imshow('Pintura', painting)
        cv2.imwrite('StoriesDownloads/images/painting.png', painting)
      elif key == '4':      
        light = colorFilter.light(imageResized)
        cv2.imshow('Luminosidade', light)
        cv2.imwrite('StoriesDownloads/images/light.png', light)
      elif key == '5':      
        rouge = colorFilter.rouge(imageResized)
        cv2.imshow('Deteccao de Cores Vermelhas', rouge)
        cv2.imwrite('StoriesDownloads/images/rouge.png', rouge)

      if cv2.waitKey(1) & 0xFF == ord('q'):
        break

      # out.write(result)
      cv2.imshow('Imagem Filtro',imageResized)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.waitKey(0)
    cv2.destroyAllWindows()