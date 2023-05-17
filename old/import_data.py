# импортирует данные о пользователях из текстовых файлов
# запись должна содержать 4 атрибута , разделенных пробелом, точнок, запятой или точкой с запятой

from rewrite_database import rewrite_database

def import_data (data):
    path = input("введите имя файла для импорта данных: ")
    with open(path, "r", encoding='utf-8') as file:
        linelist = file.readlines()
        for line in linelist:
            # print(line)
            if line != "":
                # print(line)
                line1 = line.replace(" ",";")
                line2 = line1.replace(",",";")
                line3 = line2.replace(".", ";")
                # print(line3)
                data.append(line3.replace("\n","").split(";"))

    rewrite_database(data)