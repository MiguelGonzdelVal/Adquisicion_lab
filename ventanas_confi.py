
import tkinter as tk
from tkinter import ttk
import pandas as pd

class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("SETUP")
        self.MGC_value = tk.BooleanVar(self)
        self.MGCplus = ttk.Checkbutton(self, text="MGCPlus",variable=self.MGC_value)
        self.MGCplus.grid(row=0,column=0)

        self.Lakeshore_value = tk.BooleanVar(self)
        self.Lakeshore = ttk.Checkbutton(self, text="Lakeshore",variable=self.Lakeshore_value)
        self.Lakeshore.grid(row=1,column=0)

        self.Si155_value = tk.BooleanVar(self)
        self.Si155 = ttk.Checkbutton(self, text="LUNA SI155",variable=self.Si155_value)
        self.Si155.grid(row=2,column=0)

        self.Vaccum_value = tk.BooleanVar(self)
        self.Vaccum = ttk.Checkbutton(self, text="Vaccum sensor",variable=self.Vaccum_value)
        self.Vaccum.grid(row=3,column=0)

        self.MGCplus_conf=ttk.Button(self, text ="Config", command = lambda:self.emergente_guardar('.\\configurations\\MGC_plus.txt')).grid(row=0,column=4) 
        self.Vaccum_conf=ttk.Button(self, text ="Config", command =lambda:self.emergente_guardar('.\\configurations\\pressure.txt')).grid(row=3,column=4) 

        
        self.place(width=300, height=200)

        #defino ahora los botones:
        
        
    def emergente_guardar(self,a):

        #primero se leen las caracteristicas del MGCplus:
        MGC=pd.read_csv(a,sep=';')
        def guardar():
            for i in MGC.index:
                MGC['Valor'].loc[i]= entradas[i].get()
            print(MGC)
            MGC.to_csv(a,sep=';',index=False)

        ventana=tk.Tk()
        nombres=[]
        entradas=[]
        valores=[]
        valor=tk.StringVar()
        for i in MGC.index:
           nombres.append(ttk.Label(ventana, text=MGC.Variable.loc[i]).grid(row=i,column=0))
           valor.set(str(MGC.Valor.loc[i]))
           actual=str(MGC['Valor'].loc[i])
           valores.append(tk.StringVar())
           #
           entradas.append(ttk.Entry(ventana,textvariable=valores[-1]))
           entradas[-1].grid(row=i,column=1)
           entradas[-1].insert(0,actual)
           
        ttk.Button(ventana,command=guardar,text='Save').grid(column=3)

     
           
           
        ventana.mainloop()
        
class Ventana_parada(object):
    def __init__(self):
        import tkinter as tk
        print('pulsar rec para comenzar')
        self.grabar=False
    def ejecutar(self):
        
        ventana=tk.Tk()
        boton_parada=ttk.Button(ventana, text ="STOP", command = lambda:self.stop()).grid(row=0,column=0)
        boton_rec=ttk.Button(ventana, text ="REC", command = lambda:self.rec()).grid(row=0,column=1)
        ventana.mainloop()
    def rec(self):
        self.grabar=True
    def stop(self):
        self.grabar=False
    
        




        
