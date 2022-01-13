from time import sleep
import random


def scrapping(driver,label_cntry,label_tout,label_exc,label_scrp): 
    b_all_coun = driver.find_element_by_xpath(label_cntry).click()
    sleep(random.uniform(1.0,2.0))
    b_try_out = driver.find_element_by_xpath(label_tout).click()
    sleep(random.uniform(1.0,2.0))
    excute = driver.find_element_by_xpath(label_exc).click()
    sleep(random.uniform(4.0,5.0))
    scrapping = driver.find_elements_by_xpath(label_scrp)
    elements = scrapping[0].text
    return elements