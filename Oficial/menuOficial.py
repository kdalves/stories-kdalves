import tkinter as tk
from tkinter import *
import cv2
from changeCamera import ChangeVideo
from imageFilter import FilterImage
from cameraFiltroAccessory import FilterAccessory

def video():  
  ChangeVideo(cv2.VideoCapture(0))

def accessory():
  FilterAccessory()

def imageFilter():
  FilterImage()

def changeVideo():
  ChangeVideo(cv2.VideoCapture(2))
  
window = tk.Tk()
window.title("InstaKath")
window.wm_iconbitmap('Icons/instakath.ico')
window.geometry("250x500")
window.resizable(True, True)

galleryImage = PhotoImage(file='Icons/gallery.png')
cameraImage = PhotoImage(file='Icons/camera.png')
leaveImage = PhotoImage(file='Icons/logout.png')
hatAccessory = PhotoImage(file='Icons/hat1.png')
changeCameraImage = PhotoImage(file='Icons/changeCamera1.png')
logoImage = PhotoImage(file='Icons/InstaKathSmall1.png')

toolbarTop = tk.Label(bg='white', bd=20).pack(side=tk.TOP, fill=tk.X)
label = tk.Button(master=window, image= logoImage, background='white', borderwidth = 0).place(x=5, y=4)
leave = tk.Button(master=window, image= leaveImage, bg='white', borderwidth = 0, command= window.destroy).place(x=200, y=4)


tk.Button(master=window, image= galleryImage, text= "Imagem \nFiltros", bg='#6824a3', fg="white", command=imageFilter, padx=10, pady=15, justify=CENTER).place(x=100, y=100)
tk.Button(master=window, image= cameraImage, text= "Câmera \nFiltros", bg='#6824a3', fg="white", command=video, padx=10, pady=15, justify=CENTER).place(x=100, y=200)
tk.Button(master=window, image= changeCameraImage, text= "Mudar \nCâmera", bg='#6824a3', fg="white", command=changeVideo, height=48, padx=10, pady=5, justify=CENTER).place(x=100, y=300)
tk.Button(master=window, image= hatAccessory, text= "Câmera \nAcessório", fg="white", bg='#6824a3', command=accessory, height=48 ,padx=10, pady=15, justify=CENTER).place(x=100, y=400)


window.mainloop()