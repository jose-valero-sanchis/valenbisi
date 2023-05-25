# -*- coding: utf-8 -*-

import requests
import json
import pandas as pd

fin = '2023-03-01'
estacion = '8416Y'

url = f"https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/2022-12-01T00:00:00UTC/fechafin/{fin}T23:59:59UTC/estacion/{estacion}/"

querystring = {"api_key":"your_api_key"}

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

d = json.loads(response.text)
url = d['datos']

data = requests.get(url)
l_dic = json.loads(data.text)

df = pd.DataFrame(l_dic)
df.to_csv('aemet_data.csv', index=False)
