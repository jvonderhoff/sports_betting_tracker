import tkinter
from tkinter import ttk
from AirtableAPI import AirtableClient
window = tkinter.Tk()

window.title("Sports Betting Tracker")

window.geometry('700x400')  


sports = ["Baseball", "Basketball", "Football", "Hockey", "Soccer"]

leagues = [["MLB"],
          ["NBA","NCAA"],
          ["NFL","NCAA"],
          ["NHL"],
          ["EPL","MLS"]]

#TODO put api_key and base_key in ebvironmental variable or in a file
api_key = "key8khS01fFZYRQSv"
base_key = "appnN7BwmXQR0uOSW"
airtable_client = AirtableClient(api_key, base_key)
table_name = "Bet History"

team_1 = ["Detroit Tigers"]

team_2 = ["Minnesota Twins"]

bet_type = ["Spread", "Total", "Money Line", "Parlay", "Teaser"]

platforms = ["Barstool", "Draftkings", "Fanduel"]

# Get selections 
def BetResults():     
        sportresult = sportvariable.get()
        leagueresult = leaguevariable.get()
        bettyperesult = bettypevariable.get()
        team1result = team1variable.get()
        team2result = team2variable.get()
        bettingteamresult = bettingteamvariable.get()
        platformresult = platformvariable.get()
        betoddsresult = betoddsvariable.get()
        spreadresult = spreadvariable.get()

        # put the input into an array of size 10, with the sequence of: 
        # sport, league, Team1, Team2, Betting team, Bettype (spread), spread #, Bet odds, platform, status, date 
        record = []        
        record.append(sportresult)
        record.append(leagueresult)
        record.append(team1result)
        record.append(team2result)
        record.append(bettingteamresult)
        record.append(bettyperesult)
        record.append(spreadresult)
        record.append(betoddsresult)
        record.append(platformresult)
        # TODO: drop down for "Pending", "Win", "Looss"
        record.append("Pending")
        
        airtable_client.insert_airtable_rec(table_name, record)


# Sport lable and selection combobox
sport_lbl = tkinter.Label(window, text="Sport")
sport_lbl.grid(column=0, row=0)
sportvariable = ttk.Combobox(window,value=(sports), state="readonly")
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
leaguevariable = ttk.Combobox(window, state="readonly")
leaguevariable.grid(column=1, row=1,sticky='w')
leaguevariable.bind('<Button-1>', callback)

# Team 1 label and selection combobox
team1_lbl = tkinter.Label(window, text="Team 1")
team1_lbl.grid(column=0, row=2)
team1variable = ttk.Combobox(window,value=(team_1), state="readonly")
team1variable.grid(column=1, row=2, sticky='w')

# Team 2 label and selection combobox
team2_lbl = tkinter.Label(window, text="Team 2")
team2_lbl.grid(column=0, row=3)
team2variable = ttk.Combobox(window,value=(team_2), state="readonly")
team2variable.grid(column=1, row=3, sticky='w')

# Betting Team label and selection combobox
betting_team_lbl = tkinter.Label(window, text="Betting Team")
betting_team_lbl.grid(column=0, row=4)
bettingteamvariable = ttk.Combobox(window,value=(team_2), state="readonly")
bettingteamvariable.grid(column=1, row=4, sticky='w')


# Bet type label and selection combobox
bet_type_lbl = tkinter.Label(window, text="Bet Type")
bet_type_lbl.grid(column=0, row=5)
bettypevariable = ttk.Combobox(window,value=(bet_type), state="readonly")
bettypevariable.grid(column=1, row=5, sticky='w')

# Spread label and text box
spread_lbl = tkinter.Label(window, text="Spread")
spread_lbl.grid(column=0, row=6)
spreadvariable = tkinter.StringVar()
spread = ttk.Entry(window, textvariable=spreadvariable)
spread.grid(column=1, row=6, sticky='w')

# Bet odds label and text box
bet_odds_lbl = tkinter.Label(window, text="Odds")
bet_odds_lbl.grid(column=0, row=7)
betoddsvariable = tkinter.StringVar()
bet_odds = ttk.Entry(window, textvariable=betoddsvariable)
bet_odds.grid(column=1, row=7, sticky='w')

# Bet type label and selection combobox
platform_lbl = tkinter.Label(window, text="Platform")
platform_lbl.grid(column=0, row=8)
platformvariable = ttk.Combobox(window,value=(platforms), state="readonly")
platformvariable.grid(column=1, row=8, sticky='w')


# Submit button
btn = tkinter.Button(window, text="Submit", command=BetResults)

btn.grid(column=0, row=10)



window.mainloop()