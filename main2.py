#Tkinter
#tkinter is a standard GUI library for Python. It provides a fast and easy way to create GUI applications.

#GUI (Graphical User Interface)

# we're importing the tkinter libary
import tkinter
#Tk gives us access to create a window
#we're creating a tkinter window and assigning to the
#variable called window


acronym = {
    "lol": "laugh out load",
    "tysm": "thank you so much",
    "idk":   "I dont know",
    "idc": "i dont care",
    "cba": "cant be asked",
    "brb": "be right back",
    "gg":  "Good Game",
    "ff":   "forfeit",
    "hru": " how are you"
}
#we're creating a function called onClick
def onClick():
    # it gets whatever the user inputs inside the mystery
    #and assigns it to the variable called word
    word = myEntry.get()
    # we get the meaning of the word from the acronym dictionary and assign it to the variable called meaning
    meaning = acronym[word]
    #we delete whatever is inside the text widget 
    #from the begining to the end
    myText.delete("0.0", tkinter.END)
    #we insert the meaning of the word inside the text widget
    #starting from the end
    myText.insert(tkinter.END,meaning)
    myEntry.delete("0",tkinter.END)

window = tkinter.Tk()
#we're setting the window title
window.title("Acronym Finder")
#we're setting the size of the window to 500x500
#which is a perfect square
window.geometry("500x500")



#we're creating a label widget and setting the text
myLabel = tkinter.Label(window,text= "Enter the word you wannt the meaning off")
myLabel.pack ()
#this allows the label to be displayed in the window
myEntry = tkinter.Entry(window,width=20,bg="Light Green")
myEntry.pack()
#we're creating and entry setting and setting the
#bg coulour
myButton = tkinter.Button(window,width=8,bg = "Blue",
                          text = "Submit", command=onClick)
myButton.pack()
#we're creating a button widget and setting with the colour and the text
myText  = tkinter.Text(window,width=15,height = 7,bg= "Red")
myText.pack()

# this allows the window to run
window.mainloop()




#Widgets 
# Widget are what place inside our window that the user can interact with


#labels
#entry
#button
#text


#using this tkinter window create a language tanslator
#using english as defult
#and anyother language of my choice