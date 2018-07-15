# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:59:26 2018

@author: VS
"""

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import numpy as np
import pandas as pd
from PIL import Image, ImageTk as PIIIL
import random



class panak:
    polohaX = 0
    polohaY = 0
    spritS = None
    spritS1 = None
    spritS2 = None
    spritN = None
    spritN1 = None
    spritN2 = None
    spritW = None
    spritW1 = None
    spritW2 = None
    spritE = None
    spritE1 = None
    spritE2 = None
    naMape = None
    jmenoSpritu = "chyba"
    aktualniOri = "S"
    
   
    def __init__(self, platno_ob, sourad, rozmerPoleX, rozmerPoleY, soubor):
      
        self.jmenoSpritu = soubor
        obrazekPIL_hrac = PIIIL.Image.open("chodic_soubory\\" + self.jmenoSpritu+"N.png")  #obrázek se otevře pomocí PILu
        obrazekPIL_hrac = obrazekPIL_hrac.resize((rozmerPoleX,rozmerPoleY))
        self.spritN = PIIIL.PhotoImage(obrazekPIL_hrac)
        obrazekPIL_hrac = PIIIL.Image.open("chodic_soubory\\" + self.jmenoSpritu+"N1.png")  #obrázek se otevře pomocí PILu
        obrazekPIL_hrac = obrazekPIL_hrac.resize((rozmerPoleX,rozmerPoleY))
        self.spritN1 = PIIIL.PhotoImage(obrazekPIL_hrac)
        obrazekPIL_hrac = PIIIL.Image.open("chodic_soubory\\" + self.jmenoSpritu+"N2.png")  #obrázek se otevře pomocí PILu
        obrazekPIL_hrac = obrazekPIL_hrac.resize((rozmerPoleX,rozmerPoleY))
        self.spritN2 = PIIIL.PhotoImage(obrazekPIL_hrac)
        obrazekPIL_hrac = PIIIL.Image.open("chodic_soubory\\" + self.jmenoSpritu+"W.png")  #obrázek se otevře pomocí PILu
        obrazekPIL_hrac = obrazekPIL_hrac.resize((rozmerPoleX,rozmerPoleY))
        self.spritW = PIIIL.PhotoImage(obrazekPIL_hrac)
        obrazekPIL_hrac = PIIIL.Image.open("chodic_soubory\\" + self.jmenoSpritu+"W1.png")  #obrázek se otevře pomocí PILu
        obrazekPIL_hrac = obrazekPIL_hrac.resize((rozmerPoleX,rozmerPoleY))
        self.spritW1 = PIIIL.PhotoImage(obrazekPIL_hrac)
        obrazekPIL_hrac = PIIIL.Image.open("chodic_soubory\\" + self.jmenoSpritu+"W2.png")  #obrázek se otevře pomocí PILu
        obrazekPIL_hrac = obrazekPIL_hrac.resize((rozmerPoleX,rozmerPoleY))
        self.spritW2 = PIIIL.PhotoImage(obrazekPIL_hrac)
        obrazekPIL_hrac = PIIIL.Image.open("chodic_soubory\\" + self.jmenoSpritu+"E.png")  #obrázek se otevře pomocí PILu
        obrazekPIL_hrac = obrazekPIL_hrac.resize((rozmerPoleX,rozmerPoleY))
        self.spritE = PIIIL.PhotoImage(obrazekPIL_hrac)
        obrazekPIL_hrac = PIIIL.Image.open("chodic_soubory\\" + self.jmenoSpritu+"E1.png")  #obrázek se otevře pomocí PILu
        obrazekPIL_hrac = obrazekPIL_hrac.resize((rozmerPoleX,rozmerPoleY))
        self.spritE1 = PIIIL.PhotoImage(obrazekPIL_hrac)
        obrazekPIL_hrac = PIIIL.Image.open("chodic_soubory\\" + self.jmenoSpritu+"E2.png")  #obrázek se otevře pomocí PILu
        obrazekPIL_hrac = obrazekPIL_hrac.resize((rozmerPoleX,rozmerPoleY))
        self.spritE2 = PIIIL.PhotoImage(obrazekPIL_hrac)
        obrazekPIL_hrac = PIIIL.Image.open("chodic_soubory\\" + self.jmenoSpritu+"S.png")  #obrázek se otevře pomocí PILu
        obrazekPIL_hrac = obrazekPIL_hrac.resize((rozmerPoleX,rozmerPoleY))
        self.spritS = PIIIL.PhotoImage(obrazekPIL_hrac)
        obrazekPIL_hrac = PIIIL.Image.open("chodic_soubory\\" + self.jmenoSpritu+"S1.png")  #obrázek se otevře pomocí PILu
        obrazekPIL_hrac = obrazekPIL_hrac.resize((rozmerPoleX,rozmerPoleY))
        self.spritS1 = PIIIL.PhotoImage(obrazekPIL_hrac)
        obrazekPIL_hrac = PIIIL.Image.open("chodic_soubory\\" + self.jmenoSpritu+"S2.png")  #obrázek se otevře pomocí PILu
        obrazekPIL_hrac = obrazekPIL_hrac.resize((rozmerPoleX,rozmerPoleY))
        self.spritS2 = PIIIL.PhotoImage(obrazekPIL_hrac)
        
        self.polohaX = sourad[0]
        self.polohaY = sourad[1]
        self.naMape = platno_ob.create_image(0 + self.polohaX*rozmerPoleX,0 + self.polohaY*rozmerPoleY,image = self.spritS, anchor = NW)#samotné vytvoření objektu na canvasu
        
    
    def otocPanaka(self,platno_ob, smer):
        if(smer=="N"):
            self.aktualniOri = "N"
            platno_ob.itemconfig(self.naMape, image = self.spritN)
        elif(smer=="E"):
            self.aktualniOri = "E"
            platno_ob.itemconfig(self.naMape, image = self.spritE)
        elif(smer=="S"):
            self.aktualniOri = "S"
            platno_ob.itemconfig(self.naMape, image = self.spritS)
        elif(smer=="W"):
            self.aktualniOri = "W"
            platno_ob.itemconfig(self.naMape, image = self.spritW)
                    
            
    def pohniPanaka(self,platno_ob, rozmerPoleX, rozmerPoleY):
        platno_ob.coords(self.naMape,0 + self.polohaX*rozmerPoleX,0 + self.polohaY*rozmerPoleY)#hýbání; šlo by to i canvas.move, kde by ale musely být změny; zde jsou souřadnice
8    
    
class hracova_postava(panak):  #dedici trida k tride panak
    sesbiranychPokladu = 0
    sesbirano = False
    mrtvy = False
    
class nepritel(panak):
    krok_animacni_iterace = 0
    
    def animuj(self, platno_ob, rozmerPoleX, rozmerPoleY, orientace, stupenIterace, postava_hrace):
        if(stupenIterace == 0):
            if(orientace == "W"):
                platno_ob.itemconfig(self.naMape, image = self.spritW1)
                platno_ob.coords(self.naMape,0 + self.polohaX*rozmerPoleX - rozmerPoleX//4 , 0 + self.polohaY*rozmerPoleY)
            if(orientace == "E"):
                platno_ob.itemconfig(self.naMape, image = self.spritE1)
                platno_ob.coords(self.naMape,0 + self.polohaX*rozmerPoleX + rozmerPoleX//4 , 0 + self.polohaY*rozmerPoleY)
            if(orientace == "S"):
                platno_ob.itemconfig(self.naMape, image = self.spritS1)
                platno_ob.coords(self.naMape,0 + self.polohaX*rozmerPoleX , 0 + self.polohaY*rozmerPoleY + rozmerPoleY//4 )
            if(orientace == "N"):
                platno_ob.itemconfig(self.naMape, image = self.spritN1)
                platno_ob.coords(self.naMape,0 + self.polohaX*rozmerPoleX , 0 + self.polohaY*rozmerPoleY - rozmerPoleY//4 )
            self.zkontrolujUlovil(postava_hrace)
            root.after(100, self.animuj, platno_ob, rozmerPoleX, rozmerPoleY, orientace,1,postava_hrace)
        if(stupenIterace == 1):
            if(orientace == "W"):
                platno_ob.itemconfig(self.naMape, image = self.spritW2)
                platno_ob.coords(self.naMape,0 + self.polohaX*rozmerPoleX -2*rozmerPoleX//4, 0 + self.polohaY*rozmerPoleY)
            if(orientace == "E"):
                platno_ob.itemconfig(self.naMape, image = self.spritE2)
                platno_ob.coords(self.naMape,0 + self.polohaX*rozmerPoleX +2*rozmerPoleX//4, 0 + self.polohaY*rozmerPoleY)
            if(orientace == "S"):
                platno_ob.itemconfig(self.naMape, image = self.spritS2)
                platno_ob.coords(self.naMape,0 + self.polohaX*rozmerPoleX , 0 + self.polohaY*rozmerPoleY+2*rozmerPoleY//4)
            if(orientace == "N"):
                platno_ob.itemconfig(self.naMape, image = self.spritN2)
                platno_ob.coords(self.naMape,0 + self.polohaX*rozmerPoleX , 0 + self.polohaY*rozmerPoleY-2*rozmerPoleY//4)
            self.zkontrolujUlovil(postava_hrace)
            root.after(100, self.animuj, platno_ob, rozmerPoleX, rozmerPoleY, orientace,2,postava_hrace)
        if(stupenIterace == 2):
            if(orientace == "W"):
                self.polohaX = self.polohaX - 1
            if(orientace == "E"):
                self.polohaX = self.polohaX + 1
            if(orientace == "S"):
                self.polohaY = self.polohaY + 1
            if(orientace == "N"):
                self.polohaY = self.polohaY - 1
            self.zkontrolujUlovil(postava_hrace)
            self.pohniPanaka(platno,rozmerPoleX,rozmerPoleY)
    
    
    
    def jdePoHracovi(self, platno_ob, mapa_panak, postava_hrace):
        vzdalenostX = self.polohaX - postava_hrace.polohaX
        vzdalenostY = self.polohaY - postava_hrace.polohaY
        pohnulSe = False
        
        if(abs(vzdalenostX) >= abs(vzdalenostY)):
            if( vzdalenostX > 0 and mapa_panak.jePolickoPruch(self.polohaX - 1,self.polohaY) == True):
                self.otocPanaka(platno_ob, "W")
                self.animuj(platno_ob, mapa_panak.rozmerPoleX, mapa_panak.rozmerPoleY, "W",0,postava_hrace)
                pohnulSe = True
            elif( vzdalenostX < 0 and mapa_panak.jePolickoPruch(self.polohaX + 1,self.polohaY) == True):
                self.otocPanaka(platno_ob, "E")
                self.animuj(platno_ob, mapa_panak.rozmerPoleX, mapa_panak.rozmerPoleY, "E",0,postava_hrace)
                pohnulSe = True
            elif( vzdalenostY > 0 and mapa_panak.jePolickoPruch(self.polohaX,self.polohaY-1) == True):
                self.otocPanaka(platno_ob, "N")
                self.animuj(platno_ob, mapa_panak.rozmerPoleX, mapa_panak.rozmerPoleY, "N",0,postava_hrace)
                pohnulSe = True
            elif( vzdalenostY < 0 and mapa_panak.jePolickoPruch(self.polohaX,self.polohaY+1) == True):
                self.otocPanaka(platno_ob, "S")
                self.animuj(platno_ob, mapa_panak.rozmerPoleX, mapa_panak.rozmerPoleY, "S",0,postava_hrace)
                pohnulSe = True
        else:
            if( vzdalenostY > 0 and mapa_panak.jePolickoPruch(self.polohaX,self.polohaY-1) == True):
                self.otocPanaka(platno_ob, "N")
                self.animuj(platno_ob, mapa_panak.rozmerPoleX, mapa_panak.rozmerPoleY, "N",0,postava_hrace)
                pohnulSe = True
            elif( vzdalenostY < 0 and mapa_panak.jePolickoPruch(self.polohaX,self.polohaY+1) == True):
                self.otocPanaka(platno_ob, "S")
                self.animuj(platno_ob, mapa_panak.rozmerPoleX, mapa_panak.rozmerPoleY, "S",0,postava_hrace)
                pohnulSe = True
            elif( vzdalenostX > 0 and mapa_panak.jePolickoPruch(self.polohaX - 1,self.polohaY) == True):
                self.otocPanaka(platno_ob, "W")
                self.animuj(platno_ob, mapa_panak.rozmerPoleX, mapa_panak.rozmerPoleY, "W",0,postava_hrace)
                pohnulSe = True
            elif( vzdalenostX < 0 and mapa_panak.jePolickoPruch(self.polohaX + 1,self.polohaY) == True):
                self.otocPanaka(platno_ob, "E")
                self.animuj(platno_ob, mapa_panak.rozmerPoleX, mapa_panak.rozmerPoleY, "E",0,postava_hrace)
                pohnulSe = True
            
        if(pohnulSe == False): self.nahodnyKrok(platno_ob, mapa_panak, postava_hrace)
        self.krok_animacni_iterace = self.krok_animacni_iterace + 1
        label_test.config(text = "Počet kroků nepřátel: " + str(self.krok_animacni_iterace))
        self.zkontrolujUlovil(postava_hrace)
        root.after(300, self.jdePoHracovi, platno_ob, mapa_panak,postava_hrace) 
    
    def zkontrolujUlovil(self,postava_hrace):
        if( abs(self.polohaX-postava_hrace.polohaX) < 1.0 and abs(self.polohaY - postava_hrace.polohaY) <1.0 and postava_hrace.sesbirano == False and postava_hrace.mrtvy == False): 
            postava_hrace.mrtvy = True
            messagebox.showinfo("Prohra", "Tygr tě chytil a sežral")
            root.destroy()
        
    
    def nahodnyKrok(self, platno_ob, mapa_panak, postava_hrace):
        nahodCislo = random.randint(1,4)
        if(nahodCislo == 1):
             self.otocPanaka(platno_ob, "E")
             if( (self.polohaX+1) >= mapa_panak.pocetPoliX):
                 pass
             elif (mapa_panak.jePolickoPruch(self.polohaX + 1,self.polohaY) == True):
                 self.animuj(platno_ob, mapa_panak.rozmerPoleX, mapa_panak.rozmerPoleY, "E",0,postava_hrace)
        elif(nahodCislo == 2):
             self.otocPanaka(platno_ob, "W")
             if( (self.polohaX-1) < 0):
                 pass
             elif (mapa_panak.jePolickoPruch(self.polohaX - 1,self.polohaY) == True):
                 self.animuj(platno_ob, mapa_panak.rozmerPoleX, mapa_panak.rozmerPoleY, "W",0,postava_hrace)
        elif(nahodCislo == 3):
             self.otocPanaka(platno_ob, "N")
             if( (self.polohaY-1) < 0):
                 pass
             elif (mapa_panak.jePolickoPruch(self.polohaX,self.polohaY-1) == True):
                 self.animuj(platno_ob, mapa_panak.rozmerPoleX, mapa_panak.rozmerPoleY, "N",0,postava_hrace)
        elif(nahodCislo == 4):
             self.otocPanaka(platno_ob, "S")
             if( (self.polohaY+1) >= mapa_panak.pocetPoliY):
                 pass
             elif (mapa_panak.jePolickoPruch(self.polohaX,self.polohaY+1) == True):
                 self.animuj(platno_ob, mapa_panak.rozmerPoleX, mapa_panak.rozmerPoleY, "S",0,postava_hrace)
        
    def nahodnaProchazka(self, platno_ob, mapa_panak, postava_hrace):
        self.nahodnyKrok(platno_ob, mapa_panak, postava_hrace)
        self.krok_animacni_iterace = self.krok_animacni_iterace + 1
        label_test.config(text = str(self.krok_animacni_iterace))
        root.after(100, self.nahodnaProchazka, platno_ob, mapa_panak) #u after se musi parametry volané funkce umístit jako další parametry after, ne do závorek za volanou funkci; after(1000, fce(param)) by totiž nejdřív volalo fce s parametrem param, to by něco vrátilo (nejčastěji None) a tohle něco by pak volala fce after
        
        
class mapap:
    planek = None
    pocetPoliY = 0
    pocetPoliX = 0
    rozmerPoleX = 1
    rozmerPoleY = 1
    tile_trava = None
    tile_skala = None
    pocetVolnychPloch = 0
    truhly = []
    sebraneTruhly = []
    volne = []
   

    def __init__(self, platno_ob, vyskaPlatna, sirkaPlatna):
        
        #self.planek = pd.read_csv("mapa.txt", header = None, sep = " ") #pro načtení mapy z disku
        self.planek = self.vygenerujPlanek()
        self.pocetPoliY = self.planek.shape[0]  #tj. počet řádků
        self.pocetPoliX = self.planek.shape[1]
        self.rozmerPoleX = round(sirkaPlatna/self.pocetPoliX)
        self.rozmerPoleY = round(vyskaPlatna/self.pocetPoliY)
        
        obrazekPIL_trava = PIIIL.Image.open("chodic_soubory\\trava.png")  #obrázek se otevře pomocí PILu
        obrazekPIL_trava = obrazekPIL_trava.resize((self.rozmerPoleX,self.rozmerPoleY))
        self.tile_trava = PIIIL.PhotoImage(obrazekPIL_trava) 
        obrazekPIL_skala = PIIIL.Image.open("chodic_soubory\\skala.png")  #obrázek se otevře pomocí PILu
        obrazekPIL_skala = obrazekPIL_skala.resize((self.rozmerPoleX,self.rozmerPoleY))
        self.tile_skala = PIIIL.PhotoImage(obrazekPIL_skala)
        for i in range (0,self.pocetPoliX):
            for j in range (0,self.pocetPoliY):
                if (self.planek[i][j] == 1):
                    platno_ob.create_image(0 + i*self.rozmerPoleX,0 + j*self.rozmerPoleY,image = self.tile_trava, anchor = NW)
                    self.pocetVolnychPloch = self.pocetVolnychPloch + 1
                elif (self.planek[i][j] == 2):
                    platno_ob.create_image(0 + i*self.rozmerPoleX,0 + j*self.rozmerPoleY,image = self.tile_skala, anchor = NW)
    
    def vygenerujPlanek(self):
        cisloX = 15
        cisloY = 15
        velikostMapyX = (cisloX//2)*2+1  #k zajištění, že mapa bude mít liché rozměry
        velikostMapyY = (cisloY//2)*2+1
        bludiste = pd.DataFrame(data = 1, index = range(velikostMapyX), columns = range(velikostMapyY)) #vytvoření dataframu plného jedniček
        #bludiste[0][:] = 2
        #bludiste[:][0] = 2
        bludiste.iloc[0,:] = bludiste.iloc[:,0]=bludiste.iloc[:,-1]=bludiste.iloc[-1,:]=2 #zastavění okrajů mapy
        
        pocetJaderZdi = 10
        pocetKrokuStaveni = 10
        for i in range(pocetJaderZdi):
            bodX = random.randint(0,velikostMapyX//2)*2 #vygenerování suého čísla, takže se nemůže stát, že do datasetu o velikosti 10 (tj. indexy 0 až 9) budu cpát hodnout souřadnice 10
            bodY = random.randint(0,velikostMapyY//2)*2
            bludiste.iloc[bodX,bodY] = 2 #vytvoření zdi v náhodném bodě
            
            for j in range(pocetKrokuStaveni):
                seznamSousedu = []
                if(bodX > 1): seznamSousedu.append([bodX-2,bodY])  #ověří se, jestli soused ob-políčko existuje (tj. jestli třeba nejsme na okraji mapy) a pokud ano, přidá se do listu
                if(bodX < bludiste.shape[1]-2):seznamSousedu.append([bodX+2,bodY])
                if(bodY > 1): seznamSousedu.append([bodX,bodY-2])
                if(bodY < bludiste.shape[0]-2):seznamSousedu.append([bodX,bodY+2])
                if (len(seznamSousedu) != 0):#pakliže list sousedů není z nějakého důvodu prázdný
                    cisloSouseda = random.randint(0, len(seznamSousedu)-1) #vybere se náhodný soused
                    novaX = seznamSousedu[cisloSouseda][0] #zjistí se jeho souřadnice
                    novaY = seznamSousedu[cisloSouseda][1]
                    if (bludiste.iloc[novaX,novaY]==1): #pokud naněm byla doposud tráva
                        bludiste.iloc[novaX,novaY]=2 #tak je tam nyní zeď
                        bludiste.iloc[novaX + (novaX-bodX)//2,novaY + (novaY-bodY)//2]=2 #a zdí se zaplácne i políčko mezi nimi
                        bodX = novaX #nové políčko se stává novým startovním políčkem a jede se do další iterace for
                        bodY = novaY
        return bludiste
        
        
    def vytvorPoklady(self):
        faktorPravdepodobnosti = 3  #pro 1 by to bylo 50:50, že na volném místě bude poklad
        seznamPokladu = [random.randint(0,faktorPravdepodobnosti) for x in range(self.pocetVolnychPloch)]
        self.sebraneTruhly = [0 for x in range(self.pocetVolnychPloch)]
        cisloMista = 0
        for i in range (0,self.pocetPoliX):
            for j in range (0,self.pocetPoliY):
                if (self.planek[i][j] == 1 and seznamPokladu[cisloMista] == 0):
                    self.truhly.append(predmet(platno,i,j,self.rozmerPoleX, self.rozmerPoleY))
                    cisloMista = cisloMista + 1
                elif (self.planek[i][j] == 1):
                    cisloMista = cisloMista + 1
                    self.volne.append([i,j])
                    
    def vytvorStartLokHrace(self):
        pocetVolnych = len(self.volne)
        cisloLokace = random.randint(1,pocetVolnych) - 1
        lokHrace = self.volne[cisloLokace]
        self.volne.pop(cisloLokace)
        return lokHrace

    def vytvorStartLokPotvory(self):
        pocetVolnych = len(self.volne)
        cisloLokace = random.randint(1,pocetVolnych) - 1
        lokPotvory = self.volne[cisloLokace]
        self.volne.pop(cisloLokace)
        return lokPotvory
    
    def jePolickoPruch(self, sourX,sourY):
        if(self.planek[sourX][sourY] == 1): return True
        elif(self.planek[sourX][sourY] == 2): return False

class predmet:
    sprit_predmet = None
    polohaX = 0
    polohaY = 0
    naMape = None
    
    def __init__(self, platno_ob, souradX, souradY, rozmerPoleX, rozmerPoleY):
        obrazekPIL_predmet = PIIIL.Image.open("chodic_soubory\\poklad.png")  #obrázek se otevře pomocí PILu
        obrazekPIL_predmet = obrazekPIL_predmet.resize((rozmerPoleX,rozmerPoleY))
        self.sprit_predmet = PIIIL.PhotoImage(obrazekPIL_predmet)
        self.polohaX = souradX
        self.polohaY = souradY
        self.naMape = platno_ob.create_image(0 + self.polohaX*rozmerPoleX,0 + self.polohaY*rozmerPoleY,image = self.sprit_predmet, anchor = NW)#samotné vytvoření objektu na canvasu
        
    def znicPredmet(self, platno_ob):
        platno_ob.delete(self.naMape)
        
        
def zkontroluj(platno):
   for i in range(len(novaMapa.truhly)):
        if( (hrac.polohaX == novaMapa.truhly[i].polohaX) and (hrac.polohaY == novaMapa.truhly[i].polohaY) and (novaMapa.sebraneTruhly[i] == 0) ):
            novaMapa.sebraneTruhly[i] = 1
            novaMapa.truhly[i].znicPredmet(platno)
            hrac.sesbiranychPokladu = hrac.sesbiranychPokladu + 1
            label_poklady.config(text = str(hrac.sesbiranychPokladu) + "/" + str(len(novaMapa.truhly))   )
            if(hrac.sesbiranychPokladu == len(novaMapa.truhly)):
                hrac.sesbirano = True
                messagebox.showinfo("Výhra", "Sesbíral jsi všechny poklady")
                root.destroy()

#dat kotrolu, jestli se nevylezlo z mapy, a pokud ne, prekreslit pandulaka
def prava(event):
    hrac.otocPanaka(platno, "E")
    if( (hrac.polohaX+1) >= novaMapa.pocetPoliX):
        pass
    elif (novaMapa.jePolickoPruch(hrac.polohaX + 1,hrac.polohaY) == True):
        hrac.polohaX = hrac.polohaX + 1
        hrac.pohniPanaka(platno,novaMapa.rozmerPoleX,novaMapa.rozmerPoleY)
    zkontroluj(platno)
def leva(event):
    hrac.otocPanaka(platno, "W")
    if( (hrac.polohaX-1) < 0):
        pass
    elif (novaMapa.jePolickoPruch(hrac.polohaX - 1,hrac.polohaY) == True):
        hrac.polohaX = hrac.polohaX - 1
        hrac.pohniPanaka(platno,novaMapa.rozmerPoleX,novaMapa.rozmerPoleY)
    zkontroluj(platno)
def nahoru(event):
    hrac.otocPanaka(platno, "N")
    if( (hrac.polohaY-1) < 0):
        pass
    elif (novaMapa.jePolickoPruch(hrac.polohaX,hrac.polohaY-1) == True):
        hrac.polohaY = hrac.polohaY - 1
        hrac.pohniPanaka(platno,novaMapa.rozmerPoleX,novaMapa.rozmerPoleY)
    zkontroluj(platno)
def dolu(event):
    hrac.otocPanaka(platno, "S")
    if( (hrac.polohaY+1) >= novaMapa.pocetPoliY):
        pass
    elif (novaMapa.jePolickoPruch(hrac.polohaX,hrac.polohaY+1) == True):
        hrac.polohaY = hrac.polohaY + 1
        hrac.pohniPanaka(platno,novaMapa.rozmerPoleX,novaMapa.rozmerPoleY)
    zkontroluj(platno)


root = Tk()
root.geometry("600x500")  #nastavení velikosti okna v pixelech#root.resizable(width = False, height = False)  #aby byla fixovaná velikost okna
root.title("Poklady")
mainframe = ttk.Frame(root)
mainframe["relief"] = "sunken"
mainframe['borderwidth'] = 5
mainframe.grid(column = 1, row = 0)  #Bez tohodle se mainframe nezobrazí!!

sirkaPlatna = 600
vyskaPlatna = 450
platno = Canvas(mainframe, width = sirkaPlatna, height = vyskaPlatna)
platno.grid(column = 0, row = 0)  #Bez tohodle se platno nezobrazí!!

platno.focus_set()    #bez focusu by to nevnimalo klavesnici
platno.bind("<Right>",prava)
platno.bind("<Left>",leva)
platno.bind("<Up>",nahoru)
platno.bind("<Down>",dolu)

novaMapa = mapap(platno, vyskaPlatna, sirkaPlatna)
novaMapa.vytvorPoklady()
hrac = hracova_postava(platno,novaMapa.vytvorStartLokHrace(),novaMapa.rozmerPoleX, novaMapa.rozmerPoleY, "hrac")
tygr = nepritel(platno,novaMapa.vytvorStartLokPotvory(),novaMapa.rozmerPoleX, novaMapa.rozmerPoleY, "tygr")
tygr2 = nepritel(platno,novaMapa.vytvorStartLokPotvory(),novaMapa.rozmerPoleX, novaMapa.rozmerPoleY, "tygr")

label_poklady = ttk.Label(mainframe, text = "Sebrane poklady/Pokladu celkem")
label_poklady.grid(column = 0, row = 1)
label_test = ttk.Label(mainframe, text = "Zacatek")
label_test.grid(column = 0, row = 2)
tygr.jdePoHracovi(platno, novaMapa, hrac)
tygr2.jdePoHracovi(platno, novaMapa, hrac)

root.mainloop()