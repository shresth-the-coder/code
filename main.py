import tkinter as tk
import gtts
import os

win = tk.Tk()
win.geometry("700x700")
var = tk.StringVar()
ent = tk.Entry(win, textvariable=var)
ent.pack()

words = " teri ma ka bhosda teri ma ki choot mein sau sau laude chutie sale randi ke bacche madhachod tumhari ma ki choot mein kerosene ghusa ke jala denge randi ke bacche saaley bhosadike tumhari ma chod de bhen ke lode tumhari ma ki choot mein barood dal dunga bomb bun jayega tumhari ma ko khule bazar mein chod dunga teri ma aur bahen se kam nahi chala teri dadi ko letana pada madharchod"


def ret():
    a = var.get()
    voice = a+words
    myobj = gtts.gTTS(text=voice, lang='en', tld='co.in', slow=False)
    myobj.save("welcome.mp3")
    os.system("welcome.mp3")

b1 = tk.Button(win, text="submit", command=ret).pack()
win.mainloop()