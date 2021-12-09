import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
import cv2
import main as m

imageOpen = None

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

image = cv2.imread('Icons/background.png')
b,g,r = cv2.split(image)
img = cv2.merge((r,g,b))
im = Image.fromarray(img)
img_resized=im.resize((350,400))
imgtk = ImageTk.PhotoImage(image=img_resized)

imageSpace = tk.Label(image= imgtk, borderwidth = 0).place(x=25, y=80)

back = tk.Button(master=window, text='voltar', bg='#6824a3', borderwidth = 0, command=lambda: m.main(), padx=10, pady=15, justify=CENTER).place(x=100, y=500)

window.mainloop()