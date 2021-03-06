from os import stat
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
            statusbar['text'] = 'Music is playing'
        except:
            tkinter.messagebox.showerror('File Error', 'File Not Found')
    else:
        mixer.music.unpause()
        statusbar['text'] = 'Music is resumed'

def stop_music():
    """stopping the music"""
    mixer.music.stop()
    statusbar['text'] = 'Music stopped'

def set_volume(value):
    """setting the volume"""
    volume = int(value)/100
    mixer.music.set_volume(volume)

def pause_music():
    """pausing the music"""
    global paused
    paused = True    
    mixer.music.pause()
    statusbar['text'] = 'Music paused'

def rewind_music():
    """rewind music"""
    play_music()
    statusbar['text'] = 'Music is rewinded'

frame = Frame(window)
frame.pack(padx=10, pady=10)

# adding the button photos
photo = PhotoImage(file='Media//play.png')
# photoLabel = Label(window, image=photo, height=100, width=100)
# photoLabel.pack()
playButton = Button(frame, image=photo, command=play_music)
playButton.grid(row=0, column=0, padx=10)

#stop button
stopPhoto = PhotoImage(file='Media//stop.png')
stopButton = Button(frame, image=stopPhoto, height=50, width=50, command=stop_music)
stopButton.grid(row=0, column=1, padx=10)

#pause button
pausePhoto = PhotoImage(file='Media//pause.png')
pauseBtn = Button(frame, image=pausePhoto, command=pause_music)
pauseBtn.grid(row=0, column=2, padx=10)

#bottom frame
bottomframe = Frame(window)
bottomframe.pack()

# rewind button
rewindPhoto = PhotoImage(file='Media//rewind.png')
rewindButton = Button(bottomframe, image=rewindPhoto, command=rewind_music)
rewindButton.grid(row=0, column=0, padx=10)
 
# volume scale
scale = Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(70) #the value being set is pass to set_volume func
scale.grid(row=0, column=1)

# status bar
statusbar = Label(window, text='Keep enjoying the music', relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X) #fill all spaces from left and right


# close window
window.mainloop()