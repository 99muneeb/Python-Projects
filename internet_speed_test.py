from tkinter import *
import speedtest


def SpeedCheck():
    """
Speed Tasting funcions
    """
    sp1 = speedtest.Speedtest()
    sp1.get_servers()
    down = str(round(sp1.download() / (10 ** 6), 3)) + "Mpbs"
    up = str(round(sp1.upload() / (10 ** 6), 3)) + "Mpbs"
    lab_down.config(text=down)
    lab_up.config(text=up)


if __name__ == '__main__':
    sp = Tk()
    sp.title("Internet Speed Test")
    sp.geometry("500x750")
    sp.config(bg="Blue")
    lab = Label(sp, text="Internet Speed Test", font=("Time New Roman", 30, "bold"), bg="Blue", fg="white")
    lab.place(x=60, y=40, height=50, width=380)
    # Downloading sped
    lab = Label(sp, text="Download Speed", font=("Time New Roman", 30, "bold"))
    lab.place(x=60, y=130, height=50, width=380)

    lab_down = Label(sp, text="00", font=("Time New Roman", 30, "bold"))
    lab_down.place(x=60, y=200, height=50, width=380)

    # uploading speed
    lab = Label(sp, text="Upload Speed", font=("Time New Roman", 30, "bold"))
    lab.place(x=60, y=290, height=50, width=380)
    lab_up = Label(sp, text="00", font=("Time New Roman", 30, "bold"))
    lab_up.place(x=60, y=360, height=50, width=380)

    button = Button(sp, text="Check Speed", font=("Time New Roman", 30, "bold"), relief=RAISED, bg="Red",
                    command=SpeedCheck)
    button.place(x=60, y=460, height=50, width=380)
    sp.mainloop()
