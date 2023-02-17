# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 23:07:58 2023

@author: Francisco Aguirre Rojas
"""

from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import resolve
from django.http import HttpResponseRedirect
import pandas as pd
import datetime
from modules import api_connection

def index(request):
    context = {}
    data = api_connection.obtiene_datos_api()
    estaciones = api_connection.obtiene_estaciones()
    
    context['data']=[data.to_html(
        classes='table style-1 dt-table-hover non-hover zero-config', 
        header=True,
        border="0",
        justify='center',
        index=False,
        escape=False
        )]
    
    context['estaciones']=[estaciones.to_html(
        classes='table style-1 dt-table-hover non-hover zero-config', 
        header=True,
        border="0",
        justify='center',
        index=False,
        escape=False
        )]
    return render(request, "index.html", context)