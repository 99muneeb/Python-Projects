'''
Python Youtube Video Downloader Project Details
In this project, we are going to create a GUI Window that will have the following widgets:

1. An Entry Box – To enter the link of a YouTube video.

2. Checkboxes – To check the quality/resolution of the video.

3. Button – To download the video.

Using this project, you can download a video from YouTube in any quality that you desire.
'''

'''teps to Build the Project
Let us look at the steps to build the YouTube Video Downloader Project:

1. Importing the Modules

2. Creating the GUI and adding components.

3. Download Function
'''
#importing modules
from tkinter import *
from pytube import YouTube

# Create an instance of tkinter frame or window
# Set the size of the tkinter window
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Any-youtube video downloader")

#Download Function:
# title() used to give the title of window
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()


# Create Field to Enter Link
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

# Create Function to Start Downloading
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()
# window.mainloop()