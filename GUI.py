from tkinter import *
from tkinter import ttk

from pfa_list import *
from text2int import *
from Bike_df import *

def on_click(event):
    global myLabel
    province = filter_province(combo_p.get())
    feature = filter_feature(combo_f.get())
    activity = filter_activity(combo_a.get())
    recommended = recommendation(bike_place, result, int(province), int(feature), int(activity))
    new_text = "Recommended location for biking: "+str(recommended)
    myLabel = Label(window, text=new_text, bg="#00FFFF", fg="#00008B")
    myLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
    return

def del_label(event):
    myLabel.place_forget()
    return

window = Tk()
window.title("Let's Bike!")
window.iconbitmap(r"2972185.ico")
window.geometry("1500x800")
window.config(bg="#00FFFF")
window.option_add("*Font", "Arial 20")

Label(window, text="Which province would you like to go biking?", bg="#00FFFF", fg="#00008B").pack(side=TOP)
combo_p =ttk.Combobox(window, values=province_list, state="readonly", width=50)
combo_p.pack(side=TOP)

Label(window, text="What kind of place would you like to bike?", bg="#00FFFF", fg="#00008B").pack(side=TOP)
combo_f =ttk.Combobox(window, values=feature_list, state="readonly", width=50)
combo_f.pack(side=TOP)

Label(window, text="What kind of activity will you be doing?", bg="#00FFFF", fg="#00008B").pack(side=TOP)
combo_a =ttk.Combobox(window, values=activity_list, state="readonly", width=50)
combo_a.pack(side=TOP)

btn1 = Button(window, text="SUBMIT")
btn1.pack(side=TOP)
btn1.bind("<Button-1>", on_click)

btn2 = Button(window, text="CLEAR")
btn2.pack(side=TOP)
btn2.bind("<Button-1>", del_label)

window.mainloop()