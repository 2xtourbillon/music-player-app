from tkinter import *
from pygame import mixer

# initialize the mixer and window
mixer.init()
window = Tk()

window.geometry('300x350')
window.title('Python music Player')

textLabel = Label(window, text="This is a Play Button")
textLabel.pack()

LionKing = 'Media//The Lion Sleeps Tonight.mp3'
StarWars = 'Media//Star Wars Theme Song By John Williams.ogg'
ACDC = 'Media//You shook me.mp3'
Boston = 'Media//More than a feeling.mp3'

def play_music():
    """loading and playing music"""
    mixer.music.load(LionKing)
    mixer.music.play()
    mixer.music.queue(ACDC)

def stop_music():
    """stopping the music"""
    mixer.music.stop()

def set_volume(value):
    """setting the volume"""
    volume = int(value)/100
    mixer.music.set_volume(volume)

photo = PhotoImage(file='Media//Logo.png')
# photoLabel = Label(window, image=photo, height=100, width=100)
# photoLabel.pack()
playButton = Button(window, image=photo, command=play_music)
playButton.pack()

#stop button
stopPhoto = PhotoImage(file='Media//stop.png')
stopButton = Button(window, image=stopPhoto, height=50, width=50, command=stop_music)
stopButton.pack()

# volume scale
scale = Scale(window, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(70) #the value being set is pass to set_volume func
scale.pack()

window.mainloop()