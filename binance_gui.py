import tkinter as tk
top = tk.Tk()

#menu bar at the top of the gui
M = Menu ( master, option, ... )

#drop down button. Use to select which indicators/klines
m = Menubutton ( master, option, ... )
m.grid()
#pop up after indicators are selected, to input the parameters
#used with label
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

#This will be used with Entry, for the option to entry manually, or visually
def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)

root = Tk()
var = DoubleVar()
scale = Scale( root, variable = var )
scale.pack(anchor=CENTER)

button = Button(root, text="Get Scale Value", command=sel)
button.pack(anchor=CENTER)

label = Label(root)
label.pack()


#consider this instead of Menubutton. Undecided on which
#probably menu button.. I think use this to scroll through the results for symbols that returned successful results
Lb1 = Listbox ( top )
Lb1.insert(1,'value')
Lb1.insert(2,'value')
Lb1.pack()


#use to display the graphs and images from the test
# stringvar() is going to be something for the images.. dunno what yet
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("I believe the connection to the image goes here")
label.pack()

#Use this to select through the display for different indicators/the color of the lines for the indicator.
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM 

#button to interact with. Most likely going to use to start the test
B = Button( master, option=value, ... )



top.mainloop()
