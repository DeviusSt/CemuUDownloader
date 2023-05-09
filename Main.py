from tkinter import *
import webbrowser

root = Tk()

def btn_click():
    webbrowser.open('https://github.com/SynthouS/WiiUScreen2Cemu/releases/download/apps/WiiUScreen2Cemu.zip', new=2)

def btn_click2():
    webbrowser.open('https://github.com/SynthouS/WiiUScreen2Cemu/releases/download/v5.5.2/WiiUApps2CemuUSA.zip', new=2)

def btn_click3():
    webbrowser.open('https://github.com/TheSipod/Splatoon-NoMotion/files/9280968/SplatoonFIX.zip', new=2)

def btn_click4():
    webbrowser.open('https://t.me/SynthouS', new=2)

def btn_click5():
    webbrowser.open('https://github.com/SynthouS', new=2)

def btn_click8():
    webbrowser.open('https://github.com/FailedShack/USBHelperLauncher/releases/download/1.0/USBHelperLauncher-1.0.zip', new=2)

def btn_click6():
    webbrowser.open('https://www.marcrobledo.com/savegame-editors/zelda-botw/', new=2)

def btn_click7():
    webbrowser.open('https://github.com/HiddenRamblings/TagMo/releases/download/master/TagMo-dc93938-github-release-signed.apk', new=2)

def btn_click9():
    webbrowser.open('https://github.com/jonbarrow/CemUI/releases/download/v2.3.3/CemUI.Setup.2.3.3.exe', new=2)

root['bg'] = '#fafafa'
root.title('CEMUUDownloader')
root.wm_attributes('-alpha', 90.0)
root.geometry('300x520')
root.iconbitmap("icon.ico")

root.resizable(width=TRUE, height=True)

canvas = Canvas(root, height=680, width=790)
canvas.pack()

frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)

title = Label(frame, text='Welcome to Cemu utilits Downloader!', bg='white', font=40)
title.pack()
btn = Button(frame, text='WiiUApps2Cemu EU', bg='light gray', command=btn_click)
btn.pack()
btn = Button(frame, text='WiiUApps2Cemu USA', bg='light gray', command=btn_click2)
btn.pack()
title = Label(frame, text='Splatoon NoMotion', bg='white', font=40)
title.pack()
btn = Button(frame, text='Splatoon NoMotion', bg='light gray', command=btn_click3)
btn.pack()
title = Label(frame, text='USBHelper', bg='white', font=40)
title.pack()
btn = Button(frame, text='USBHelper 1.0', bg='light gray', command=btn_click8)
btn.pack()
title = Label(frame, text='Other utilits', bg='white', font=40)
title.pack()
btn = Button(frame, text='Save Editor ZeldaBoth', bg='light gray', command=btn_click6)
btn.pack()
btn = Button(frame, text='TagMO', bg='light gray', command=btn_click7)
btn.pack()
btn = Button(frame, text='CemUI', bg='light gray', command=btn_click9)
btn.pack()
title = Label(frame, text='Devoloper', bg='white', font=40)
title.pack()
btn = Button(frame, text='✈ Telegram', bg='light gray', command=btn_click4)
btn.pack()
btn = Button(frame, text='📦️ GitHub', bg='light gray', command=btn_click5)
btn.pack()

root.mainloop()