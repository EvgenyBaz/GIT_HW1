# читает базу данных из файла при отработке интерфейса
def read_database():

    db_list = []
    db_file =open("../database.txt", "r", encoding='utf-8')
    linelist = db_file.readlines()

    for line in linelist:
        if line != "":
            db_list.append(line.replace("\n","").split(" "))

    # print(db_list)

    db_file.close()

    return db_list