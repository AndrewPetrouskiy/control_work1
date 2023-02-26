from datetime import datetime


# Создаем класс Note который приниммает при инициализации id, header, content, time
# По дзен Python, советует открытость класса если его открытость ему не помешает в дальнейшей работе программы
# по этому я не делал не делал приватные методы тут и не создавал property and setter!

class Note:
    def __init__(self, num_id='', header='', content='', time=datetime.now()):
        self.id = num_id
        self.content = content
        self.header = header
        self.time = time

    def __str__(self):
        return f"Id: {self.id}, Header: {self.header}, Content: {self.content}, time: {self.time}"
