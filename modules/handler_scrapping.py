from time import sleep
import random



def handler_scrapping(driver):     
   
    id = driver.find_element_by_xpath('//input[@name="cedula"]')
    id.clear()
    cedula = int(input("\n\nIntroduzca su cedula: \n\n"))
    id.send_keys(cedula)
    sleep(random.uniform(1.0,2.0))

    button = driver.find_element_by_xpath('//input[@title="Buscar"]')
    button.click()
    print("Buscando")

    sleep(random.uniform(2.0,3.0))

    register = driver.find_elements_by_xpath('//td[@align="left"]')
    
    person_dates = [] 
    dates = []


    assert len(register) == 22,"No se encontraron resultados, esto puede deberse a que introdujo una cedula invalida o inexistente"

   
   
    for date in register[:14]:
        date_person = date.text
        person_dates.append(date_person)

    for i in range(1,11,2):
        dates.append(person_dates[i])

    print("\n\nDATOS\n\n",dates)
    id.clear()
    return dates