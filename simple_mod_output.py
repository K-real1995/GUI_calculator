from abc import ABC

import helper
from output_handler import OutputHandler

# класс обработчика вывода для обычного режима
class SimpleModOutput(OutputHandler, ABC):
    def getWindow(self):
        return self.output_window

    def print(self, data):
        if helper.is_digit(data[-1]) or data[-1] == 'Error':
            self.output_window.update(data[-1])
        else:
            self.output_window.update(data[-2])