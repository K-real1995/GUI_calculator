from abc import ABC

from output_handler import OutputHandler
import helper

# класс обработчика вывода для расширенного режима
class AdvancedModOutput(OutputHandler, ABC):
    #конструктор принимающий окно вывода и количество строк
    def __init__(self, output_window, row_count=1):
        OutputHandler.__init__(self, output_window)
        self.row_count = row_count

    # вывод на цифровой дисплей
    def print(self, data):
        self.output_window.update(self.renderer(data))

    # исходя из количества строк преобразует массив с историей операций в строку для вывода
    def renderer(self, data):
        result_string = '\n'*self.row_count
        for i in range(len(data)):
            if data[i] in helper.RESULT_OPERATIONS:
                result_string = result_string + '\n'
                result_string = result_string + data[i]
                result_string = result_string + '\n'
            elif i > 0 and helper.is_digit(data[i-1]) and helper.is_digit(data[i]):
                result_string = result_string + '\n' + data[i]
            else:
                result_string = result_string + " " + data[i]
        return result_string
