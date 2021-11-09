import pydbus
import bluetooth

#Del codigo de la entrega anterior creamos una 'libreria' de funciones 
#donde ya se define las acciones que se llevaran a cabo dentro de la interfaz grafica


global dispositivos #Variable global para guardar una lista de dispositivos disponibles previamente escaneados

#Esa es la funcion que busca los dispositivos cercanos para conectarse, es parecido al codigo de la entrega anterior pero con algunos cambios
def consulta():
    global dispositivos
    print("Inicializando escaneo de dispositivos para conectrarse\n")
    dispositivos = bluetooth.discover_devices(duration=8, lookup_names=True,flush_cache=True, lookup_class=False)
    if len(dispositivos)>0:
        print(f"Se encontraron {len(dispositivos)}")
        cont=0
        for x in dispositivos:
            print(f"disp. no{cont} es: {x}\n")
            cont=+1
    else:
        print("No se encontro ningun dispositivo disponible\n")
   
    return dispositivos
#Aqui es donde se envia una tupla con la direccion y el nombre del dispositivo al que nos queremos conectar
def conexion(connecte):
    print(connecte[0])
    audio_dev = connecte[0]
    adapter_path = '/org/bluez/hci0'
    device_path = f'{adapter_path}/dev_{audio_dev.replace(":", "_")}'

    bluez_service = 'org.bluez'
    bus = pydbus.SystemBus()
    adapter = bus.get(bluez_service, adapter_path)
    device = bus.get(bluez_service, device_path)

    device.Connect()
    print(f"Dispositivo {connecte[1]} conectado\n")
#Para tomar la variable de dispositivos
def getdisps():
    global dispositivos
    return dispositivos;

