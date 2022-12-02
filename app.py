# from controller.repositorio import exportarDatos, saludable
# from controller.imprimir import imprimir
# https://www.microsoft.com/en-us/download/details.aspx?id=53587

#tensorflow

import datetime
import json
from flask import Flask, request
from flask_restful import Resource,Api
from flask_cors import CORS
from flask import Flask


from controller.control import obtenerVersion
from controller.mimodelo import obtenerSentimiento

app = Flask(__name__)


app = Flask(__name__)

print('Sistema de automatizacion de obtencion de datos para las base de bronce')
print('No apto para produccion, solo para pruebas')

cors = CORS(app, resources={r"*": {"origins": "*"}})
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

api = Api(app)

# #Chequiar la salud del contenedor
api.add_resource(obtenerVersion, '/')
api.add_resource(obtenerSentimiento, '/modelo')


_PORT = 30001
if __name__ == '__main__':
    print(f'Systran - Modulo DAC# en el puerto {_PORT} Listo!!!!!!!!')
    app.run(port=_PORT,host='0.0.0.0',debug=True)


#Para que pueda entrar con angular
# @app.after_request
# def after_request(response):
#   header = response.headers
#   header['Access-Control-Allow-Origin'] = '*'
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', '*')
#   response.headers.add('Access-Control-Allow-Methods', '*')
#   return response