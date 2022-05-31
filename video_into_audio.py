""""
Python video to Audio Converter Project
Details:
        In this project, the user will have to take the following steps
1.click on Browse Button
2.Browse a video file
3.Click on save Button
4.The video file is successfuuly saved """
# Importing the Modules


import moviepy.editor
from tkinter.filedialog import *
from tkinter import *

# Creating the GUI Window
window = Tk()
# Set the size of the tinter window
window.geometry("700x350")
window.title("WEllCome")  # give title to the window
Label(window, text="Video To Audio Converter", bg='orange', font=('Calibri 15')).pack()
# a label
Label(window, text="Choose a file").pack()


# Browse() function
def browse():  # browsing function
    global video  # global variable
    video = askopenfilename()
    video = moviepy.editor.VideoFileClip(video)
    pathlab.config(text=video)  # configure method


def save():
    audio = video.audio  # convert to audio
    audio.write_audiofile("sample.wav")  # save as audio
    Label(window, text="Video Converted into Audio and Saved Successfully", bg='blue',
          font=('Calibri 15')).pack()  # a label


pathlab = Label(window)
pathlab.pack()
# creating buttons
Button(window, text='browse', command=browse).pack()
Button(window, text='SAVE', command=save).pack()

window.mainloop()
