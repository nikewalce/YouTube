# Подключаем библиотеки
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
        print(Exception)

def add_to_spreadsheet_statistics(values, statistics_list,name_hashtag,spreadsheetId, service):

    # добавление данных
    body = {
        'valueInputOption': 'USER_ENTERED',
        'data': [{
            'range': 'Лист номер один!D1',
            "majorDimension": "ROWS",  # Сначала заполнять строки, затем столбцы
            'values': [[name_hashtag]]
        }, {
            'range': 'Лист номер один!2:2',
            "majorDimension": "ROWS",  # Сначала заполнять строки, затем столбцы
            'values': [['Название канала', 'Ссылка', 'Ник канала', 'Количество подписчиков', 'Видео']]
        }, {
            'range': 'Лист номер один!3:1100',
            "majorDimension": "ROWS",  # Сначала заполнять строки, затем столбцы
            'values': values
        }, {
            'range': 'Лист номер один!C3:1100',
            "majorDimension": "ROWS",  # Сначала заполнять строки, затем столбцы
            'values': statistics_list
        }]
    }

    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body=body).execute()


Spread_serv = autoriz()
spreadsheetId = Spread_serv[0]
service = Spread_serv[1]
name_hashtag = "сри"
values = [['fsd','adsd'],['fsfdsd','adasdsd'],['fdassd','adsfdsd']]
statistics_list = [['aafsd','fsd','dsf','dsf','dsf'],['aaafasd','fsd','dsf','dsf','dsf'],['aaafsd','fsd','dsf','dsf','dsf']]
add_to_spreadsheet_statistics(values, statistics_list, name_hashtag,spreadsheetId, service)
