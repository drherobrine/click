
from tkinter import *
import time

global cash
global clickersBought
global clickerWorkTimeMS
global clickerCost
global clickerNum
global clickerCostMultiplier
cash = 0
clickersBought = 0
clickerWorkTime = 1
clickerCost = 10
clickerCostMultiplier = 1
clickerWorkTimeMS = clickerWorkTime * 1000


def addCash():
    global cash
    global clickerWorkTimeMS
    global clickersBought
    cash += clickersBought
    Game.after(clickerWorkTimeMS, addCash)
    cashDisplayV.set("Cash: $" + str(cash))
    save()


def save():
    saveFile = open("save.txt", "w")
    saveFile.write("%d" %cash + "\n")
    saveFile.write("%d" %clickersBought + "\n")
    saveFile.close()

def load():
    global cash
    global clickersBought
    loadFile = open("save.txt", "r")
    loadLines = loadFile.readlines()
    cash = int(loadLines[0])
    clickersBought = int(loadLines[1])
    print(cash)
    print(clickersBought)
    loadFile.close()

def timer():
    global cash
    global clickerWorkTimeMS
    Game.after(clickerWorkTimeMS, addCash)

def hideMe(sth):
    sth.pack_forget()


def click():
    global cash
    cash += 1
    cashDisplayV.set("Cash: $" + str(cash))

def shopUI():
    clickerCostDisplay.pack()
    hideMe(shop)
    hideMe(click)
    back.pack()
    buy.pack()
    clickerNum.pack()


def clicker():
    global clickerCost
    global cash
    global clickerWorkTime
    cash += clickersBought
    time.sleep(clickerWorkTime)


def normalUI():
    hideMe(clickerCostDisplay)
    hideMe(back)
    hideMe(buy)
    hideMe(clickerNum)
    click.pack(anchor=CENTER)
    cashDisplay.pack(anchor=NE)
    shop.pack()

def buyClicker():
    global cash
    global clickersBought
    global clickerWorkTime
    global clickerCost
    global clickerCostMultiplier
    clickerWorkTime -= 0.1
    costDisplayV.set("Next Clicker: $" + str(clickerCost))
    clickersBoughtV.set("Clickers Bought: " + str(clickersBought))
    if clickerCost > cash:
        pass
    else:
        cash -= clickerCost
        clickersBought += 1
        clickerCost += clickerCostMultiplier
        clickerCostMultiplier += 1
        cashDisplayV.set("Cash: $" + str(cash))
        cashDisplay.pack()

load()
Game = Tk()



Game.title("Garry's Clicker")
global costDisplayV
screenHeight = Game.winfo_screenheight()
screenWidth = Game.winfo_screenwidth()
geometry = "%dx%d" % (screenWidth, screenHeight)

Game.geometry(geometry)


buy = Button(Game, text="Buy Clicker", command=buyClicker)
back = Button(Game, text="Back", command=normalUI)
click = Button(Game, text="Click", command=click, padx=10, pady=10)
cashDisplayV = StringVar()
clickersBoughtV = StringVar()
costDisplayV = StringVar()
shop = Button(Game, text="Shop", command=shopUI)
cashDisplay = Label(Game, textvariable=cashDisplayV, font=("Helvetica", 24))
clickerNum = Label(Game, textvariable=clickersBoughtV, font=("Helvetica", 24))
clickerCostDisplay = Label(Game, textvariable=costDisplayV, font=("Helvetica", 24))
click.pack(anchor=CENTER)
cashDisplay.pack(anchor=NE)
shop.pack()

Game.after(clickerWorkTimeMS, addCash)


Game.mainloop()
