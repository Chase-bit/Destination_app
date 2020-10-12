import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk 
import urllib
import requests
import config
HEIGHT = 500
WIDTH = 600




def get_location(place):
    API_KEY = config.API_KEY_SOURCE
    get_image = 'https://maps.googleapis.com/maps/api/streetview?'
    parameters = {'location': place, 'size': '400x400', 'key': API_KEY}
    response = requests.get(get_image, params=parameters)
    file = open('response_img.png', 'wb')
    file.write(response.content)
    file.close()
    load = Image.open('response_img.png')
    render = ImageTk.PhotoImage(load)
    img = tk.Label(lower_frame, image = render)
    img.image = render
    img.place(x=1, y=1)

    

# Mainloop
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

file = tk.PhotoImage(file='background.png')
image = tk.Label(root, image=file)
image.place(relwidth=1, relheight=1)


# Text label, button and entry field
label = tk.Label(root, text='Enter your Destination')
label.place(x=230, y=20)


w = tk.Button(root, font='Courier', text='Get picture', command=lambda: get_location(entry.get()))
w.place(height=20, width=200, relx=0.33, rely=0.2)

entry = tk.Entry(root, bd=1)
entry.place(height=30, width=300, relx=0.25, rely=0.1)


lower_frame = tk.Frame(root, bd=1)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


root.mainloop()

