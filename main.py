import dispositivo
import threading
import time
import datetime
from tkinter import filedialog
import tkinter as tk
import pickle
import subprocess
import socket
import ventanas_confi
import config
#INPUTS

main_window = tk.Tk()
app = ventanas_confi.Application(main_window)
app.mainloop()

Objetos=config.set_up(app)
ventana=tk.Tk()
archivo=filedialog.asksaveasfile(parent=ventana)
ventana.mainloop()


subprocess.Popen(['python','dibujo.py'])
s = socket.socket()        
s.connect(('localhost', 12345))


#sampling time
t_s=1
#recording time
t_rec=10

it_rec =int(t_rec//t_s)




file_name = archivo.name


server_address='192.168.1.124'
server_port = 7
active_channels=[3]
active_subchannels=[1]

#objeto=dispositivo.LUNA_Si155(3,'10.0.0.55',[1,2],1,False)
#print(objeto.lambda_0)
#objeto=dispositivo.Lakeshore_218(2,9600,'COM4',[1,2,3],['CERNOX','CERNOX','CERNOX'])

HILOS=[threading.Thread(target=objeto.DAQ) for objeto in Objetos]
for hilo in HILOS:hilo.start()

file= open(file_name,'w')
file.close()
save_it=0
texto=''
Parada=ventanas_confi.Ventana_parada()
hilo_stp=threading.Thread(target=Parada.ejecutar).start()

while True:
    if Parada.grabar:
        save_it+=1
        muestra=[str(datetime.datetime.now())]
        for objeto in Objetos:
            datos=objeto.get_data()
            if type(datos)==list:
                
                for dato in datos:muestra.append(dato)
        lectura=pickle.dumps(muestra)	
        try:s.send(lectura)
        except:pass
        print(muestra)
        texto+=str(muestra).replace('[','').replace(']','\n')
        if save_it==it_rec:
            file= open(file_name,'a')
            file.write(texto)
            file.close()
            save_it=0
            texto=''
        
        time.sleep(0.2)
    if not Parada.grabar:
        if len(texto)>0:
            file= open(file_name,'a')
            file.write(texto)
            file.close()
            save_it=0
            texto=''
            
        


