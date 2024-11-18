from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
statist = []
# initialize the Chrome driver
driver = webdriver.Chrome("ChromeDriver/chromedriver")

# перейти на страницу
driver.get('https://www.youtube.com/channel/UC9BGxwtlIgZBimMgvc7TlXA/videos')

elements = driver.find_elements(By.XPATH, '//*[@id="meta"]')

for all_information in elements:
    statist.append(all_information.text)
    #print(i.text)

nickname = statist[0].split('\n')[1]
subscribers = statist[0].split('\n')[2]
name_video = []
view_video = []
days_ago_video = []
#print(nickname,subscribers)
#print(statist[1:])
for name_view_days in statist[1:-2]:#с 1 элемента до последнего, не включая последний
    name_video.append(name_view_days.split('\n')[0])
    view_video.append(name_view_days.split('\n')[1])
    days_ago_video.append(name_view_days.split('\n')[2])

#print(name_video[-1],view_video[-1],days_ago_video[-1])


driver.quit()