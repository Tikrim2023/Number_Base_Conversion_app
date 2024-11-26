from tkinter import *
from tkinter import ttk

#colours
co0 = "#ffffff" #white
co1 = "#000000"  #black
co2 = "#7DB1FA"  #blue
co3 = "#FA7516"  #orange
co4 = "#C3DEF7"  #lightblue

window = Tk()
window.title('')
window.geometry("350x310")
window.resizable(width=False,height=False)
window.configure(bg=co0)

style = ttk.Style()
style.theme_use('clam')

ttk.Separator(window,orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=190)

def convert():
    def number_to_decimal(number, base):


        decimal = int(number, base)

        binary = bin(decimal)
        octal = oct(decimal)
        hexadecimal = hex(decimal)

    

        l_binary["text"] = str(binary[2:])
        l_octal["text"] = str(octal[2:])
        l_decimal["text"] = str(decimal)
        l_hexadecimal["text"] = str(hexadecimal[2:])
 

    base = combo.get()
    number = e_value.get()

    if base == "BINARY":
       base = 2
    elif base == "OCTAL":
       base = 8
    elif base == "DECIMAL":
        base = 10
    else:
       base = 16

    number_to_decimal(number,base)


    
#frames
frame_up = Frame(window, width=400, height=60, bg=co0, pady=0, padx=10)
frame_up.grid(row=1,column=0)

frame_down = Frame(window,width=400, height=300, bg=co0, pady=12, padx=0)
frame_down.grid(row=2,column=0)

#App Name
app_name = Label(frame_up, text="Numeric Base Converter", anchor="center", font=("System 20"), bg=co2, fg=co1)
app_name.place(x=3, y=15)

#List for the bases
bases = ["BINARY", "OCTAL", "DECIMAL", "HEXADECIMAL"]

combo = ttk.Combobox(frame_down, width=12, justify="center", text="co1",font=("Ivy 12 bold"))
combo["values"] = (bases)
combo.place(x=35, y=10)

#entry part(user input box)
e_value = Entry(frame_down, width=10, justify="center", font= ("", 13), highlightthickness=1, relief=SOLID)
e_value.place(x=160, y=10)

b_converter = Button(frame_down,text="CONVERT", command=convert, height=1, bg=co1,  fg=co0, font=("Ivy 8 bold"), relief=RAISED, overrelief=RIDGE)
b_converter.place(x=255, y=10)

l_binary = Label(frame_down, text="BINARY", bg=co2, fg=co1, width=12, height=1, anchor="nw", font=("Verdana 13"))
l_binary.place(x=35, y=60)
l_binary = Label(frame_down, text="",  fg=co1, width=12, height=1, anchor="nw", font=("Verdana 13"))
l_binary.place(x=170, y=60)

l_decimal = Label(frame_down, text="DECIMAL", bg=co2, fg=co1, width=12, height=1, anchor="nw", font=("Verdana 13"))
l_decimal.place(x=35, y=100)
l_decimal = Label(frame_down, text="",  fg=co1, width=12, height=1, anchor="nw", font=("Verdana 13"))
l_decimal.place(x=170, y=100)

l_octal = Label(frame_down, text="OCTAL", bg=co2, fg=co1, width=12, height=1, anchor="nw", font=("Verdana 13"))
l_octal.place(x=35, y=140)
l_octal = Label(frame_down, text="", fg=co1, width=12, height=1, anchor="nw", font=("Verdana 13"))
l_octal.place(x=170, y=140)

l_hexadecimal = Label(frame_down, text="HEXADECIMAL", bg=co2, fg=co1, width=12, height=1, anchor="nw", font=("Verdana 13"))
l_hexadecimal.place(x=35, y=180)
l_hexadecimal = Label(frame_down, text="",  fg=co1, width=12, height=1, anchor="nw", font=("Verdana 13"))
l_hexadecimal.place(x=170, y=180)

window.mainloop()
