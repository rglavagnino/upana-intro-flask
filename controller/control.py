from controller.imprimir import salida,imprimir
from flask_restful import Resource
import json
# from controller.version import obtenerActivo

class obtenerVersion(Resource):
    def get(self):
        imprimir('Entrando a revisar la version ')
        dev = json.dumps([{'version':"0.0.1", "nombre":"chocolate"}])
        dev = json.loads(dev)
        retorno = salida('EXITO', 'Se pudo obtener la version',dev)
        return retorno , 501

    def post(self):
        retorno = salida('ERROR', 'No implementado',[])
        return retorno , 501