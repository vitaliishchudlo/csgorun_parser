from selenium import webdriver
import sys
import time
import os
import plyer.platforms.win.notification
from plyer import notification

koef = float(input('ЯКИЙ КОФ МЕНШЕ? (X.X) '))  # ask what coefficient to check
driver = webdriver.Chrome(executable_path='chromedriver.exe')  # open browser Chrome
driver.get('https://csgorun.pro/')  # open site CS:GO RUN

list = [10 ** 10, 10 ** 10, 10 ** 10]  # history of crash

while True:
    get_number = driver.find_element_by_class_name('graph-label').text
    get_number = str(get_number).replace('x', '')

    if get_number == list[0]:
        print(f'Waiting... < {koef}')
        time.sleep(1)

    else:
        os.system('CLS')

        print('Added new number')
        list.insert(0, get_number)
        if float(list[0]) < float(koef) and float(list[1]) < float(koef) and \
                float(list[2]) < float(koef) and float(list[3]) < float(koef) and \
                float(list[4]) < float(koef):
            message = f'ВИПАЛО 5 РАЗА МЕНШЕ {koef}'
            notification.notify(title="CS GO RUN HACK", message=message, app_name='HACKER')

        elif float(list[0]) < float(koef) and float(list[1]) < float(koef) and \
                float(list[2]) < float(koef) and float(list[3]) < float(koef):
            message = f'ВИПАЛО 4 РАЗА МЕНШЕ {koef}'
            notification.notify(title="CS GO RUN HACK", message=message, app_name='HACKER')

        elif float(list[0]) < float(koef) and float(list[1]) < float(koef) and \
                float(list[2]) < float(koef):
            message = f'ВИПАЛО 3 РАЗА МЕНШЕ {koef}'
            notification.notify(title="CS GO RUN HACK", message=message, app_name='HACKER')

        elif float(list[0]) < float(koef) and float(list[1]) < float(koef):
            message = f'ВИПАЛО 2 РАЗА МЕНШЕ {koef}'
            notification.notify(title="CS GO RUN HACK", message=message, app_name='HACKER')

        else:
            print('More')
            os.system('CLS')

        if len(list) > 8:
            del list[-1]
        else:
            pass
        print(list)
