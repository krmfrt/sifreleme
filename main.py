from tkinter import *
from PIL import ImageTk, Image
from cryptography.fernet import Fernet
from tkinter import messagebox
import base64, hashlib

main_window = Tk()
main_window.title("Mesaj Şifreleme")
main_window.geometry("600x820")

my_frame= Frame(main_window)
my_frame.pack(pady=7000, padx=7000)



img = Image.open(r"C:\Users\Keko\Downloads\tps.jpg")
img=img.resize((150, 200))
image_icon= Image.open(r"C:\Users\Keko\Downloads\icon.png")
image_icon1= ImageTk.PhotoImage(image_icon)

main_window.iconphoto(False, image_icon1)

img1 = ImageTk.PhotoImage(img)
main_label = Label(image=img1)
main_label.place(x=220, y=20)

title_label = Label(text="Kayıt Başlığını Giriniz!")
title_label.place(x=180, y=230)
title_label.config(font=("Helvetica ", 18, "bold"))

title_entry = Entry()
title_entry.place(x=180, y=265, width=250, height=20)



title_label = Label(text="Mesajınızı Giriniz!")
title_label.place(x=200, y=285)
title_label.config(font=("Helvetica ", 18, "bold"))

text = Text()
text.place(x=100, y=350, height=300, width=400)

sifre_label = Label(text="Şifrenizi Giriniz!")
sifre_label.place(x=200, y=645)
sifre_label.config(font=("Helvetica ", 18, "bold"))

sifre_entry = Entry()
sifre_entry.place(x=180, y=690, width=250, height=20)






def encryp() :
    global sifre_entry
    a= title_entry.get()
    passcode = sifre_entry.get()
    key = base64.b64encode(f"{passcode:<32}".encode("utf-8"))
    fernet = Fernet(key=key)
    mesaj = text.get(1.0, END)
    encrypp = fernet.encrypt(mesaj.encode("utf-8"))
    text.delete(1.0, END)
    text.insert(END, encrypp)
    result=encrypp.decode("utf-8")

    with open('log.txt', 'a') as f:
        f.write(f"{a}")
        f.write('\n')
        f.write(f"{result}")
        f.write('\n')
        f.close()


def decryp() :
    mesaj = text.get(1.0, END)
    global sifre_entry
    passcode = sifre_entry.get()
    key = base64.b64encode(f"{passcode:<32}".encode("utf-8"))
    fernet = Fernet(key=key)
    mesaj = text.get(1.0, END)
    decrypp = fernet.decrypt(mesaj.encode("utf-8"))
    text.delete(1.0, END)
    text.insert(END, decrypp)

def cls():
    text.delete(1.0, END)
    sifre_entry.delete(0, END)
    title_entry.delete(0, END)


encryp_button = Button()
encryp_button.config(font=("Times New Roman", 8) )
encryp_button.config(text="Şifrele & Kaydet", command=encryp)
encryp_button.place(x=240, y=720, width=100, height=20)

dencryp_button = Button()
dencryp_button.config(font=("Times New Roman", 8) )
dencryp_button.config(text="Mesajı Çözümle", command=decryp)
dencryp_button.place(x=240, y=750, width=100, height=20)


cls_button = Button()
cls_button.config(font=("Times New Roman", 8) )
cls_button.config(text="Ekranı Temizle", command=cls)
cls_button.place(x=240, y=780, width=100, height=20)





main_window.mainloop()
