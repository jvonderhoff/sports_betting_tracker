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

team_1 = ["Detroit Tigers"]

team_2 = ["Minnesota Twins"]

bet_type = ["Spread", "Total", "Money Line", "Parlay", "Teaser"]

# Display selections 
def showBetResults():     
        sportresult = tkinter.Label(window, text=sportvariable.get())
        sportresult.grid(column=0, row=7)
        leagueresult = tkinter.Label(window, text=leaguevariable.get())
        leagueresult.grid(column=0, row=8)

# Sport lable and selection combobox
sport_lbl = tkinter.Label(window, text="Sport")
sport_lbl.grid(column=0, row=0)
sportvariable = ttk.Combobox(window,value=(sports))
sportvariable.grid(column=1, row=0, sticky='w')




# Populate leagues combobox based off sports selection
def callback(eventObject):
    abc = eventObject.widget.get()
    sport = sportvariable.get()
    index=sports.index(sport)
    leaguevariable.config(values=leagues[index])


# League label and selection combobox
league_lbl = tkinter.Label(window, text="League")
league_lbl.grid(column=0, row=1)
leaguevariable = ttk.Combobox(window)
leaguevariable.grid(column=1, row=1,sticky='w')
leaguevariable.bind('<Button-1>', callback)

# Team 1 label and selection combobox
team1_lbl = tkinter.Label(window, text="Team 1")
team1_lbl.grid(column=0, row=2)
team1variable = ttk.Combobox(window,value=(team_1))
team1variable.grid(column=1, row=2)

# Team 2 label and selection combobox
team2_lbl = tkinter.Label(window, text="Team 2")
team2_lbl.grid(column=0, row=3)
team2variable = ttk.Combobox(window,value=(team_2))
team2variable.grid(column=1, row=3)


# Bet type label and selection combobox
bet_type_lbl = tkinter.Label(window, text="Bet Type")
bet_type_lbl.grid(column=0, row=4)
bettypevariable = ttk.Combobox(window,value=(bet_type))
bettypevariable.grid(column=1, row=4)


# Submit button
btn = tkinter.Button(window, text="Submit", command=showBetResults)

btn.grid(column=0, row=6)



window.mainloop()