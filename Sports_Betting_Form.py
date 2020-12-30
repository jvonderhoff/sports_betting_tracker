import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.title("Sports Betting Tracker")

window.geometry('350x200')


sports = ["Baseball", "Basketball", "Football", "Hockey", "Soccer"]

leagues = [["MLB"],
          ["NBA","NCAA"],
          ["NFL","NCAA"],
          ["NHL"],
          ["EPL","MLS"]]

# Display selections 
def showBetResults():     
        sportresult = tkinter.Label(window, text=sportvariable.get())
        sportresult.grid(column=0, row=7)
        leagueresult = tkinter.Label(window, text=leaguevariable.get())
        leagueresult.grid(column=0, row=8)

# Sport lable and selection combobox
lbl = tkinter.Label(window, text="Sport")
lbl.grid(column=0, row=0)
sportvariable = ttk.Combobox(window,value=(sports))
sportvariable.grid(column=1, row=0, sticky='w')




# Populate leagues combobox based off sports selection
def callback(eventObject):
    abc = eventObject.widget.get()
    sport = sportvariable.get()
    index=sports.index(sport)
    leaguevariable.config(values=leagues[index])


# League label and  selection combobox
lbl2 = tkinter.Label(window, text="League")
lbl2.grid(column=0, row=1)
leaguevariable = ttk.Combobox(window)
leaguevariable.grid(column=1, row=1,sticky='w')
leaguevariable.bind('<Button-1>', callback)


# Submit button
btn = tkinter.Button(window, text="Submit", command=showBetResults)

btn.grid(column=0, row=6)



window.mainloop()