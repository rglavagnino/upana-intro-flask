from flask_restful import Resource
from controller.imprimir import salida,imprimir
from flask import request
from tensorflow.keras.models import load_model
import numpy as np
import joblib

import datetime
import json

class obtenerSentimiento(Resource):
    def post(self):
        if 'Authorization' not in request.headers:
            return salida('ERROR', 'No esta identificado',''),401
        token = request.headers['Authorization']
        if token != 'upana for the win':
            return salida('ERROR', 'Contraseña equivocada',''),401
        # print()]
        # sent = request.json["como_me_siento"]
        print(request.json)
        s_len = request.json["sepal_longitud"]
        s_wid = request.json["sepal_ancho"]
        p_len = request.json["petal_longitud"]
        p_wid = request.json["petal_ancho"]
    
        flor = [[s_len,s_wid,p_len,p_wid]]
        model = load_model("controller/modelos/iris.h5")
        scaler = joblib.load("controller/modelos/scaler.pkl")
        scaler.clip = False
        flower = scaler.transform(flor)
    
        clase = np.array(['setosa', 'versicolor', 'virginica'])
        

        class_ind=model.predict(flower) 
        clased=np.argmax(class_ind,axis=1)

        print(clased)
#         import joblib
# joblib.dump(scaler,'iris_scaler.pkl')


#pip3 install -U scikit-learn scipy matplotlib
        retorno = salida('EXITO', 'Este es una flor ' + clase[clased][0]  ,[{"clase":clase[clased][0]}])
        return retorno , 501
    
    def get(self):
        retorno = salida('ERROR', 'No implementado',[])
        return retorno , 501
    
    def put(self):
        retorno = salida('ERROR', 'No implementado',[])
        return retorno , 501
    
    def patch(self):
        retorno = salida('ERROR', 'No implementado',[])
        return retorno , 501

    def delete(self):
        retorno = salida('ERROR', 'No implementado',[])
        return retorno , 501