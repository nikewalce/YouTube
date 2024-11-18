# Подключаем библиотеки
import sys

import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

def autoriz():
    try:
        CREDENTIALS_FILE = 'credentials.json'  # Имя файла с закрытым ключом, вы должны подставить свое

        # Читаем ключи из файла
        credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                                       ['https://www.googleapis.com/auth/spreadsheets',
                                                                        'https://www.googleapis.com/auth/drive'])

        httpAuth = credentials.authorize(httplib2.Http())  # Авторизуемся в системе
        service = googleapiclient.discovery.build('sheets', 'v4',
                                                  http=httpAuth)  # Выбираем работу с таблицами и 4 версию API
        spreadsheetId = '1QlvHirUEoi-MT7nZrMAB4-kvFeqZdfBvWS0ExHbuPJs'  # сохраняем идентификатор файла
        driveService = googleapiclient.discovery.build('drive', 'v3',
                                                       http=httpAuth)  # Выбираем работу с Google Drive и 3 версию API
        # Доступ к редактированию
        # access = driveService.permissions().create(
        #     fileId=spreadsheetId,
        #     body={'type': 'user', 'role': 'writer', 'emailAddress': 'nikewalce1@gmail.com'},
        #     # Открываем доступ на редактирование
        #     fields='id'
        # ).execute()
        print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)
        return spreadsheetId, service
    except Exception:
        print("Autorize exception")
        e = sys.exc_info()[1]
        print(e.args[0])

def read_sheet(service, spreadsheetId):
    # чтение данных ROWS/COLUMNS
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId,
        range='A1:A5',
        majorDimension='ROWS'
    ).execute()
    return values



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

def pars(hashtag, range_count):
    list_bloggers = []
    try:
        # initialize the Chrome driver
        driver = webdriver.Chrome("ChromeDriver/chromedriver")

        # перейти на страницу
        driver.get("https://www.youtube.com/hashtag/"+hashtag)
        #driver.get("https://www.youtube.com/results?search_query=+%23%D0%B5%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3+%23%D0%BE%D1%87%D0%BA%D0%B8")

        for page in range(0, range_count):
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(5)
        elements = driver.find_elements(By.XPATH, '//*[@id="text"]/a')
        #time.sleep(10)
        number_of_repetitions = 0
        for i in elements:
            if (i.text + ',,' + i.get_attribute('href')) not in list_bloggers:
                list_bloggers.append(i.text + ',,' + i.get_attribute('href'))
            else:
                number_of_repetitions += 1
                #print(i.text + ' ' + i.get_attribute('href'))
        print(number_of_repetitions)
        driver.quit()
        return list_bloggers
    except Exception:
        print('Parse exception')
        e = sys.exc_info()[1]
        print(e.args[0])
        return list_bloggers

def add_to_spreadsheet_statistics(values, name_hashtag, statistics_list,spreadsheetId, service):
    try:
        # добавление данных
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': [{
                'range': 'Лист номер один!D1',
                "majorDimension": "ROWS",  # Сначала заполнять строки, затем столбцы
                'values': [[name_hashtag]]
            },{
                'range': 'Лист номер один!2:2',
                "majorDimension": "ROWS",  # Сначала заполнять строки, затем столбцы
                'values': [['Название канала','Ссылка','Ник канала','Количество подписчиков','Видео']]
            },{
                'range': 'Лист номер один!A3:B1100',
                "majorDimension": "ROWS",  # Сначала заполнять строки, затем столбцы
                'values': values
            },{
                'range': 'Лист номер один!C3:1100',
                "majorDimension": "ROWS",  # Сначала заполнять строки, затем столбцы
                'values': statistics_list
            }]
        }

        results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body=body).execute()
    except Exception:
        print('add_to_spreadsheet_statistics exception')
        e = sys.exc_info()[1]
        print(e.args[0])


def add_to_spreadsheet(values, spreadsheetId, name_hashtag, service):
    try:
        # добавление данных
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': [{
                'range': 'Лист номер один!D1',
                "majorDimension": "ROWS",  # Сначала заполнять строки, затем столбцы
                'values': [[name_hashtag]]
            },{
                'range': 'Лист номер один!2:2',
                "majorDimension": "ROWS",  # Сначала заполнять строки, затем столбцы
                'values': [['Название канала','Ссылка','Ник канала','Количество подписчиков','Видео']]
            },{
                'range': 'Лист номер один!3:1100',
                "majorDimension": "ROWS",  # Сначала заполнять строки, затем столбцы
                'values': values
            }]
        }

        results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body=body).execute()
    except Exception:
        print('add_to_spreadsheet Exception')
        e = sys.exc_info()[1]
        print(e.args[0])



Spread_serv = autoriz()
spreadsheetId = Spread_serv[0]
service = Spread_serv[1]

values = []
name_hashtag = "книги"
range_count = 1
list_bloggers = pars(name_hashtag,range_count)
for element_list in list_bloggers:
    values.append(element_list.split(',,'))

print(values)
#add_to_spreadsheet(values, spreadsheetId, name_hashtag, service)

#statistics_list = statistics(values)
#print(statistics_list)
#print('list_blog')
#print(values)
#add_to_spreadsheet_statistics(values, name_hashtag, statistics_list, spreadsheetId, service)
