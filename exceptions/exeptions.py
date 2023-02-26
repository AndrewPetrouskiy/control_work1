from files.files_operation import FileOperation


# функции которые проверяют валидность введенных значений.

def enter_first_menu() -> int:
    while True:
        try:
            answer = int(input("Please enter that do you want to do. \n" +
                               "enter 1: to add a new note,\nenter 2: to read one note,\n" +
                               "enter 3: to read all notes that you have,\nenter 4: to update an existing note,\n" +
                               "enter 5: to delete an existing note,\nenter 6: to exit the application\n"))
            if 0 <= answer <= 6:
                return answer
            else:
                print("You entered wrong number")
        except:
            print("You're wrong. Try again")


def enter_not_exist_file() -> int:
    while True:
        try:
            answer = int(input("Enter 1: to add a new note,\nenter 2: to exit the application\n"))
            if answer == 1 or answer == 2:
                return answer
            else:
                print("You entered wrong number")
        except:
            print("You're wrong. Try again")


def choose_how_to_sort() -> int:
    while True:
        try:
            answer = int(input("Enter 1: to sort by ID,\nenter 2: to sort by date and time\n"))
            if answer == 1 or answer == 2:
                return answer
            else:
                print("You entered wrong number")
        except:
            print("You're wrong. Try again")


def number_for_update() -> str:
    while True:
        try:
            answer = int(input("Which note do you want to update? Enter the ID" +
                               " of note which you want to update: "))
            len_all_notes = len(FileOperation('notes.csv').read_lines())
            if 1 <= answer <= len_all_notes:
                return str(answer)
            else:
                print("You entered wrong number")
        except:
            print("You're wrong. Try again")


def number_for_delete() -> str:
    while True:
        try:
            answer = int(input("Which note do you want to delete? Enter the ID" +
                               " of note which you want to delete: "))
            len_all_notes = len(FileOperation('notes.csv').read_lines())
            if 1 <= answer <= len_all_notes:
                return str(answer)
            else:
                print("You entered wrong number")
        except:
            print("You're wrong. Try again")
