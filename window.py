from tkinter import *
import pywhatkit


def send():
    phone = entry0.get()
    msg = entry2.get()
    Hr, Min = entry1.get().split(" ")
    Hr = int(Hr)
    Min = int(Min)
    # increase the waittime if your internet connection is slow
    waittime = 15  # in seconds
    pywhatkit.sendwhatmsg(phone, msg, Hr, Min, waittime, True, 5)


window = Tk()
window.title("Whatsapp Scheduler")

photo = PhotoImage(file=f"Jb studios Logo.png")
window.iconphoto(False, photo)

window.geometry("600x752")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=752,
    width=600,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

entry0_img = PhotoImage(file=f"textbox0.png")
entry0_bg = canvas.create_image(
    301.5, 344.5,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    font=("Inter-Medium", int(15.0)),
    bg="#ece5dd",
    highlightthickness=0)

entry0.place(
    x=83.0, y=316,
    width=437.0,
    height=55)

entry1_img = PhotoImage(file=f"textbox1.png")
entry1_bg = canvas.create_image(
    301.5, 551.5,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    font=("Inter-Medium", int(15.0)),
    bg="#ece5dd",
    highlightthickness=0)

entry1.place(
    x=83.0, y=523,
    width=437.0,
    height=55)

entry2_img = PhotoImage(file=f"textbox2.png")
entry2_bg = canvas.create_image(
    301.5, 446.5,
    image=entry2_img)

entry2 = Entry(
    font=("Inter-Medium", int(15.0)),
    bd=0,
    bg="#ece5dd",
    highlightthickness=0)

entry2.place(
    x=83.0, y=418,
    width=437.0,
    height=55)

canvas.create_text(
    156.5, 299.5,
    text="Phone No.",
    fill="#848484",
    font=("Inter-Medium", int(24.0)))

canvas.create_text(
    234.5, 504.5,
    text="Time(Hours, Minutes)",
    fill="#848484",
    font=("Inter-Medium", int(24.0)))

canvas.create_text(
    146.5, 398.5,
    text="Message",
    fill="#848484",
    font=("Inter-Medium", int(24.0)))

img0 = PhotoImage(file=f"send.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=send,
    relief="flat")

b0.place(
    x=239, y=665,
    width=122,
    height=41)

background_img = PhotoImage(file=f"background1.png")
background = canvas.create_image(
    490.0, 131.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()
