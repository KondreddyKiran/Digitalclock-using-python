import tkinter as ui
import time
window = ui.Tk()
def update_clock():
    hours= time.strftime("%H")
    minutes= time.strftime("%M")
    Seconds= time.strftime("%S")
    am_pm= time.strftime("%p")
    time_text= hours +":"+ minutes +":"+Seconds +" "+ am_pm
    digital_clock_label.config(text= time_text)
    digital_clock_label.after(1000,update_clock)
digital_clock_label = ui.Label(window,text=" 00:00:00",font="Helvetica 100 bold")
digital_clock_label.pack()
update_clock()
window.mainloop()