from abc import ABC, abstractmethod

# абстрактный класс представляющий самый простой интерфейс для реализации вывода

class OutputHandler(ABC):
    def __init__(self, output_window, rows=1):
        self.output_window = output_window
        self.rows = rows

    @abstractmethod
    def print(self, data):
        pass

