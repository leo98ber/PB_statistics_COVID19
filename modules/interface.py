from time import sleep
from selenium import webdriver
import random
from modules.handler_scrapping import scrapping
from modules.data import clean_data


def interface():

    """
    
    INSTRUCCIONES:

    Este es un script simple, al ejecutarse se extraen datos de la web, espesificamente las estadisticas por paises de
    personas confirmadas, en estado critico, muertas y recuperadas por COVID19. Al extraer los datos se guardan en formato pandas
    generando un reporte con la fecha y hora de la ejecucion del programa.

    
    """


    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome('./chromedriver.exe',chrome_options=options)
    driver.get('https://covid19-api.com/docs')
    print("\n\nPagina Cargada\n\n")
    sleep(random.uniform(2.0,3.0))


    label_cntry ='//div[@id="operations-Country-getLatestAllCountries"]'
    label_tout = '//button[@class="btn try-out__btn"]'
    label_exc = '//button[@class="btn execute opblock-control__btn"]'
    label_scrp = '//div[@class="highlight-code"]'
    elements = scrapping(driver,label_cntry,label_tout,label_exc,label_scrp)

    df = clean_data(elements)

   


 
 
