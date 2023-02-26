from abc import ABC, abstractmethod


# создаем интерфейc по работе с файлами

class FileOperationInterface(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def read_lines(self):
        pass

    @abstractmethod
    def save_lines(self, lines):
        pass
