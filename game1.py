from tkinter import *
import time

global clickStrength
global cash
global clickersBought
global clickerWorkTimeMS
global clickerCost
global clickerNum
global clickerCostMultiplier
global upgradesBought
global clickStrengthMultiplier
global upgradeCost
global upgradeCostMultiplier
upgradeCostMultiplier = 50
upgradeCost = 1000
clickStrengthMultiplier = 1
upgradesBought = 0
clickStrength = 1
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
    global clickStrength
    saveFile = open("save.txt", "w")
    saveFile.write("%d" %cash + "\n")
    saveFile.write("%d" %clickersBought + "\n")
    saveFile.write("%d" %clickerCost + "\n")
    saveFile.write("%d" %clickerCostMultiplier + "\n")
    saveFile.write("%d" %upgradesBought + "\n")
    saveFile.write("%d" %upgradeCost + "\n")
    saveFile.write("%d" %upgradeCostMultiplier + "\n")
    saveFile.write("%d" %clickStrengthMultiplier + "\n")
    saveFile.write("%d" %clickStrength + "\n")
    saveFile.close()

def load():
    global cash
    global clickersBought
    global clickerCost
    global clickerCostMultiplier
    global upgradesBought
    global upgradeCost
    global upgradeCostMultiplier
    global clickStrengthMultiplier
    global clickStrength
    loadFile = open("save.txt", "r")
    loadLines = loadFile.readlines()
    cash = int(loadLines[0])
    clickersBought = int(loadLines[1])
    clickerCost = int(loadLines[2])
    clickerCostMultiplier = int(loadLines[3])
    upgradesBought = int(loadLines[4])
    upgradeCost = int(loadLines[5])
    upgradeCostMultiplier = int(loadLines[6])
    clickStrengthMultiplier = int(loadLines[7])
    clickStrength = int(loadLines[8])
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
    cash += clickStrength
    cashDisplayV.set("Cash: $" + str(cash))

def shopUI():
    costDisplayV.set("Next Clicker: $" + str(clickerCost))
    upgradeDisplayV.set("Next Upgrade: $" + str(upgradeCost))
    clickerCostDisplay.pack()
    upgradeCostDisplay.pack()
    buyUG.pack()
    hideMe(shop)
    hideMe(click)
    back.pack()
    buyClick.pack()
    clickerNum.pack()


def clicker():
    global clickerCost
    global cash
    global clickerWorkTime
    cash += clickersBought
    time.sleep(clickerWorkTime)

def buyUpgrade():
    global upgradeCost
    global cash
    global upgradesBought
    global clickStrength
    global clickStrengthMultiplier
    global upgradeCostMultiplier
    upgradeDisplayV.set("Next Upgrade: $" + str(upgradeCost))
    if cash < upgradeCost:
        pass
    else:
        upgradesBought += 1
        clickStrength += clickStrengthMultiplier
        upgradeCost += upgradeCostMultiplier
        upgradeCostMultiplier += 1
        clickStrengthMultiplier += 1
        cash -= upgradeCost


def normalUI():
    hideMe(clickerCostDisplay)
    hideMe(back)
    hideMe(buyClick)
    hideMe(clickerNum)
    hideMe(buyUG)
    hideMe(upgradeCostDisplay)
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


buyClick = Button(Game, text="Buy Clicker", command=buyClicker)
back = Button(Game, text="Back", command=normalUI)
click = Button(Game, text="Click", command=click, padx=10, pady=10)
upgradeDisplayV = StringVar()
cashDisplayV = StringVar()
clickersBoughtV = StringVar()
costDisplayV = StringVar()
shop = Button(Game, text="Shop", command=shopUI)
cashDisplay = Label(Game, textvariable=cashDisplayV, font=("Helvetica", 24))
clickerNum = Label(Game, textvariable=clickersBoughtV, font=("Helvetica", 24))
clickerCostDisplay = Label(Game, textvariable=costDisplayV, font=("Helvetica", 24))
upgradeCostDisplay = Label(Game, textvariable=upgradeDisplayV, font=("Helvetica", 24))
buyUG = Button(Game, text="Mouse Upgrade", command=buyUpgrade)
click.pack(anchor=CENTER)
cashDisplay.pack(anchor=NE)
shop.pack()

Game.after(clickerWorkTimeMS, addCash)


Game.mainloop()
