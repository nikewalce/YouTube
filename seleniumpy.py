from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

def stat(link):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    from selenium.webdriver.common.keys import Keys
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

def statistics(values):
    list_stat = []
    for i in values:
        print(i[1]+"/videos")
        stat_video = stat(i[1]+"/videos")
        list_stat.append(stat_video)
        #print(stat(i[1]+"/videos"))
    return list_stat


def pars():
    list_bloggers = []
    # initialize the Chrome driver
    driver = webdriver.Chrome("ChromeDriver/chromedriver")

    # перейти на страницу
    driver.get("https://www.youtube.com/hashtag/гараж")

    for page in range(0, 1):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(5)
    elements = driver.find_elements(By.XPATH, '//*[@id="text"]/a')
    # elements_view = driver.find_elements(By.XPATH, '//*[@id="meta"]/ytd-video-meta-block')
    # time.sleep(10)
    # count = 0
    # count_view = 0

    for i in elements:
        if (i.text + ',,' + i.get_attribute('href')) not in list_bloggers:
            list_bloggers.append(i.text + ',,' + i.get_attribute('href'))
        else:
            print(i.text + ' ' + i.get_attribute('href'))
    # for i in elements:
    #     print(i.text+f"{count}")
    #     count += 1
    # for i in elements_view:
    #     print(i.text+f"{count_view}")
    #     count_view += 1
    # print(count,count_view)
    driver.quit()
    return list_bloggers

values = []
list_bloggers = pars()
for element_list in list_bloggers:
    values.append(element_list.split(',,'))
print(values)

# print('statistics')
# print(statistics(values))


