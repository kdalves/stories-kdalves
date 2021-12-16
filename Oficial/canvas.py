from tkinter import *
from PIL import Image,ImageTk

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("400x600")

#Create a canvas
canvas= Canvas(win, width= 300, height= 300)
canvas.pack()

#Load an image in the script
image = Image.open('StoriesUploads/teste.png')
resizedImage = image.resize((300, 300), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resizedImage)

#Add image to the Canvas Items
canvas.create_image(300,300,anchor=CENTER,image=img)

win.mainloop()