from time import sleep
import json
import pandas as pd
import numpy as np
from modules.handler_files import handler_files,reading


def data_treatment(json_data,list_values,list_countries):
    values = list(json_data.values())
    values.pop(1)
    country = values.pop(0)
    list_countries.append(country)
    data = values[:4]
    list_values.append(data)
    return list_values,list_countries


def clean_data(elements):
    lim = len(elements)-3
    elements = elements[15:lim].strip()+"}"
    i1 = 0
    v = ""
    list_values = []
    list_countries = []

    print("\nExtrayendo datos \n")
    
    for x in elements.split("{"):
        v = x.strip()
        v_1 = v.strip(',')
        v_2 = v_1.strip('}')
        v_3 = v_2.strip()
        v_4 = v_3.strip()
        v_5 = v_4.strip()
        v_6 = v_5.rstrip()
        v_7 = "{"+v_6+"}"
        i1 += 1 

        json_data= json.loads(v_7)
        list_data,country = data_treatment(json_data,list_values,list_countries)

    print("\n\nDatos extraidos exitosamente\n\n")
    sleep(1)
    n_df = np.array(list_data)
    df= pd.DataFrame(n_df,columns=["confirmados","recuperados","criticos","muertos"],index=[country]) 
    file_name = handler_files(df,'w')
    sleep(1)
    print("\nPaises guardados exitosamente\n")
    sleep(1)
    print("\nReporte: ")
    reading(file_name)