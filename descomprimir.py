# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 16:40:33 2023

@author: javil
"""

import zipfile
import os

zips = os.listdir('./Datos')
pref = './Datos'
for r in zips:
    ruta = pref+'/'+r
    ruta_extraccion = './Datos_descomp/Desc'+r
    password = None
    archivo_zip = zipfile.ZipFile(ruta, "r")
    try:
        archivo_zip.extractall(pwd=password, path=ruta_extraccion)
    except:
        pass
    archivo_zip.close()


