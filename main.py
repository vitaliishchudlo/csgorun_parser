# {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}

from selenium import webdriver
import sys
import time
import os
import plyer.platforms.win.notification
from plyer import notification
from ast import literal_eval
from pathlib import Path



koef = float(input('ЯКИЙ КОФ МЕНШЕ? (X.X) '))  # ask what coefficient to check
driver = webdriver.Chrome(executable_path='chromedriver.exe')  # open browser Chrome
# driver.minimize_window() # Скрити вікно
driver.get('https://csgorun.pro/')  # open site CS:GO RUN

list = [10 ** 10, 10 ** 10, 10 ** 10]  # history of crash


def writer_file(num):
    stat = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}
    stat[str(num)] = 1
    f = open('statistic.txt', 'r')
    file_stat = literal_eval(f.read())
    z = {k: stat[k] + file_stat[k] for k in stat}
    f.close()
    w = open('statistic.txt', 'w')
    print(z)
    w.write(str(z))
    w.close()



def check_file_statistic(num):
    my_file = Path("statistic.txt")
    if my_file.is_file() == True:
        print(my_file.is_file())
        writer_file(num)
    else:
        print('FALSE')
        file = open("statistic.txt", "w")
        file.write(str("{'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}"))
        file.close()
        check_file_statistic(num)


while True:
    driver.minimize_window()
    get_number = driver.find_element_by_class_name('graph-label').text
    get_number = str(get_number).replace('x', '')

    if get_number == list[0]:
        print(f'Waiting... < {koef}')
        time.sleep(0.9)

    else:
        os.system('CLS')

        print('Added new number')
        list.insert(0, get_number)
        if float(list[0]) < float(koef) and float(list[1]) < float(koef) and \
                float(list[2]) < float(koef) and float(list[3]) < float(koef) and \
                float(list[4]) < float(koef) and float(list[5]) < float(koef) and \
                float(list[6]) < float(koef) and float(list[7]) < float(koef):
            message = f'ВИПАЛО 8 РАЗ МЕНШЕ {koef}'
            notification.notify(title="CS GO RUN HACK", message=message, app_name='HACKER')
            check_file_statistic(8)

        elif float(list[0]) < float(koef) and float(list[1]) < float(koef) and \
                float(list[2]) < float(koef) and float(list[3]) < float(koef) and \
                float(list[4]) < float(koef) and float(list[5]) < float(koef) and \
                float(list[6]) < float(koef):
            message = f'ВИПАЛО 7 РАЗ МЕНШЕ {koef}'
            notification.notify(title="CS GO RUN HACK", message=message, app_name='HACKER')
            check_file_statistic(7)

        elif float(list[0]) < float(koef) and float(list[1]) < float(koef) and \
                float(list[2]) < float(koef) and float(list[3]) < float(koef) and \
                float(list[4]) < float(koef) and float(list[5]) < float(koef):
            message = f'ВИПАЛО 6 РАЗ МЕНШЕ {koef}'
            notification.notify(title="CS GO RUN HACK", message=message, app_name='HACKER')
            check_file_statistic(6)

        elif float(list[0]) < float(koef) and float(list[1]) < float(koef) and \
                float(list[2]) < float(koef) and float(list[3]) < float(koef) and \
                float(list[4]) < float(koef):
            message = f'ВИПАЛО 5 РАЗ МЕНШЕ {koef}'
            notification.notify(title="CS GO RUN HACK", message=message, app_name='HACKER')
            check_file_statistic(5)

        elif float(list[0]) < float(koef) and float(list[1]) < float(koef) and \
                float(list[2]) < float(koef) and float(list[3]) < float(koef):
            message = f'ВИПАЛО 4 РАЗИ МЕНШЕ {koef}'
            notification.notify(title="CS GO RUN HACK", message=message, app_name='HACKER')
            check_file_statistic(4)

        elif float(list[0]) < float(koef) and float(list[1]) < float(koef) and \
                float(list[2]) < float(koef):
            message = f'ВИПАЛО 3 РАЗИ МЕНШЕ {koef}'
            notification.notify(title="CS GO RUN HACK", message=message, app_name='HACKER')
            check_file_statistic(3)

        elif float(list[0]) < float(koef) and float(list[1]) < float(koef):
            message = f'ВИПАЛО 2 РАЗИ МЕНШЕ {koef}'
            notification.notify(title="CS GO RUN HACK", message=message, app_name='HACKER')
            check_file_statistic(2)

        else:
            print('More')
            os.system('CLS')

        if len(list) > 8:
            del list[-1]
        else:
            pass
        print(list)
