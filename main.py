from files.files_operation import FileOperation
from notes_controller import NoteController
from files.repository import Repository
from viewer.view import View


def start():
    # Инициализируем класс работы с файлами
    file_operation = FileOperation(file_path="notes.csv")
    # Инициализируем класс изменения файла
    repository = Repository(file_operation)
    # Инициализируем класс управления заметками
    notes_controller = NoteController(repository)
    # Инициализируем viewer и запускаем функцию run
    view = View(notes_controller)
    view.run()


# запускаем нашу программу по заметкам
if __name__ == '__main__':
    start()
