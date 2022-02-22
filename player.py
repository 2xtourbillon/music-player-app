from tkinter import *
from pygame import mixer

window = Tk()

mixer.init()

window.geometry('300x250')
window.title('Python music Player')

textLabel = Label(window, text="This is a Play Button")
textLabel.pack()

LionKing = 'Media//The Lion Sleeps Tonight.mp3'
StarWars = 'Media//Star Wars Theme Song By John Williams.ogg'
ACDC = 'Media//You shook me.mp3'
Boston = 'Media//More than a feeling.mp3'

def play_music():
    mixer.music.load(ACDC)
    mixer.music.play()



photo = PhotoImage(file='Media//Logo.png')
# photoLabel = Label(window, image=photo, height=100, width=100)
# photoLabel.pack()
playButton = Button(window, image=photo, command=play_music)
playButton.pack()

window.mainloop()