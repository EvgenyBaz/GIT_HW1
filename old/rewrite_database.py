# перезаписывает базу данных справочника после изменения данных в памяти

def rewrite_database(data):
    db_file =open("../database.txt", "w", encoding='utf-8')

    for line in data:
        db_file.write(" ".join(line)+"\n")

    db_file.close()