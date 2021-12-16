import tkinter as tk
from PIL import Image, ImageTk
import cv2
# from cameraFiltroAccessoryTeste import FiltroAcessory
import numpy as np

cascadeFace = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class MainVideo():
  def __init__(self, window, cap):
  # def __init__(self, window, cap, kindVideo):
    self.window = window
    self.cap = cap
    self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    self.interval = 20
    # if kindVideo == 'accessor'
    # self.FiltroAcessory(cap)
    cnt=0
    accessory = 0

    while cnt<500:
        _, img = cap.read()
        
        grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


        key = cv2.waitKey(10)

        if key != -1:
          key = chr(key)

        if key == '\x1b':
          break
      
        if key == '1':
          accessory = 1 
          # cv2.imwrite('StoriesDownloads/graduate.png', final)
        elif key == '2':
          accessory = 2
        elif key == '3':
          accessory = 3
        elif key == '4':
          accessory = 4
        elif key == '5':
          accessory = 5
        
        self.final = self.detection(grayscale, img, accessory)

        if cv2.waitKey(1) & 0xFF == ord('q'):
          break 

        # if final is not None:
          # cv2.imshow('Video', final) 
          # out.write(final)

        cnt+=1
    cap.release()
    # out.release()
    # cv2.destroyAllWindows() 
    self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
    self.canvas.pack()
    self.update_image()

  def detection(self, grayscale, img, accessory):    
    face = cascadeFace.detectMultiScale(grayscale, 1.3, 5)

    for (xface, yface, wface, hface) in face:
      if accessory == 1:
        imgHeadAccessory= cv2.imread('Filters/graduate.png',-1)
      elif accessory == 2:
        imgHeadAccessory= cv2.imread('Filters/devil.png',-1)
      elif accessory == 3:
        imgHeadAccessory= cv2.imread('Filters/coroa.png',-1)    
      elif accessory == 4:
        imgHeadAccessory= cv2.imread('Filters/santa.png',-1)
      else:
        imgHeadAccessory= cv2.imread('Filters/sombrero.png',-1)
          
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
          
      return self.img

  def update_image(self):
      self.image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB)
      self.image = Image.fromarray(self.image)
      self.image = ImageTk.PhotoImage(self.image)
      self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
      self.window.after(self.interval, self.update_image)
