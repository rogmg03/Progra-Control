#Programacion en POO de Robot "Larry"
import os
import time
from tkinter import *
import pygame
import threading
from threading import Thread
import serial
pygame.mixer.init()
#ventana principal
ventana_principal=Tk()
ventana_principal.title("Larry")
ventana_principal.geometry("1000x600+300+0")
ventana_principal.resizable(width=NO,height=NO)
#contenedor principal
contenedor_principal=Canvas(ventana_principal,width=1000,height=600,bg="#657392")
contenedor_principal.place(x=0,y=0)
#cargar imagen
#funcion para cargar una imagen
global musica
musica=True
def cargarimagen(nombre):
    ruta = os.path.join("Imagenes",nombre)
    imagen = PhotoImage(file=ruta)
    return imagen
def fin():
        imagen=cargarimagen("Larry.gif")
        animacionl.config(image=imagen)
        time.sleep(999)
        return fin()
#Clase Larry
class Larry:
    def __init__(self):
        self.posicionx=350
        self.posiciony=150
        self.imagen="Larry.gif"
        self.cancion=None
        self.volumen=pygame.mixer.music.set_volume(0.5)
    def set_derecha_posicionx(self):
        self.posicionx+=15
    def set_izquierda_posicionx(self):
        self.posicionx-=15
    def aumentar_posiciony(self):
        self.posiciony-=10
    def reducir_posiciony(self):
        self.posiciony+=11
    def set_imagen(self,name):
        self.imagen=name
    def set_volumen(self):
        self.volumen+=0.05
    def set_cancion(self,name):
        self.cancion=pygame.mixer.music.load(name)
        
    def mover_derecha(self):
        for x in range(16):
            self.set_imagen("Derecha"+str(x)+".gif")
            imagen=cargarimagen(self.imagen)
            animacionl.config(image=imagen)
            self.set_derecha_posicionx()
            animacionl.place(x=self.posicionx,y=self.posiciony)
            time.sleep(0.1)
        return fin()
    def mover_izquierda(self):
        for x in range(15,-1,-1):
            self.set_imagen("Derecha"+str(x)+".gif")
            imagen=cargarimagen(self.imagen)
            animacionl.config(image=imagen)
            self.set_izquierda_posicionx()
            animacionl.place(x=self.posicionx,y=self.posiciony)
            time.sleep(0.1)
        return fin()
    def reproducir(self):
        self.set_cancion("cancion.mp3")
        self.cancion
        pygame.mixer.music.play()
    def detener(self):
        self.set_cancion("cancion.mp3")
        self.cancion
        pygame.mixer.music.stop()
    def presentar(self):
        self.set_cancion("saludo.wav")
        self.cancion
        pygame.mixer.music.play()
    def saludar(self):
        for x in range(1,26):
            self.set_imagen("Saludo"+str(x)+".gif")
            imagen=cargarimagen(self.imagen)
            animacionl.config(image=imagen)
            animacionl.place(x=self.posicionx,y=self.posiciony)
            time.sleep(0.1)
        return fin()
    def cohete(self):
        for x in range(29):
            self.set_imagen("cohete"+str(x)+".gif")
            imagen=cargarimagen(self.imagen)
            animacionl.config(image=imagen)
            if x<15:
                self.aumentar_posiciony()
                animacionl.place(x=self.posicionx,y=self.posiciony)
                time.sleep(0.1)
            elif x>=15:
                self.reducir_posiciony()
                animacionl.place(x=self.posicionx,y=self.posiciony)
                time.sleep(0.1)
        return fin()
    def musica(self):
        global musica
        if musica==True:
            self.reproducir()
        else:
            self.detener()
        musica=not musica

    def moverf(self):
        derecha=Thread(target=self.mover_derecha,args=())
        return derecha.start()
    def izquierdaf(self):
        izquierda=Thread(target=self.mover_izquierda,args=())
        return izquierda.start()
    def presentarf(self):
        self.presentar()
        presentart=Thread(target=self.saludar,args=())
        return presentart.start()
    def cohetef(self):
        cohetet=Thread(target=self.cohete,args=())
        return cohetet.start()

Larry=Larry()
imagen=cargarimagen("Larry.gif")
animacionl=Label(ventana_principal,bg="#657392",image=imagen)
animacionl.place(x=Larry.posicionx,y=Larry.posiciony)
ser=serial.Serial("COM3",baudrate=9600,timeout=1)
arduinoData=ser.readline().decode("ascii")
while 1:
    if arduinoData=="1":
        Larry.moverf()
    if arduinoData=="2":
        larry.izquierdaf()
    if arduinoData=="3":
        Larry.cohetef()
    if arduinoData=="4":
        Larry.presentarf()
    if arduinoData=="5":
        Larry.musica()

mainloop()
