import tkinter as tk
from tkinter import LabelFrame, filedialog
from tkinter import IntVar
from typing import Text
from pygame import mixer

class Aplicacion(tk.Frame):

    def __init__(self,master = None):
        self.master = master
        super().__init__(master)
        self.pack()
        mixer.init()
        self.crearWidgets()

    def crearWidgets(self):
        self.selec = tk.Button(self,text="Seleccionar cancion", command= lambda:self.seleccionarCancion())
        self.selec.grid(row = 0, column= 0)

        self.pausa = tk.Button(self,text = "Pausar",command= lambda: mixer.music.pause())
        self.pausa.grid(row = 1, column= 0)

        self.reanudar = tk.Button(self,text = "Reanudar",command= lambda: mixer.music.unpause())
        self.reanudar.grid(row = 2, column= 0)

        self.spinbox = tk.Spinbox(self,from_=0.0, to=1.0,increment=0.1,command= lambda: mixer.music.set_volume(float(self.spinbox.get())))
        self.spinbox.grid(row = 3 ,column = 0)

        self.exit = tk.Button(self, text = "Salir", command= lambda:self.salir())
        self.exit.grid(row = 4, column= 0)


    def seleccionarCancion(self):
        self.cancion = filedialog.askopenfilename(title = "Seleccionar cancion",filetypes=(('Archivos de musica MP3','*.mp3'),('Todos los archivos','*.*')))
        mixer.music.load(self.cancion)
        mixer.music.play()
        mixer.music.set_volume(0.5)

    def salir(self):
        mixer.music.stop()
        self.destroy()
        self.master.destroy()
    
root = tk.Tk()
root.resizable(0,0)
app = Aplicacion(master=root)
app.mainloop()