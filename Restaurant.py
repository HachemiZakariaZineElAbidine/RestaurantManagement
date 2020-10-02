import tkinter
from tkinter import messagebox

def show_model_windows():
    messagebox.showinfo("","Bientot Disponible")


def Pizza_M(*args):
    Marg = (int(MargeriteSpin1.get())*150)+(int(MargeriteSpin2.get())*300)+(int(MargeriteSpin3.get())*1200)
    Champ = (int(ChampignonSpin1.get())*180)+(int(ChampignonSpin2.get())*350)+(int(ChampignonSpin3.get())*1300)
    Napo = (int(NapolitanaSpin1.get())*250)+(int(NapolitanaSpin2.get())*450)+(int(NapolitanaSpin3.get())*1700)
    Tho = (int(ThonSpin1.get())*250)+(int(ThonSpin2.get())*450)+(int(ThonSpin3.get())*1700)
    Mexi = (int(MexicaineSpin1.get())*350)+(int(MexicaineSpin2.get())*600)+(int(MexicaineSpin3.get())*2300)
    Orien =  (int(OrientaleSpin1.get())*300)+(int(OrientaleSpin2.get())*550)+(int(OrientaleSpin3.get())*2100)
    p = Marg + Champ + Napo + Tho + Mexi + Orien
    return(p)


def Salade_M(*args):
    Mac = (int(MacedoineSpin.get())*350)
    Ces = (int(CesarSpin.get())*400)
    From = (int(FromagereSpin.get())*450)
    Ver = (int(VerteSpin.get())*250)
    s = Mac + Ces + From + Ver
    return(s)


def Burger_M(*args):
    Clas = (int(ClasiqueSpin1.get())*400)+(int(ClasiqueSpin2.get())*550)
    Ches = (int(CheeseSpin1.get())*500)+(int(CheeseSpin2.get())*650)
    Chik = (int(ChickenSpin1.get())*400)+(int(ChickenSpin2.get())*550)
    Fis = (int(FishSpin1.get())*400)+(int(FishSpin2.get())*550)
    b = Clas + Ches + Chik + Fis
    return(b)


def Plat_M(*args):
    Sth = (int(SteakHacheSpin.get())*700)
    Ste = (int(SteakSpin.get())*1000)
    Enc = (int(EntreCotesSpin.get())*1200)
    Esg = (int(EscalopeGrilleSpin.get())*600)
    Esp = (int(EscalopePanneSpin.get())*700)
    Psb = (int(PanneSauceBlancheSpin.get())*450)
    Psr = (int(PanneSauceRougeSpin.get())*450)
    p = Sth + Ste + Enc + Esg +Esp + Psb + Psr
    return(p)


def Montant_F(*args):
    pm = Pizza_M()
    sm = Salade_M()
    bm = Burger_M()
    plm = Plat_M()
    mf = pm + sm + bm + plm
    mf = str(mf)
    mf = mf+" Da"
    AffichageLabel.configure(text=mf)


def Reset_All(*args):
    FromagereSpin.set()
    CesarSpin.set()
    MacedoineSpin.set()
    VerteSpin.set()


main = tkinter.Tk()

# Titre
main.title("Restaurant Management Systeme")

# Geometry
scx = int(main.winfo_screenwidth())
scy = int(main.winfo_screenheight())
winx = 800
winy = 450
posx = (scx // 2) - (winx // 2)
posy = (scy // 2) - (winy // 2)
geo = "{}x{}+{}+{}".format(winx,winy,posx,posy)
main.geometry(geo)
main.minsize(800, 450)
main.maxsize(800, 450)


# Pizza Frame
PizzaFrame = tkinter.LabelFrame(main, text="PIZZA")
PizzaFrame.grid(row=0, column=0)

# Size
# S
S = tkinter.Label(PizzaFrame, text="   S ")
S.grid(row=0, column=2)
# M
M = tkinter.Label(PizzaFrame, text=" M ")
M.grid(row=0, column=4)
# XXL
XXL = tkinter.Label(PizzaFrame, text=" XXL ")
XXL.grid(row=0, column=6)

# Margerite
MargeriteLabel= tkinter.Label(PizzaFrame, text="Margerite")
MargeriteLabel.grid(row=1, column=0)
MargeriteSpin1 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
MargeriteSpin1.grid(row=1, column=2)
MargeriteSpin2 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
MargeriteSpin2.grid(row=1, column=4)
MargeriteSpin3 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
MargeriteSpin3.grid(row=1, column=6)

#Champignon
ChampignonLabel = tkinter.Label(PizzaFrame, text="Champignon")
ChampignonLabel.grid(row=2, column=0)
ChampignonSpin1 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
ChampignonSpin1.grid(row=2, column=2)
ChampignonSpin2 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
ChampignonSpin2.grid(row=2, column=4)
ChampignonSpin3 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
ChampignonSpin3.grid(row=2, column=6)

#Napolitana
NapolitanaLabel = tkinter.Label(PizzaFrame, text="Napolitana")
NapolitanaLabel.grid(row=3, column=0)
NapolitanaSpin1 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
NapolitanaSpin1.grid(row=3, column=2)
NapolitanaSpin2 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
NapolitanaSpin2.grid(row=3, column=4)
NapolitanaSpin3 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
NapolitanaSpin3.grid(row=3, column=6)

# Thon
ThonLabel = tkinter.Label(PizzaFrame, text="Thon")
ThonLabel.grid(row=4, column=0)
ThonSpin1 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
ThonSpin1.grid(row=4, column=2)
ThonSpin2 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
ThonSpin2.grid(row=4, column=4)
ThonSpin3 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
ThonSpin3.grid(row=4, column=6)

#Mexicaine
MexicaineLabel = tkinter.Label(PizzaFrame, text="Mexicaine")
MexicaineLabel.grid(row=5, column=0)
MexicaineSpin1 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
MexicaineSpin1.grid(row=5, column=2)
MexicaineSpin2 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
MexicaineSpin2.grid(row=5, column=4)
MexicaineSpin3 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
MexicaineSpin3.grid(row=5, column=6)

#Orientale
OrientaleLabel = tkinter.Label(PizzaFrame, text="Orientale")
OrientaleLabel.grid(row=6, column=0)
OrientaleSpin1 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
OrientaleSpin1.grid(row=6, column=2)
OrientaleSpin2 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
OrientaleSpin2.grid(row=6, column=4)
OrientaleSpin3 = tkinter.Spinbox(PizzaFrame, from_=0, to=100)
OrientaleSpin3.grid(row=6, column=6)




# Burger Frame
BurgerFrame = tkinter.LabelFrame(main, text="BURGER")
BurgerFrame.grid(row=1, column=0)

# Size
Simple = tkinter.Label(BurgerFrame, text="Simple")
Simple.grid(row=0, column=2)
Double = tkinter.Label(BurgerFrame, text="Double")
Double.grid(row=0, column=4)

# Clasique
ClasiqueLabel = tkinter.Label(BurgerFrame, text="Clasique")
ClasiqueLabel.grid(row=1, column=0)
ClasiqueSpin1 = tkinter.Spinbox(BurgerFrame, from_=0, to=100)
ClasiqueSpin1.grid(row=1, column=2)
ClasiqueSpin2 = tkinter.Spinbox(BurgerFrame, from_=0, to=100)
ClasiqueSpin2.grid(row=1, column=4)

# Cheese
CheeseLabel = tkinter.Label(BurgerFrame, text="Cheese")
CheeseLabel.grid(row=2, column=0)
CheeseSpin1 = tkinter.Spinbox(BurgerFrame, from_=0, to=100)
CheeseSpin1.grid(row=2, column=2)
CheeseSpin2 = tkinter.Spinbox(BurgerFrame, from_=0, to=100)
CheeseSpin2.grid(row=2, column=4)


# Chicken
ChickenLabel = tkinter.Label(BurgerFrame, text="Chicken")
ChickenLabel.grid(row=3, column=0)
ChickenSpin1 = tkinter.Spinbox(BurgerFrame, from_=0, to=100)
ChickenSpin1.grid(row=3, column=2)
ChickenSpin2 = tkinter.Spinbox(BurgerFrame, from_=0, to=100)
ChickenSpin2.grid(row=3, column=4)

# Fish
FishLabel = tkinter.Label(BurgerFrame, text="Fish")
FishLabel.grid(row=4, column=0)
FishSpin1 = tkinter.Spinbox(BurgerFrame, from_=0, to=100)
FishSpin1.grid(row=4, column=2)
FishSpin2 = tkinter.Spinbox(BurgerFrame, from_=0, to=100)
FishSpin2.grid(row=4, column=4)

# Eggy
EggyLabel = tkinter.Label(BurgerFrame, text="Eggy")
EggyLabel.grid(row=5, column=0)
EggySpin1 = tkinter.Spinbox(BurgerFrame, from_=0, to=100)
EggySpin1.grid(row=5, column=2)
EggySpin2 = tkinter.Spinbox(BurgerFrame, from_=0, to=100)
EggySpin2.grid(row=5, column=4)




# Plat Frame
PlatFrame = tkinter.LabelFrame(main, text="PLAT")
PlatFrame.grid(row=0, column=1)

# SteakHaché
SteakHacheLabel = tkinter.Label(PlatFrame, text="SteakHaché")
SteakHacheLabel.grid(row=0, column=0)
SteakHacheSpin = tkinter.Spinbox(PlatFrame, from_=0, to=100)
SteakHacheSpin.grid(row= 0, column=2)

# Steak
SteakLabel = tkinter.Label(PlatFrame, text="Steak")
SteakLabel.grid(row=1, column=0)
SteakSpin = tkinter.Spinbox(PlatFrame, from_=0, to=100)
SteakSpin.grid(row=1, column=2)

# EntreCotes
EntreCotesLabel = tkinter.Label(PlatFrame, text="Entre Cotes")
EntreCotesLabel.grid(row=2, column=0)
EntreCotesSpin = tkinter.Spinbox(PlatFrame, from_=0, to=100)
EntreCotesSpin.grid(row=2, column=2)

# EscalopeGrille
EscalopeGrilleLabel = tkinter.Label(PlatFrame, text="Escalope Grillé")
EscalopeGrilleLabel.grid(row=3, column=0)
EscalopeGrilleSpin = tkinter.Spinbox(PlatFrame, from_=0, to=100)
EscalopeGrilleSpin.grid(row=3, column=2)

# EscalopePanne
EscalopePanneLabel = tkinter.Label(PlatFrame, text="Escalope Panné")
EscalopePanneLabel.grid(row=4, column=0)
EscalopePanneSpin = tkinter.Spinbox(PlatFrame, from_=0, to=100)
EscalopePanneSpin.grid(row=4, column=2)

# PanneSauceBlanche
PanneSauceBlancheLabel = tkinter.Label(PlatFrame, text="Panné Sauce Blanche")
PanneSauceBlancheLabel.grid(row=5, column=0)
PanneSauceBlancheSpin = tkinter.Spinbox(PlatFrame, from_=0, to=100)
PanneSauceBlancheSpin.grid(row=5, column=2)

# PanneSauceRouge
PanneSauceRougeLabel = tkinter.Label(PlatFrame, text="Panné Sauce Rouge")
PanneSauceRougeLabel.grid(row=6, column=0)
PanneSauceRougeSpin = tkinter.Spinbox(PlatFrame, from_=0, to=100)
PanneSauceRougeSpin.grid(row=6, column=2)




# Salade Frame

SaladeFrame = tkinter.LabelFrame(main, text="SALADE")
SaladeFrame.grid(row=1, column=1)

# Macédoine
MacedoineLabel = tkinter.Label(SaladeFrame, text="Macédoine")
MacedoineLabel.grid(row=0, column=0)
MacedoineSpin = tkinter.Spinbox(SaladeFrame, from_=0, to=100)
MacedoineSpin.grid(row=0, column=2)

# César
CesarLabel = tkinter.Label(SaladeFrame, text="César")
CesarLabel.grid(row=1, column=0)
CesarSpin = tkinter.Spinbox(SaladeFrame, from_=0, to=100)
CesarSpin.grid(row=1, column=2)

# Fromagere
FromagereLabel = tkinter.Label(SaladeFrame, text="Fromagere")
FromagereLabel.grid(row=2, column=0)
FromagereSpin = tkinter.Spinbox(SaladeFrame, from_=0, to=100)
FromagereSpin.grid(row=2, column=2)

# Verte
VerteLabel = tkinter.Label(SaladeFrame, text="Verte")
VerteLabel.grid(row=3, column=0)
VerteSpin = tkinter.Spinbox(SaladeFrame, from_=0, to=100)
VerteSpin.grid(row=3, column=2)



# Commande Frame

CommandeFrame = tkinter.LabelFrame(main, text="COMMANDE")
CommandeFrame.grid(row=2, column=0)

# Emporter sur place

SurPlace_widget = tkinter.Radiobutton(CommandeFrame, text="Sur Place", value=1)
SurPlace_widget.grid(row=1, column=0)
Emporter_widget = tkinter.Radiobutton(CommandeFrame, text="Emporter", value=0)
Emporter_widget.grid(row=1, column=1)


# Terminer
TerminerButton = tkinter.Button(main, text="Terminer", command=Montant_F)
TerminerButton.grid(row=3, column=1)

# Réinitialiser
ResetButton = tkinter.Button(main, text="Réinitialiser", command=show_model_windows)
ResetButton.grid(row=3, column=0)

# Prix Frame
AffichageFrame = tkinter.LabelFrame(main, text="PRIX")
AffichageFrame.grid(row=3, column=2)


# Affichage Resultat
AffichageLabel = tkinter.Label(AffichageFrame)
AffichageLabel.grid(row=0, column=3)



main.mainloop()
