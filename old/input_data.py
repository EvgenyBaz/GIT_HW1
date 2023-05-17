# внесение данных о новом пользователе из консоли

from rewrite_database import rewrite_database

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

    # print(*data, sep="\n")

    return data