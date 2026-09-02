# Soccor API

from tkinter import *
from SoccarAPI import *


def onClick():
    number = jerseyEntry.get()
    number = int(number)
    playerData = getPlayerData(number)
    realNameLabel.config(text=playerData['name'],fg="black")
    realPositionLabel.config(text=playerData['position'],fg="black")
    realCountryLabel.config(text=playerData['citizenship'],fg="black")
    realAppLabel.config(text=playerData['appearances'],fg="black")
    realGoalLabel.config(text=playerData['goals'],fg="black")

smallFont = ["Helvetica", 14]
mediumFont = ["Helvetica", 18]

window = Tk()
window.geometry("500x500")
window.title("Soccer API")
window.config(bg="light blue")


instructionLabel = Label (window, text="Enter a Player's jersey number", font=smallFont, bg="light blue",fg="black")
instructionLabel.pack()

jerseyEntry = Entry(window,)
jerseyEntry.pack()

myButton = Button(window, text="SHOW PLAYER", font=smallFont, bg="blue", fg="white",
                  command = onClick)
myButton.pack()

nameLabel = Label(window, text="Player Name: ", font=mediumFont, bg="light blue", fg="black")
nameLabel.pack()

realNameLabel = Label(window, text="???????", font=mediumFont, bg="light blue", fg="black")
realNameLabel.pack()

positionLabel = Label(window, text="Player Position: ", font=mediumFont, bg="light blue", fg="black")
positionLabel.pack()

realPositionLabel = Label(window, text="???????", font=mediumFont, bg="light blue", fg="black")
realPositionLabel.pack()

countryLabel = Label(window, text="Player Nationality: ", font=mediumFont, bg="light blue", fg="black")
countryLabel.pack()

realCountryLabel = Label(window, text="???????", font=mediumFont, bg="light blue", fg="black")
realCountryLabel.pack()

applabel = Label(window, text="Player Appearances: ", font=mediumFont, bg="light blue", fg="black")
applabel.pack()

realAppLabel = Label(window, text="???????", font=mediumFont, bg="light blue", fg="black")
realAppLabel.pack()

goallabel = Label(window, text="Player Goals: ", font=mediumFont, bg="light blue", fg="black")
goallabel.pack()

realGoalLabel = Label(window, text="???????", font=mediumFont, bg="light blue", fg="black")
realGoalLabel.pack()    

window.mainloop()#






#using what i learnt today create prime real madrid