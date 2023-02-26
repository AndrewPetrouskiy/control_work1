import time
from exceptions.exeptions import *
from os import path


# создаем класс View для работы с клиентом
class View:
    # инициализируем конструктор
    def __init__(self, notes_controller):
        self.notes_controller = notes_controller

    # создаем метод run для работы с клиентом
    def run(self):
        # приветственное окно
        print("Hello. I welcome you to my notes application")
        time.sleep(1)
        # используем цикл while для непревной работы в меню, пока клиент не захочет выйти
        while True:
            # сперва нужно проверить существует ли файл, если его нет,
            # то предлажить пользователю заполнить певую заметку или выйти из программы
            if not path.exists('notes.csv'):
                print("You don't have any notes. Please fill in first note!")
                number = enter_not_exist_file()
                if number == 1:
                    header = input("Header: ")
                    content = input("Content: ")
                    self.notes_controller.first_save(header, content)
                if number == 2:
                    print("Thank you that you use my little application. Bye - Bye")
                    break
            # если заметка уже есть, то предлажить выбрать один из вариантом работы с файлом
            else:
                print()
                num = enter_first_menu()
                if num == 6:
                    # если пользователь выбирет 6, то попращаться с ним и завершить программу
                    print("Thank you that you used my little application. Bye - Bye")
                    break
                if num == 1:
                    # если пользователь выбирет 1, то заполнить новую заметку
                    header = input("Header: ")
                    content = input("Content: ")
                    self.notes_controller.save_note(header, content)
                if num == 2:
                    # если пользователь выбирет 2, то вывести на экран одну заметку которую он выбирет по заголовкам
                    self.notes_controller.show_header()
                    note_id = input("Enter the ID: ")
                    self.notes_controller.read_note(note_id)
                if num == 3:
                    # если пользователь выбирет 3, то вывести на экран отсортиранные заметки или по id или по time
                    print("How do you want to sort")
                    sort_number = choose_how_to_sort()
                    if sort_number == 1:
                        self.notes_controller.read_all_notes()
                    if sort_number == 2:
                        self.notes_controller.time_sorted_all_notes()
                if num == 4:
                    # если пользователь выбирет 4, то выбрать по заголовкам заметку и изменить ее
                    self.notes_controller.show_header()
                    num_id = number_for_update()
                    self.notes_controller.update_note(num_id)
                if num == 5:
                    # если пользователь выбирет 5, то выбрать по загаловкам заметку и удалить ее
                    self.notes_controller.show_header()
                    num_id = number_for_delete()
                    self.notes_controller.delete_note(num_id)
                    print(f"File deleted")
