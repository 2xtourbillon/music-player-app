from tkinter import *
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox

# initialize the mixer and window
mixer.init()

window = Tk()
window.geometry('300x350')
window.title('Python music Player')

def browse_file():
    """browse file dialog in menu"""
    global filename
    filename = filedialog.askopenfilename()

def help_me():
    """adding help message box"""
    tkinter.messagebox.showinfo('Help','How amazing it is')

# adding a menu/submenu
menubar = Menu(window) # menu
submenu = Menu(menubar, tearoff=0) # submenu
window.config(menu=menubar)

# adding items to menu
menubar.add_cascade(label='File', menu=submenu)
submenu.add_command(label='Open', command=browse_file)
submenu.add_command(label='Exit', command=window.destroy)

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About Us", menu=submenu)
submenu.add_cascade(label='Help', command=help_me)

textLabel = Label(window, text="This is a Play Button")
textLabel.pack()

LionKing = 'Media//The Lion Sleeps Tonight.mp3'
StarWars = 'Media//Star Wars Theme Song By John Williams.ogg'
ACDC = 'Media//You shook me.mp3'
Boston = 'Media//More than a feeling.mp3'

def play_music():
    """loading and playing music"""
    try:
        paused #check if pause button is clicked
    except:
        try:
            mixer.music.load(filename)
            mixer.music.play()
        except:
            tkinter.messagebox.showerror('File Error', 'File Not Found')
    else:
        mixer.music.unpause()

def stop_music():
    """stopping the music"""
    mixer.music.stop()

def set_volume(value):
    """setting the volume"""
    volume = int(value)/100
    mixer.music.set_volume(volume)

def pause_music():
    """pausing the music"""
    global paused
    paused = True    
    mixer.music.pause()

# adding the button photos
photo = PhotoImage(file='Media//Logo.png')
# photoLabel = Label(window, image=photo, height=100, width=100)
# photoLabel.pack()
playButton = Button(window, image=photo, command=play_music)
playButton.pack()

#stop button
stopPhoto = PhotoImage(file='Media//stop.png')
stopButton = Button(window, image=stopPhoto, height=50, width=50, command=stop_music)
stopButton.pack()

#pause button
pausePhoto = PhotoImage(file='Media//pause.png')
pauseBtn = Button(window, image=pausePhoto, command=pause_music)
pauseBtn.pack()

# volume scale
scale = Scale(window, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(70) #the value being set is pass to set_volume func
scale.pack()



# close window
window.mainloop()