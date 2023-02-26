from abc import ABC, abstractmethod

# создаем интерфейc по работе с изменениями файлов
class RepositoryInterface(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_all_notes(self) -> list:
        pass

    @abstractmethod
    def create_note(self, header, content) -> list:
        ...

    @abstractmethod
    def update_note(self, id_notes) -> list:
        ...

    @abstractmethod
    def delete_note(self, id_note):
        pass
