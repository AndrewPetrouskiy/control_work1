from note import Note
from files.repository_interface import RepositoryInterface
from files.files_operation import *

# создаем класс Repository унаследованный от интерфейся RepositoryInterface
class Repository(RepositoryInterface):
    # инициализируем конструктор
    def __init__(self, file_operation):
        super().__init__()
        self.fileOperation = file_operation
    # функция котрая читает с файла
    def get_all_notes(self):
        read_notes = self.fileOperation.read_lines()
        return read_notes

    # функция котрая записывает в файл нового пользователя если csv файла не существует
    def first_create_note(self, header, content):
        notes = []
        new_note = Note(header=header, content=content)
        update_note = [new_note.id, new_note.header, new_note.content, new_note.time]
        notes.append(update_note)
        FileOperation.save_lines(self, notes)

    # функция котрая записывает в файл нового пользователя если csv файл существует
    def create_note(self, header, content):
        notes = self.get_all_notes()
        new_note = Note(header=header, content=content)
        update_note = [new_note.id, new_note.header, new_note.content, new_note.time]
        notes.append(update_note)
        FileOperation.save_lines(self, notes)

    # функция котрая записывает файл с измененной заметкой
    def update_note(self, id_notes):
        notes = self.get_all_notes()
        for i, note in enumerate(notes):
            if note[0] == id_notes:
                id = len(notes) + 1
                header = input("Header: ")
                content = input("Content: ")
                new_note = Note(id, header=header, content=content)
                update_note = [new_note.id, new_note.header, new_note.content, new_note.time]
                notes[i] = update_note
        FileOperation.save_lines(self, notes)

    # функция котрая записывает файл с удаленной заметкой
    def delete_note(self, id_note):
        notes = self.get_all_notes()
        for i, note in enumerate(notes):
            if note[0] == id_note:
                notes.pop(i)
        FileOperation.save_lines(self, notes)
