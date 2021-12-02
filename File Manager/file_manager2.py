import os
import shutil
import sys

import settings as sett

sett.start_place()


OS = sys.platform
if OS == 'darwin':
    symbol_l = '/'

elif OS == 'cygwin' or OS == 'win32' :
    symbol_l = "\\"

else:
    symbol_l = "/"


tr = os.getcwd()
tr = tr.split(symbol_l)
tr = tr[:-1:]
tr_len = len(tr)





def mkfold(folder_name):
    os.mkdir(folder_name)

def rmfold(folder_name):
    shutil.rmtree(folder_name)

def cf(path):

    OS = sys.platform
    if OS == 'darwin':
        symbol = '/'

    elif OS == 'cygwin' or OS == 'win32' :
        symbol = "\\"

    else:
        symbol = "/"

    if path == "-":

        p = str(os.getcwd())
        p = p.split(symbol)
        p[0] = ""
        p[-1] = ""

        if len(p)-1 > tr_len:

            sum = ""
            for i in range(len(p)):
                sum = sum + symbol + p[i]
            sum = sum[1::]

            os.chdir(sum)
        else:
            print('Дальше нельзя')

    elif  "."+symbol in path:
        p = str(os.getcwd())+symbol+path[2::]
        os.chdir(p)


    else:
        os.chdir(path)

def list():
    print(os.listdir())

def pwd():
    print(os.getcwd())

def create(file_name):
    file = open(file_name, "w+")
    file.close()

def rmv(file_name):
    try:
        os.remove(file_name)
    except:
        print('Что-то пошло не так')

def cet(file_name):
    try:
        file = open(file_name, "r")
        print(file.read())
        file.close()
    except:
        print('Что-то пошло не так')

def rewrite(file_name, content):
    try:
        file = open(file_name, "w")
        file.write(content)
    except:
        print('Что-то пошло не так')
def add(file_name, content):
    file = open(file_name, "a")
    file.write(content)
    file.close()

def rename(first_name, second_name):
    try:
        os.rename(first_name,second_name)
    except:
        print('Что-то пошло не так')

def copy(first_name, second_name):
    try:
        shutil.copy(first_name,second_name)
    except:
        print('Что-то пошло не так')

def move(first_name, second_name):
    try:
        shutil.move(first_name,second_name)
    except:
        print('Что-то пошло не так')

def help():
    print("""    Создание папки [команда имя] - mkfold
    Удаление папки по имени [команда имя] - rmfold
    
    Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх [команда путь]- cf
    Переход на 1 папку вверх - "cf -"
    Относительный переход к папке от текущей - "./[путь] или .\\[путь]"
    
    Создание пустых файлов с указанием имени [команда имя] - create
    Запись текста в файл с заменой текста [команда имя текст] - rewrite
    Дозапись текста в файл [команда имя текст] - add
    Просмотр содержимого текстового файла [команда имя] - cet
    Удаление файлов по имени [команда имя] - rmv
    Копирование файлов из одной папки в другую [команда путь1 путь2] - copy
    Перемещение файлов [команда путь1 путь2] - move
    Переименование файлов [команда СтароеИмя НовоеИмя] - rename
    Показать все файлы директории [команда] - list
    Просмотреть текущий путь [команда]- pwd
    Помощь [команда] - help
    Выход [команда] - exit """)




help()
while True:
    vvod = input('Введите команду и параметры: ')
    vvod = vvod.split()
    command = vvod[0]

    if command == "mkfold":
        try:
            mkfold(vvod[-1])
        except:
            print('что-то пошло не так')

    if command == "rmfold":
        try:
            rmfold(vvod[-1])
        except:
            print('что-то пошло не так')

    if command == "pwd":
        pwd()

    if command == "cf":
        try:
            cf(vvod[-1])
        except:
            print('что-то пошло не так')

    if command == "list":
        list()

    if command == "create":
        create(vvod[-1])

    if command == "rmv":
        try:
            rmv(vvod[-1])
        except:
            print('что-то пошло не так')

    if command == "cet":
        try:
            cet(vvod[-1])
        except:
            print('что-то пошло не так')
    if command == "rewrite":
        try:
            sum = ""
            for i in range(len(vvod)):
                if i > 1:
                    sum = sum +" "+ vvod[i]
            rewrite(vvod[1], sum)
        except:
            print('Что-то пошло не так')
    if command == "add":
        try:
            sum = ""
            for i in range(len(vvod)):
                if i > 1:
                    sum = sum +" "+ vvod[i]
            add(vvod[1], sum)
        except:
            print('Что-то пошло не так')
    if command == "exit":
       sys.exit()

    if command == 'rename':
        try:
            if len(vvod) < 4:
                rename(vvod[1],vvod[-1])
            else:
                print("Слишком много аргументов")
        except:
            print('Что-то пошло не так')
    if command == 'copy':
        try:
            copy(vvod[1], vvod[-1])
        except:
            print('Что-то пошло не так')
    if command == 'move':
        try:
            move(vvod[1], vvod[-1])
        except:
            print("Что-то пошло не так")

    if command == 'help':
        help()





