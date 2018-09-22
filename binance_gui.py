from tkinter import *
from tkinter import ttk

def indicator_widget(event):
    top_0 = Tk()
#Indicator entry box, and button to run test
    Indicator= Label(top_0, text= 'Indicators')

    #Nest the button to run this to pull up another window prompting the parameters for selected indicators
    select_btn= Button(top_0, text='Select Indicators')
    ind_entry = Entry(top_0)
    ind_entry.bind('<Return>', set_inds)
    select_btn.bind('<Button-1>', set_inds)
    def set_inds(event):
        top_2 = Tk()
        # Indicator scroll bar/ listbox
        lb = Listbox(top_2, height=5)
        yscroll = Scrollbar(top_2, orient=VERTICAL)
        lb['yscrollcommand'] = yscroll.set
        yscroll['command'] = lb.yview

        Indicators = ['Commodity Channel Index', 'Parabolic SAR',
                      'Money Flow Index', 'Bolinger Bands', 'StochRSI'
                      'STOCH', 'EMA', 'RSI']
        for indicator in Indicators:
            lb.insert(0, indicator)

        lb.grid(row=0, column=2, rowspan=2, sticky=N + S)
        yscroll.grid(row=0, column=1, rowspan=2, sticky=N + S + E)
   
    #Indicator scroll bar/ listbox
    lb= Listbox(top_0, height=5)
    yscroll= Scrollbar(top_0, orient= VERTICAL)
    lb['yscrollcommand'] = yscroll.set
    yscroll['command'] = lb.yview


    Use_lab=Label(top_0, text= 'Use all Indicators')
    yes_radio=Radiobutton(top_0, text='yes', value=1)
    no_radio=Radiobutton(top_0, text='no', value=2)

    Indicators =['Commodity Channel Index','Parabolic SAR',
                     'Money Flow Index','Bolinger Bands','StochRSI'
                     'STOCH','EMA','RSI']
    for indicator in Indicators:
        lb.insert(0, indicator)
    
    def onselect(evt):

        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        ind_entry.insert(0, ', ')
        return ind_entry.insert(0, '%s' % (value))
#    return some value here like ('You selected item %d: "%s"' % (index, value))


    lb.bind('<<ListboxSelect>>',onselect)

    Indicator.grid(row=0,column=0,sticky=E+N)
    select_btn.grid(row=1, column=0,sticky=E+N)
    ind_entry.grid(row=0, column=1,sticky=E+N, padx=2)

    lb.grid(row=0,column=2,rowspan=2,sticky=N+S)

    Use_lab.grid(row=0,column=3,sticky=W+N)
    yes_radio.grid(row=1, column=3,sticky=W+N)
    no_radio.grid(row=2,column=3,sticky=W+N)

    yscroll.grid(row=0, column=1, rowspan=2, sticky=N+S+E)
    

def symbol_widget(event):
    top_1 = Tk()
    #symbol scroll bar
    Symbol_lab= Label(top_1, text= 'Symbols')
    symb_set= Button(top_1, text='Set Symbols')
    symb_entry = Entry(top_1)

    symb_entry.bind('<Return>', quit_symb_window)
    symb_set.bind('<Button-1>', quit_symb_window)

    lb= Listbox(top_1, height=5)
    yscroll= Scrollbar(top_1, orient= VERTICAL)
    lb['yscrollcommand'] = yscroll.set
    yscroll['command'] = lb.yview

    def onselect(evt):

        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
#    return some value here like ('You selected item %d: "%s"' % (index, value))
    lb.bind('<<ListboxSelect>>',onselect)

    Use_lab=Label(top_1, text= 'Use all Symbols')
    yes_radio=Radiobutton(top_1, text='yes', value=1)
    no_radio=Radiobutton(top_1, text='no', value=2)

    Symbols = 'Query for symbols'
    for symbol in Symbols:
        lb.insert(0, indicator)

    Symbol_lab.grid(row=0,column=0,sticky=E+N)
    symb_set.grid(row=1, column=0,sticky=E+N)

    lb.grid(row=0,column=1,rowspan=2,sticky=N+S)
    yscroll.grid(row=0, column=1, rowspan=2, sticky=N+S+E)


    Use_lab.grid(row=0,column=3,sticky=W+N)
    yes_radio.grid(row=1, column=3,sticky=W+N)
    no_radio.grid(row=2,column=3,sticky=W+N)



top = Tk()

indicator_btn = Button(top, text ='Select indicators', command = indicator_widget)
symbol_btn = Button(top, text ='Select symbols', command = symbol_widget)


indicator_btn.grid(row=0,column=0,sticky='en')
symbol_btn.grid(row=0,column=1,sticky='wn')

top.mainloop()
