from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def pars():
    list_bloggers = []
    # initialize the Chrome driver
    driver = webdriver.Chrome("ChromeDriver/chromedriver1.exe")

    # перейти на страницу
    driver.get("https://centiman.avito.ru/service-dataset-collector-frontend/project/791")
    #driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(20)
    # for page in range(0, 1):
    #     driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    #     time.sleep(5)
    #elements = driver.find_elements(By.XPATH, '//*[@id="sections"]')

    #print(elements)


    # for i in elements:
    #     if (i.text + ',,' + i.get_attribute('href')) not in list_bloggers:
    #         list_bloggers.append(i.text + ',,' + i.get_attribute('href'))
    #     else:
    #         print(i.text + ' ' + i.get_attribute('href'))

    driver.quit()
    return list_bloggers

list_bloggers = pars()
print(list_bloggers)