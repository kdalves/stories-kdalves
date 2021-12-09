import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
import cv2
import colorFilter
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
    
    cv2.imshow("videoFiltros", filter)
    out.write(filter)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cap.release()
  out.release()
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def open_file():
  global imageOpen
  imageOpen = filedialog.askopenfilename(
    initialdir = 'D:\Projetos\stories-kdalves\StoriesUploads',
    filetypes=[("Text Files", "*.png, *.jpg"), ("All Files", "*.*")]
  )
  


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

# image = cv2.imread('Icons/background.png')
image = videoRecord if videoRecord else cv2.imread('Icons/background.png')
b,g,r = cv2.split(image)
img = cv2.merge((r,g,b))
im = Image.fromarray(img)
img_resized=im.resize((350,400))
imgtk = ImageTk.PhotoImage(image=img_resized)

imageSpace = tk.Label(image= imgtk, borderwidth = 0).place(x=25, y=80)

image = tk.Button(master=window, image= galleryImage, bg='#6824a3', borderwidth = 0, command=lambda: open_file(), padx=10, pady=15, justify=CENTER).place(x=100, y=500)
video = tk.Button(master=window, image= cameraImage , bg='#6824a3', borderwidth = 0, command=video, padx=10, pady=15, justify=CENTER).place(x=250, y=500)
# video = tk.Button(master=window, image= cameraImage , bg='#6824a3', borderwidth = 0, command=vw, padx=10, pady=15, justify=CENTER).place(x=250, y=500)

window.mainloop()