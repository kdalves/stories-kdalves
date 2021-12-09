import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
import cv2
import colorFilter
# import imageFilter
# import cameraFiltroAccessory
import numpy as np
# import videoWindow as vw

imageOpen = None
videoRecord = None

def printmask(img):
  height, width = img.shape

  for i in range(height):
    for j in range(width):
      print(f"{img[i, j]},")
    print("\n")

def video():
  media = [0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111]
  cap = cv2.VideoCapture(0)
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  out = cv2.VideoWriter('videoFiltros.mp4',fourcc, 20.0, (640,480))

  mask = np.reshape(media, (3, 3))

  while(True):
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame32f = np.float32(frame)
    frameFiltered = cv2.filter2D(frame32f, cv2.CV_32F, mask, anchor=(1, 1), delta=0)


    result = np.uint8(frameFiltered)

    key = cv2.waitKey(10)

    key = cv2.waitKey(10)

    if key != -1:
      key = chr(key)

    if key == '\x1b':
      break

    if key == '1':
      maskgreyscale = colorFilter.greyscale(frame)
      # mask = np.reshape(maskgreyscale, (3, 3))
      cv2.imshow('greyscale', maskgreyscale)
      filter = maskgreyscale
      cv2.imwrite('StoriesDownloads/videoGray.png', maskgreyscale)
    elif key == '2':      
      maskinvertmask = colorFilter.invertmask(frame)
      cv2.imshow('invertmask', maskinvertmask)
      filter = maskinvertmask
      cv2.imwrite('StoriesDownloads/videoRadioactive.png', maskinvertmask)
    elif key == '3':      
      painting = colorFilter.painting(frame)
      cv2.imshow('painting', painting)
      filter = painting
      cv2.imwrite('StoriesDownloads/videoPainting.png', painting)
    elif key == '4':      
      light = colorFilter.light(frame)
      cv2.imshow('light', light)
      filter = light
      cv2.imwrite('StoriesDownloads/videoLight.png', light)
    elif key == '5':      
      rouge = colorFilter.rouge(frame)
      cv2.imshow('rouge', rouge)
      filter = rouge
      cv2.imwrite('StoriesDownloads/videoRouge.png', rouge)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
    
    cv2.imshow("videoFiltros", result)
    out.write(result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cap.release()
  out.release()
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def accessory():
  cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

  img = cv2.imread('teste.png')

  def detection(grayscale, img):    
    face = cascade_face.detectMultiScale(grayscale, 1.3, 5)

    for (xface, yface, wface, hface) in face:        
      imgHeadAccessory= cv2.imread('Filters/graduate.png',-1)
          
      width, depth, _= imgHeadAccessory.shape
      width= int(wface + 0.1* width)
      depth= int(hface* 2/3)
      imgHeadAccessory= cv2.resize(imgHeadAccessory, (width, depth))
          
      centrex= xface + wface/2
      xHeadAccessory= int(centrex-width/2)  
      yHeadAccessory= int(yface- (depth*2/3) )
          
      if xHeadAccessory<0:
        xHeadAccessory=0
      if yHeadAccessory<0:
        yHeadAccessory=0
      y2=int(yHeadAccessory+depth)
      if(y2>= img.shape[0]): 
        y2= img.shape[0]
      x2= int(xHeadAccessory+width)
      if(x2>= img.shape[1]):
        x2= img.shape[1]
            
            
      imgHeadAccessory= imgHeadAccessory[0: y2-yHeadAccessory, 0:x2-xHeadAccessory] 
      bg=  img[yHeadAccessory: y2, xHeadAccessory: x2]
      sg = np.atleast_3d(255 - imgHeadAccessory[:, :,3])/255.0
      np.multiply(bg, sg, out=bg, casting="unsafe")
      np.add(bg, 255-imgHeadAccessory[:, :,0:3] * np.atleast_3d(imgHeadAccessory[:, :,3]), out=bg)
      img[yHeadAccessory: y2, xHeadAccessory: x2] = bg
          
      return img        


  cap = cv2.VideoCapture(0)
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  out = cv2.VideoWriter('graduateVideo.mp4',fourcc, 20.0, (640,480))

  cnt=0
  while cnt<500:
      _, img = cap.read()
      
      grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
      final = detection(grayscale, img) 
      
      if final is not None:
        cv2.imshow('Video', final) 
        out.write(final)

      key = cv2.waitKey(10)

      if key != -1:
        key = chr(key)

      if key == '\x1b':
        break

      if key == '1':
        cv2.imwrite('StoriesDownloads/graduate.png', final)
      
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
      
      cnt+=1
  cap.release()
  out.release()
  cv2.destroyAllWindows()

def imageFilter():
  image = cv2.imread('StoriesUploads/teste.png')

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
      cv2.imwrite('StoriesDownloads/maskgreyscale.png', maskgreyscale)
    elif key == '2':      
      radioactive = colorFilter.invertmask(imageResized)
      cv2.imshow('Radioativo', radioactive)
      cv2.imwrite('StoriesDownloads/radioactive.png', radioactive)
    elif key == '3':      
      painting = colorFilter.painting(imageResized)
      cv2.imshow('Pintura', painting)
      cv2.imwrite('StoriesDownloads/painting.png', painting)
    elif key == '4':      
      light = colorFilter.light(imageResized)
      cv2.imshow('Luminosidade', light)
      cv2.imwrite('StoriesDownloads/light.png', light)
    elif key == '5':      
      rouge = colorFilter.rouge(imageResized)
      cv2.imshow('Deteccao de Cores Vermelhas', rouge)
      cv2.imwrite('StoriesDownloads/rouge.png', rouge)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

    # out.write(result)
    cv2.imshow('Imagem Filtro',imageResized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cv2.waitKey(0)
  cv2.destroyAllWindows()

def changeVideo():
  media = [0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111]
  cap = cv2.VideoCapture(2)
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  out = cv2.VideoWriter('videoFiltros.mp4',fourcc, 20.0, (640,480))

  mask = np.reshape(media, (3, 3))

  while(True):
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame32f = np.float32(frame)
    frameFiltered = cv2.filter2D(frame32f, cv2.CV_32F, mask, anchor=(1, 1), delta=0)


    result = np.uint8(frameFiltered)

    key = cv2.waitKey(10)

    if key != -1:
      key = chr(key)

    if key == '\x1b':
      break

    if key == '1':
      maskgreyscale = colorFilter.greyscale(frame)
      # mask = np.reshape(maskgreyscale, (3, 3))
      cv2.imshow('greyscale', maskgreyscale)
      filter = maskgreyscale
      cv2.imwrite('StoriesDownloads/videoGray.png', maskgreyscale)
    elif key == '2':      
      maskinvertmask = colorFilter.invertmask(frame)
      cv2.imshow('invertmask', maskinvertmask)
      filter = maskinvertmask
      cv2.imwrite('StoriesDownloads/videoRadioactive.png', maskinvertmask)
    elif key == '3':      
      painting = colorFilter.painting(frame)
      cv2.imshow('painting', painting)
      filter = painting
      cv2.imwrite('StoriesDownloads/videoPainting.png', painting)
    elif key == '4':      
      light = colorFilter.light(frame)
      cv2.imshow('light', light)
      filter = light
      cv2.imwrite('StoriesDownloads/videoLight.png', light)
    elif key == '5':      
      rouge = colorFilter.rouge(frame)
      cv2.imshow('rouge', rouge)
      filter = rouge
      cv2.imwrite('StoriesDownloads/videoRouge.png', rouge)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
    
    cv2.imshow("videoFiltros", result)
    out.write(result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cap.release()
  out.release()
  cv2.waitKey(0)
  cv2.destroyAllWindows()

window = tk.Tk()
window.title("InstaKath")
window.wm_iconbitmap('Icons/instakath.ico')
window.geometry("400x600")
window.resizable(True, True)

galleryImage = PhotoImage(file='Icons/gallery.png')
cameraImage = PhotoImage(file='Icons/camera.png')
leaveImage = PhotoImage(file='Icons/logout.png')
logoImage = PhotoImage(file='Icons/InstaKathSmall1.png')

toolbarTop = tk.Label(bg='white', bd=20).pack(side=tk.TOP, fill=tk.X)
label = tk.Button(master=window, image= logoImage, background='white', borderwidth = 0).place(x=5, y=4)
leave = tk.Button(master=window, image= leaveImage, bg='white', borderwidth = 0, command= window.destroy).place(x=350, y=4)


imageFiltro = tk.Button(master=window, text= "Imagem \nFiltros", bg='#6824a3', fg="white", command=lambda: imageFilter(), padx=10, pady=15, justify=CENTER).place(x=80, y=200)
video = tk.Button(master=window, text= "Câmera \nFiltros", bg='#6824a3', fg="white", command=lambda: video(), padx=10, pady=15, justify=CENTER).place(x=80, y=400)
changeCamera = tk.Button(master=window, text= "Mudar \nCâmera", bg='#6824a3', fg="white", command=lambda: changeVideo(), padx=10, pady=15, justify=CENTER).place(x=250, y=200)
cameraFiltroAccessory = tk.Button(master=window, text= "Câmera \nAcessório", fg="white", bg='#6824a3', command=lambda: accessory(), padx=10, pady=15, justify=CENTER).place(x=250, y=400)


window.mainloop()