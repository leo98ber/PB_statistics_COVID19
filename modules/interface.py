from modules import persons,donwload,handler_files
from time import sleep
from selenium import webdriver
import random



data_base = ["cedula","nombre","estado","municipio","parroquia"]
file_name = "base_de_datos.csv"

def interface():

    """INSTRUCCIONES:


    
    Introduzca C para registrar una persona de la base de datos del CNE en la base de datos (o base de archivos), debera ingresar el 
    numero de cedula como un numero entero y este software se encara de encontrar la informacion correspondiente al documento de
    identidad indicado


    Introduzca R para acceder a las opciones de visualizaciones de clientes las cuales se presentan a continuacion:

        * list_persons: Muestra todos los ciudadanos del sistema electoral almacenados en la base de archivos local
    
        * filter_persons: Mediante una etiqueta o item se puede filtrar a los ciudadanos segun su informacion en el sistema electral
         y se obtiene una nueva lista con los clientes que cumplen con los requerimientos indicados para el tag seleccionado, estos 
         items o tags validos son cedula,nombre,estado,municipio,parroquia,centro y direccion. Un punto importante a resaltar es que 
         la cedula de identidad de estar en la forma V- o E- del mismo de lo contrario

        *person: Muestra la informacion del ciudadano una vez indicada la cedula de identidad en la forma V- o E- del mismo
        de lo contrario

    Introduzca D para eliminar a un ciudadano segun su cedula en la forma V- o E-.

    NOTA: Se resalta la importancia de indicar la cedula identidad de la forma V-xxxxxx en las funciones locales del software, a excepcion
    de cuando se extrae datos de la pagina que solo se permiten formatos int (enteros). La razon es por que el sistema del CNE entrega los 
    datos de esta forma. Esto no solo aplica con el documento de identidad, si no tambien para los otros items en el caso de que se quieran
    usar como filtro deberan tener la misma forma que en el sistema del CNE
    
    """

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome('./chromedriver.exe',chrome_options=options)
    driver.get('http://www.cne.gob.ve/web/index.php')
    print("\n\nPagina lista\n\n")
    sleep(random.uniform(1.0,2.0))

    while True: 
        handler = handler_files.Handler_fields(file_name,data_base)
        info_client = donwload.Field_exist(file_name,data_base)
        person = persons.Person(handler,info_client,driver)
        module = input('\nIndique la modalidad o presione "q" para escapar:\n')
        module = module.upper().strip()

        if module == 'C':
            person.create()            

        elif module == 'R':
            person.read()

        elif module == 'D':
            person.delete()

        elif module == 'Q':
            break

        else:
            print("\nError usted introdujo una opcion invalida intente de nuevo\n")

 
