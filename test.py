from time import sleep
from pandas.core.algorithms import mode
from selenium import webdriver
import random
import json
import pandas as pd
import numpy as np
from datetime import datetime
import pytz


def reading(file):
    df = pd.read_csv(file,index_col=0)
    print(df)




def time_function():
    caracas_tz = pytz.timezone("America/Caracas") 
    caracas_date = datetime.now(caracas_tz) 
    time_zone = caracas_date.strftime("%d/%m/%y %H:%M:%S")
    print("Caracas: ",time_zone ) 
    time_zone = caracas_date.strftime("%d_%m_%y_%H%M%S")
    return time_zone


def handler_files(df,m_w):
    
    time = time_function()
    name_csv = 'files_data/'+"Reporte_"+time+'.csv'
    df.to_csv(name_csv,mode=m_w)
    print("Archivo creado: ", name_csv)
    return name_csv
 



options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('./chromedriver.exe',chrome_options=options)
driver.get('https://covid19-api.com/docs')
print("\n\nPagina lista\n\n")
sleep(random.uniform(2.0,3.0))


def scrapping(driver,label_cntry,label_tout,label_exc,label_scrp): # label_cname etiqueta para buscar por pais
    b_all_coun = driver.find_element_by_xpath(label_cntry).click()
    sleep(random.uniform(1.0,2.0))
    b_try_out = driver.find_element_by_xpath(label_tout).click()
    sleep(random.uniform(1.0,2.0))
    excute = driver.find_element_by_xpath(label_exc).click()
    sleep(random.uniform(4.0,5.0))
    scrapping = driver.find_elements_by_xpath(label_scrp)
    #print("\n\n",type(scrapping),len(scrapping))

    elements = scrapping[0].text
    #print("\n\n",type(elements),len(elements))
    return elements

# Por pais
"""
label_cntry ='//div[@id="operations-Country-getLatestCountryDataByName"]'
label_tout = '//button[@class="btn try-out__btn"]'
label_cname = '//input[@placeholder="name - Name of the country"]'
label_exc = '//button[@class="btn execute opblock-control__btn"]'
label_scrp = '//div[@class="highlight-code"]'

"""


# Todos los paises




label_cntry ='//div[@id="operations-Country-getLatestAllCountries"]'
label_tout = '//button[@class="btn try-out__btn"]'
label_exc = '//button[@class="btn execute opblock-control__btn"]'
label_scrp = '//div[@class="highlight-code"]'

elements = scrapping(driver,label_cntry,label_tout,label_exc,label_scrp)
   

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

    sleep(1)
    n_df = np.array(list_data)
    df= pd.DataFrame(n_df,columns=["confirmados","recuperados","criticos","muertos"],index=[country]) 
    file_name = handler_files(df,'w')
    sleep(1)
    print("Paises guardados exitosamente")
    sleep(1)
    print("Reporte: ")
    reading(file_name)
 

df = clean_data(elements)
    






   