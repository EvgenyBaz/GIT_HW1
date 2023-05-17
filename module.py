
# читает базу данных из файла при отработке интерфейса

def read_database():

    db_list = []
    db_file =open("database.txt", "r", encoding='utf-8')
    linelist = db_file.readlines()

    for line in linelist:
        if line != "":
            db_list.append(line.replace("\n","").split(" "))

    db_file.close()

    return db_list

# перезаписывает базу данных справочника после изменения данных в памяти

def rewrite_database(data):
    db_file =open("database.txt", "w", encoding='utf-8')

    for line in data:
        db_file.write(" ".join(line)+"\n")

    db_file.close()

# внесение данных о новом пользователе из консоли

def input_data_local(data):
    data_second_name = input("Введите фамилию пользователя: ").strip()
    if data_second_name == "":
        data_second_name = "_"
    data_first_name = input("Введите имя пользователя: ").strip()
    if data_second_name == "":
        data_first_name = "_"
    data_father_name = input("Введите отчество пользователя: ").strip()
    if data_father_name == "":
        data_father_name = "_"
    phone_number = input("Введите телефон пользователя: ").strip()
    if phone_number == "":
        phone_number = "_"

    line = (data_second_name, data_first_name, data_father_name, phone_number)
    data.append(line)

    rewrite_database(data)


# осуществояет поиск по фамилии или имени и показывает данные найденогй записи

def find_data_local(data):
    flag = 0
    search_atribut = input("введите фамилию или имя пользователя: ")
    for line in data:
        for user_atribut in line:
            if user_atribut == search_atribut:
                print("\nФамилия: ", line[0], "\nИмя: ", line[1], "\nОтчество: ", line[2], "\nНомер телефона :", line[3])
                flag = 1
    if flag == 0:
        print("\nтакой записи нет")

# экспортирует базу данных справочника в формате csv или xml  на выбор

def export_data(data):

    data_exp_type = -1
    while not (data_exp_type == 0 or data_exp_type == 1):
        print("выберите тип экспорта данных: 0 - XML, 1 - csv: ")
        data_exp_type = int(input())

    if data_exp_type == 1:
        with open("exporter.csv", "w", encoding='utf-8') as file1:
            file1.write("Фамилия;Имя;Отчечтво;Номер телефона\n")
            for line in data:
                for atribute in range(len(line)-1):
                    # print(line[atribute])
                    file1.write(line[atribute] +";")
                file1.write(line[atribute+1] + "\n")
    else:
        with open("exporter.xml", "w", encoding='utf-8') as file1:
            file1.write('<?xml version="1.0" encoding="utf-8"?>\n')
            file1.write("<phonebook>\n")
            for i in range (len(data)):
                file1.write(f"    <user> {i+1}\n")
                file1.write(f"        <Фамилия>{data[i][0]}</Фамилия>\n")
                file1.write(f"        <Имя>{data[i][1]}</Имя>\n")
                file1.write(f"        <Отчество>{data[i][2]}</Отчество>\n")
                file1.write(f"        <Т_номер>{data[i][3]}</Т_номер>\n")
                file1.write(f"    </user>\n")

            file1.write("</phonebook>")

# импортирует данные о пользователях из текстовых файлов
# запись должна содержать 4 атрибута , разделенных пробелом, точнок, запятой или точкой с запятой

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

# распетатывает базу данных в консоли

def print_data(data):
     print("Фамилия;Имя;Отчечтво;Номер телефона\n")
     print(*data, sep="\n")