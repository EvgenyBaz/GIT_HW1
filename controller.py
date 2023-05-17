# запускает графический интерфейс и отрабатывает тот или иной сценарий в зависимости от выбора пользователя

from view import user_interface as ui
from module import read_database as read_db
from module import input_data_local
from module import find_data_local
from module import export_data
from module import import_data
from module import print_data

def controller():


    position = -1

    while position != 0:
        position = ui()
        data = read_db()
        match position:
            case 1:
                input_data_local(data)
            case 2:
                find_data_local(data)
            case 3:
                import_data(data)
            case 4:
                export_data(data)
            case 5:
                print_data(data)
    else:
        print("конец работы")