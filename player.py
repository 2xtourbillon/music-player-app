from tkinter import *
from pygame import mixer

window = Tk()

mixer.init()

window.geometry('300x300')
window.title('Python music Player')

textLabel = Label(window, text="This is a Play Button")
textLabel.pack()

LionKing = 'The Lion Sleeps Tonight.mp3'
StarWars = 'Star Wars Theme Song By John Williams.ogg'
ACDC = 'You shook me.mp3'
Boston = 'More than a feeling.mp3'

def play_music():
    mixer.music.load(ACDC)
    mixer.music.play()



photo = PhotoImage(file='pensiveRobot.png')
# photoLabel = Label(window, image=photo, height=100, width=100)
# photoLabel.pack()
playButton = Button(window, image=photo, command=play_music)
playButton.pack()

window.mainloop()