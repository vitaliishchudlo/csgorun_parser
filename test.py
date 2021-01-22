# # list = []
# #
# #
# # def run():
# #     #get_num = random.randint(1,10)
# #     try:
# #         get_num = int(input('Введите число: '))
# #         if get_num == list[0]:
# #             print('ПОВТОРЯЕТСЯ, ИГНОР')
# #             print(list)
# #         else:
# #             print('ДОБАВЛЕНО ЧИСЛО')
# #             list.insert(0, get_num)
# #             print(list)
# #     except ValueError:
# #         print('Введите число а не букву')
# #     run()
# #
# # def append_list():
# #     try:
# #         f_num = int(input('First number? '))
# #         list.append(f_num)
# #         run()
# #     except ValueError:
# #         print('Write correct number')
# #         append_list()
# #
# #
# #
# # if __name__ == '__main__':
# #     append_list()
# import decimal
#
# # list = ['1.32', 1.02]
# #
# # print(list[0])
# #
# # check = float(list[0])
# #
# # if check > list[1]:
# #     print('hey')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# from selenium import webdriver
# import sys
# import time
# import os
# import plyer.platforms.win.notification
# from plyer import notification
#
# koef = float(input('ЯКИЙ КОФ МЕНШЕ? (X.X) '))  # ask what coefficient to check
# driver = webdriver.Chrome(executable_path='chromedriver.exe')  # open browser Chrome
# driver.get('https://csgorun.pro/')  # open site CS:GO RUN
#
# list = [0, 0, 0]  # history of crash
#
#
#
# def main():
#     while True:
#         get_number = driver.find_element_by_class_name('graph-label')
#         result = get_number.text
#         result = str(result).replace('x', '')
#         if result == list[0]:
#             print(f'Waiting... < {koef}')
#             time.sleep(1.25)
#             main()
#         else:
#             print('Added new number')
#             list.insert(0, result)
#
#             if float(list[0]) < float(koef) and float(list[1]) < float(koef) and \
#                     float(list[2]) < float(koef):
#                 print('YOU CAN BET')
#                 message = f'ВИПАЛО 3 РАЗА МЕНШЕ {koef}'
#                 notification.notify("CS GO RUN HACK", message)
#             elif float(list[0]) < float(koef) and float(list[1]) < float(koef):
#                 print('YOU CAN BET')
#                 message = f'ВИПАЛО 2 РАЗА МЕНШЕ {koef}'
#                 notification.notify(title="CS GO RUN HACK", message=message, app_name='HACKER')
#
#             else:
#                 print('MORE')
#             os.system('CLS')
#             if len(list) > 8:
#                 del list[-1]
#             else:
#                 pass
#             print(list)
#
#         main()  # return to
#
#
# if __name__ == '__main__':
#     main()
# a = {'a': 1, 'b': 3, 'c': 5}
# b = {'a': 331, 'b': 2, 'c': 6}
# z = {k: a[k] + b[k] for k in b}
from ast import literal_eval

def writer_file():
    stat = {'2': 4, '3': 2, '4': 111, '5': 6, '6': 3, '7': 0, '8': 0}
    f = open('new.txt', 'r')
    history_stat = literal_eval(f.read())
    z = {k: stat[k] + history_stat[k] for k in stat}
    print(z)
    #last_stat = {k: stat[k] + history_stat[k] for k in stat}
    #print(last_stat)


writer_file()

