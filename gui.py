from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from gen import *
from config import *
import pyperclip


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_entry_1(event):
    name = entry_1.get()
    entry_1['text'] = name
    hashed_password = hash_generator(password=name,salt_lenght=20,time=time, memory_c=memory*time)
    hashed_password_str = hashed_password.decode('utf-8')
    
    result_label = Label(window, text=hashed_password, bg="#181818", fg="#FFFFFF",font=("MontserratRoman Medium", 10 * -1))
    result_label.place(x=0, y=220)
    
    copy_button = Button(window, text="Copier", command=lambda: pyperclip.copy(hashed_password_str))
    copy_button.place(x=240, y=140)  # Spécifiez les coordonnées du bouton
  
    print(hashed_password)

def on_entry_2(event):
    pass
    
def on_button_click():
    seq = rdm_str_generator(20)
    hashed_password = hash_generator(password=seq,salt_lenght=20,time=time, memory_c=memory*time)
    hashed_password_str = hashed_password.decode('utf-8')
    
    result_label3 = Label(window, text=hashed_password_str, bg="#181818", fg="#FFFFFF",font=("MontserratRoman Medium", 10 * -1))
    result_label3.place(x=0, y=520)
    
    result_label3_bis = Label(window, text=seq, bg="#181818", fg="green",font=("MontserratRoman Medium", 18 * -1))
    result_label3_bis.place(x=0, y=540)
    
    copy_button = Button(window, text="Copier", command=lambda: pyperclip.copy(hashed_password_str))
    copy_button.place(x=620, y=520)

    copy_button = Button(window, text="Copier", command=lambda: pyperclip.copy(seq))
    copy_button.place(x=320, y=540)
    
    desc_label= Label(window, text="Unhashed Password", bg="#181818", fg="red",font=("MontserratRoman Medium", 16 * -1))
    desc_label.place(x=700, y=550)
    
    desc_label2= Label(window, text="Hashed Password", bg="#181818", fg="red",font=("MontserratRoman Medium", 16 * -1))
    desc_label2.place(x=700, y=515)
    
def verify_button():
    unhashed_password = entry_2.get()
    hashed_password = entry_3.get()
    is_correct = hash_verify(str.encode(hashed_password),unhashed_password)
    if is_correct != True:
        is_correct == False
        result_label4 = Label(window, text="False", bg="#181818", fg="red",font=("MontserratRoman Medium", 20 * -1))
    else:
        result_label4 = Label(window, text="True", bg="#181818", fg="green",font=("MontserratRoman Medium", 20 * -1))
    result_label4.place(x=700, y=380)

window = Tk()

window.geometry("950x600")
window.configure(bg = "#181818")


canvas = Canvas(
    window,
    bg = "#181818",
    height = 600,
    width = 950,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    211.0,
    13.0,
    anchor="nw",
    text="Safe Password Generator",
    fill="#FFFFFF",
    font=("MontserratRoman Bold", 40 * -1)
)

canvas.create_text(
    11.0,
    127.0,
    anchor="nw",
    text="Secure yours",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 36 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=on_button_click,
    relief="flat",
    bg="#1E1E1E"
)
button_1.place(
    x=343.0,
    y=128.0,
    width=264.0,
    height=44.0
)

canvas.create_text(
    660.0,
    127.0,
    anchor="nw",
    text="Verify",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 36 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    150.5,
    193.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=21.0,
    y=180.0,
    width=259.0,
    height=24.0
)
entry_1.bind('<Return>', on_entry_1)

#########################################

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    799.5,
    193.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=670.0,
    y=180.0,
    width=259.0,
    height=24.0
)
entry_2.insert(0, "Unhashed password")


##################################

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_3 = canvas.create_image(
    799.5,
    250.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=669.5,
    y=238.0,
    width=259.0,
    height=24.0
)
entry_3.insert(0, "Hashed password")


################################################

button_verify = Button(
    text="Verify",
    borderwidth=0,
    highlightthickness=0,
    command=verify_button,
    relief="flat",
    bg="#5B2727",
    font=("MontserratRoman Bold", 36 * -1),
    fg='white'
)

button_verify.place(
    x=668.0,
    y=300.0,
    width=250.0,
    height=40.0
)

window.resizable(False, False)
window.mainloop()
