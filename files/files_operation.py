import csv
from files.operation_Interface import FileOperationInterface


# создаем класс FileOperation унаследованный от интерфейся FileOperationInterface
class FileOperation(FileOperationInterface):
    # конструктор класса
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def read_lines(self):
        with open("notes.csv", encoding='utf-8') as r_file:
            # Создаем объект reader, указываем символ-разделитель ","
            notes = []
            file_reader = csv.reader(r_file, delimiter=";")
            # Счетчик для подсчета количества строк и вывода заголовков столбцов
            count = 0
            # Считывание данных из CSV файла
            for row in file_reader:
                if count > 0:
                    notes.append(row)
                count += 1
            return notes

    def save_lines(self, lines):
        new_id = 1
        with open("notes.csv", mode="w", encoding='utf-8') as w_file:
            # создаем объект writer с разделителем ";"
            file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
            # создаем первую строку с заголовками
            file_writer.writerow(['id', 'Header', 'Content', 'DateTime'])
            # заполняем файл построчно заменяя id файла от 1 и инкриментируем на 1
            for line in lines:
                line[0] = new_id
                file_writer.writerow(line)
                new_id += 1
