import dispositivo
import pandas as pd
def set_up(app):
    DEVICES=[]
    [app.MGC_value.get(),app.Lakeshore_value.get(),app.Si155_value.get(),app.Vaccum_value.get()]
    Address_ID=1
    if app.MGC_value.get():
        MGC=pd.read_csv('.\\configurations\\MGC_plus.txt',sep=';')
        server_address=MGC.Valor.values[0]
        server_port=int(MGC.Valor.values[1])
        active_channels=[int(ch) for ch in MGC.Valor.values[2].split(',')]
        active_subchannels=[int(ch) for ch in MGC.Valor.values[3].split(',')]
        print(server_address,server_port,active_channels,active_subchannels,MGC.Valor.values[3].split(','))
        DEVICES.append(dispositivo.MGCPlus(Address_ID,server_address,server_port,active_channels,active_subchannels))
        Address_ID+=1

    if app.Vaccum_value.get():
        P=pd.read_csv('.\\configurations\\pressure.txt',sep=';')
        Baud_rate=int(P.Valor.values[0])
        port=str(P.Valor.values[1])
        DEVICES.append(dispositivo.Pressure(Address_ID,Baud_rate,port,'pressure'))
    return DEVICES
