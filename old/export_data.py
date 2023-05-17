# экспортирует базу данных справочника в формате csv или xml  на выбор
def export_data(data):

    data_exp_type = -1
    while not (data_exp_type == 0 or data_exp_type == 1):
        print("выберите тип экспорта данных: 0 - XML, 1 - csv: ")
        data_exp_type = int(input())

    if data_exp_type == 1:
        with open("../exporter.csv", "w", encoding='utf-8') as file1:
            file1.write("Фамилия;Имя;Отчечтво;Номер телефона\n")
            for line in data:
                for atribute in range(len(line)-1):
                    # print(line[atribute])
                    file1.write(line[atribute] +";")
                file1.write(line[atribute+1] + "\n")
    else:
        with open("../exporter.xml", "w", encoding='utf-8') as file1:
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