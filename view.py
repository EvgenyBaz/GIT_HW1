def user_interface():
    print("\nтелефонный справочник \n  ")
    print("1 - ввести данные абонента")
    print("2 - найти абонента и вывести данные")
    print("3 - импортировать данные абонента")
    print("4 - экспортировать базу справочиника")
    print("5 - распечатать весь справочник")
    print("0 - окончание работы")

    position = int(input("выберите пункт меню: "))
    while position<0 or position>5:
        print("ошибка ввода")
        position = int(input("выберите пункт меню: "))
    else:
        return position




