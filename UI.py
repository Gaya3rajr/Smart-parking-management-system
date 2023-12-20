from tkinter import Tk, Canvas, Frame, BOTH
from tkinter.ttk import Button, Style
from PIL import ImageTk, Image
import os

window = Tk()
window.title("Car Parking Slot Finder")
window.state("zoomed")
window.iconbitmap("./cps.ico")


style = Style()
style.configure("TButton",
                foreground="blue",
                background="blue",
                font=("Helvetica", 25),
                relief="flat",
                padding=(10, 10))

canvas = Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight(), bg="white")
canvas.pack(fill=BOTH, expand=True)

bg_image = Image.open("car.png")
resized_image = bg_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
bg = ImageTk.PhotoImage(resized_image)

canvas.create_image(0, 0, image=bg, anchor='nw')

def resize_image(e):
    global bg, resized_image
    resized_image = bg_image.resize((e.width, e.height))
    bg = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(background, image=bg)


    canvas.config(width=e.width, height=e.height)


    canvas.coords(background, e.width // 2, e.height // 2)

window.bind("<Configure>", resize_image)

def check_slots():

    print("Slots checked!")
    os.system("python main.py")

button_frame = Frame(window)
button_frame.pack(pady=(0, 50))

check_button = Button(button_frame, text="Check Slots", command=check_slots, style="TButton")
check_button.pack()


button_frame.place(relx=0.2, rely=0.6, anchor="w")


background = canvas.create_image(window.winfo_screenwidth() // 2, window.winfo_screenheight() // 2, image=bg)

window.mainloop()
