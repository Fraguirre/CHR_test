# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 23:39:54 2023

@author: BEAST OF DARKNESS
"""

import requests
import json
import pandas as pd

def obtiene_datos_api():
    api_url = "http://api.citybik.es/v2/networks/bikesantiago"
    response = requests.get(api_url)
    
    json_response = response.json()
    
    # Convertir la respuesta en formato JSON en un DataFrame
    df = pd.json_normalize(json_response['network'])
    df = df.drop(['stations'],axis = 1)

    return df

        
def obtiene_estaciones():
    # Realizar solicitud HTTP y obtener la respuesta en formato JSON
    response = requests.get('http://api.citybik.es/v2/networks/bikesantiago')
    json_response = response.json()
    
    # Obtener la lista de estaciones
    stations = json_response['network']['stations']
    
    # Convertir la lista en un DataFrame de Pandas
    df = pd.json_normalize(stations, sep='_')
    
    return df
