# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 17:20:00 2023

@author: javil
"""

import os
import csv

carpetas = os.listdir('./Datos_descomp')
for carpeta in carpetas:
    csvs = os.listdir('./Datos_descomp/'+carpeta)
    with open('bbdd.csv', 'a', encoding='utf-8', newline='') as basedatos:
        writer = csv.writer(basedatos, delimiter=';')
        for csvi in csvs:
            with open('./Datos_descomp/'+carpeta+'/'+csvi, 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                cabecera = 0
                for row in reader:
                    if cabecera == 0:
                        cabecera += 1
                        continue
                    writer.writerow(row)