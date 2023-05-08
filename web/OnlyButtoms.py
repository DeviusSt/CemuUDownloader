from tkinter import *
import webbrowser

root['bg'] = '#fafafa'
root.title('CEMUUCraker')
root.wm_attributes('-alpha', 100.0)
root.geometry('300x250')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack()

frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)

title = Label(frame, text='Welcome to Cemu Utilits Craked!', bg='white', font=40)
title.pack()
btn = Button(frame, text='WiiUApps2Cemu EU', bg='light gray')
btn.pack()
btn = Button(frame, text='WiiUApps2Cemu USA', bg='light gray')
btn.pack()
title = Label(frame, text='Splatoon NoMotion', bg='white', font=40)
title.pack()
btn = Button(frame, text='Splatoon NoMotion', bg='light gray')
btn.pack()
title = Label(frame, text='Devoloper', bg='white', font=40)
title.pack()
btn = Button(frame, text='✈ Telegram', bg='light gray')
btn.pack()
btn = Button(frame, text='📦️ GitHub', bg='light gray')
btn.pack()

root.mainloop()
