from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

def stat(link):
    statist = []
    # initialize the Chrome driver
    driver = webdriver.Chrome("ChromeDriver/chromedriver")

    # перейти на страницу
    driver.get(link)

    elements = driver.find_elements(By.XPATH, '//*[@id="meta"]')

    for all_information in elements:
        statist.append(all_information.text)
        # print(i.text)
    try:
        nickname = statist[0].split('\n')[1]
        subscribers = statist[0].split('\n')[2]
    except IndexError:
        subscribers = 'закрыто'
    name_view_days_list = []
    # name_video = []
    # view_video = []
    # days_ago_video = []
    # print(nickname,subscribers)
    # print(statist[1:])
    for name_view_days in statist[1:-2]:  # с 1 элемента до последнего, не включая последний
        # name_video.append(name_view_days.split('\n')[0])
        # view_video.append(name_view_days.split('\n')[1])
        # days_ago_video.append(name_view_days.split('\n')[2])
        #name_view_days_list.append(name_view_days.replace('\n', ','))
        name_view_days_list.append(name_view_days)
    # print(name_video[-1],view_video[-1],days_ago_video[-1])
    name_view_days_list.insert(0,subscribers)
    name_view_days_list.insert(0, nickname)
    driver.quit()
    return name_view_days_list

def code_return(link):
    statist = []
    # initialize the Chrome driver
    driver = webdriver.Chrome("ChromeDriver/chromedriver")

    # перейти на страницу
    driver.get(link)

    page_source = driver.page_source
    print(page_source)
    continuee = driver.find_element_by_name('continue')



def statistics(values):
    list_stat = []
    url = 'https://www.youtube.com/@oblomoffood/videos'
    # for i in values:
    #     print(i[1]+"/videos")
    #     stat_video = stat(i[1]+"/videos")
    #     list_stat.append(stat_video)
    #     #print(stat(i[1]+"/videos"))
    stat_video = stat(url)
    list_stat.append(stat_video)
    return list_stat

#values = [['Имя блогера','Ссылка на канал']]
#print(statistics(values))

code_return('https://www.youtube.com/@oblomoffood/videos')