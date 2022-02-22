from tkinter import *

window = Tk()
window.geometry('300x300')
window.title('Python music Player')

textLabel = Label(window, text="This is a Play Button")
textLabel.pack()

photo = PhotoImage(file='pensiveRobot.png')
photoLabel = Label(window, image=photo)
photoLabel.pack()







window.mainloop()