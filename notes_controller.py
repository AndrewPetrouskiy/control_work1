from note import Note


class NoteController:
    # конструктор
    def __init__(self, repository):
        self.repository = repository

    # функция которая делает сохранения данных файлов, если csv файла не существует.
    def first_save(self, header, content):
        self.repository.first_create_note(header, content)

    # функция которая делает сохранения данных файлов, если csv файл существует.
    def save_note(self, header, content):
        self.repository.create_note(header, content)

    # функция которая читает нужную заметку
    def read_note(self, note_id):
        notes = self.repository.get_all_notes()
        for note in notes:
            if note[0] == note_id:
                n = Note(num_id=note[0], header=note[1], content=note[2], time=note[3])
                print(n)

    # функция которая показывает id and headers всех имеющихся заметок
    def show_header(self):
        notes = self.repository.get_all_notes()
        for note in notes:
            print(f"{note[0]} {note[1]}")

    # функция которая читает и выводит все имеющиеся заметки
    def read_all_notes(self):
        notes = self.repository.get_all_notes()
        for note in notes:
            n = Note(num_id=note[0], header=note[1], content=note[2], time=note[3])
            print(n)

    # функция которая выводит все отсортированные заметки по дате
    def time_sorted_all_notes(self):
        notes = self.repository.get_all_notes()
        notes = sorted(notes, key=lambda date: date[3])

        for note in notes:
            n = Note(num_id=note[0], header=note[1], content=note[2], time=note[3])
            print(n)

    # функция которая изменяет выбранную заметку
    def update_note(self, note_id):
        self.repository.update_note(note_id)

    # функция которая удаляет выбранную заметку
    def delete_note(self, note_id):
        self.repository.delete_note(note_id)
