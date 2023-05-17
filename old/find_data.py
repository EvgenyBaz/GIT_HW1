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