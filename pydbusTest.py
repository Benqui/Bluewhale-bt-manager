#las librerias que estamos usando
import pydbus
import bluetooth


print("Inicializando escaneo de dispositivos para conectrarse\n")
#Este cubre el primer punto que es buscar los dispositivos cercanos para conectarse
dispositivos = bluetooth.discover_devices(duration=8, lookup_names=True,flush_cache=True, lookup_class=False)
#Despiega los dispositivos conectados
print(f"Se encontraron {len(dispositivos)}")
cont=0
for x in dispositivos:
    print(f"disp. no{cont} es: {x}\n")
    cont=+1

if len(dispositivos)>0:
    option= int(input("A que dispositivo te quieres conectar?\t"))
    #Seleccionamos el disposivo al que nos queremos conectar Que es el punto 2
    connecte=dispositivos[option]

    print(connecte[0])
    #Conexion del dispositivo 
    audio_dev = connecte[0]
    adapter_path = '/org/bluez/hci0'
    device_path = f'{adapter_path}/dev_{audio_dev.replace(":", "_")}'

    bluez_service = 'org.bluez'
    bus = pydbus.SystemBus()
    adapter = bus.get(bluez_service, adapter_path)
    device = bus.get(bluez_service, device_path)

    #device.Pair()
    device.Connect()
    print("Dispositivo conectado")#Si este mensaje no sale y sale un error no hay conexion
else:
    print("No hay dispositivos")



