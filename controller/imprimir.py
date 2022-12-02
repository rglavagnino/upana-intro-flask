import logging
import datetime

def imprimir(msg):
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.info(msg)
    fecha = datetime.datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
    print(f'{fecha} - {msg}')

def salida(exito, msg, data):
    salida = {
        'ESTADO': exito
        ,'MENSAJE': msg
        ,'DATA':data
    }
    return salida