from operation_handler import OperationHandler
import helper


# главный обработчик распределяет ивенты приходящие с интерфейса в работу
class MainHandler:
    def __init__(self, output_handler, max_row_size, memory_cells_count):
        self.data = ['0']
        self.output_handler = output_handler
        self.operation_handler = OperationHandler(max_row_size, memory_cells_count)

    # принимает ключ кнопки и выполняет команду
    def input(self, string):
        if string == 'Error':
            return
        # обработка результата
        if string in helper.RESULT_OPERATIONS and len(self.data) > 2:
            if self.data[-1] != 'Error':
                if len(self.data[helper.find_start_index(self.data) + 1:]) > 2:
                    if helper.is_digit(self.data[-1]):
                        result = self.operation_handler.doResultFromList(self.data)
                        self.data.append(string)
                        self.data.append(str(result))

        # обработка символов ввода 0-9 и .
        elif string in helper.INPUT_SYMBOLS:
            if helper.is_digit(self.data[-1]):
                if len(self.data) > 2 and self.data[-2] in helper.RESULT_OPERATIONS:
                    self.data.append(string)
                else:
                    if self.data[-1] == '0' and string != '.':
                        self.data[-1] = string
                    else:
                        self.data[-1] = self.data[-1] + string
            else:
                self.data.append(string)

        # обработка унарных операций
        elif string in helper.UNARY_OPERATIONS:
            if self.data[-1] != 'Error':
                if helper.is_digit(self.data[-1]):
                    self.data[-1] = self.operation_handler.doUnaryOperation(string, self.data[-1])

        # обработка операций с памятью
        elif string[:2] in helper.MEMORY_OPERATIONS:
            index = (-1) if helper.is_digit(self.data[-1]) else (-2)
            memoryOpResult = str(self.operation_handler.doMemoryOperation(string, self.data[index]))
            if helper.is_digit(memoryOpResult):
                self.data[index] = memoryOpResult

        # обработка бинарных операций
        elif string in helper.BINARY_OPERATIONS:
            if self.data[-1] != 'Error':
                if self.data[-1] in helper.BINARY_OPERATIONS:
                    self.data[-1] = string
                elif helper.is_digit(self.data[-1]):
                    self.data.append(string)

        # кнопки редактирования ввода
        elif string in helper.EDIT_OPERATIONS:
            if string == 'C':
                self.data = ['0']
            elif string == 'backSpace':
                if helper.is_digit(self.data[-1]):
                    if len(self.data[-1]) > 1:
                        self.data[-1] = self.data[-1][:-1]
                    else:
                        self.data[-1] = '0'
            elif string == 'CE':
                index = helper.find_start_index(self.data)
                if index >= 0:
                    self.data = self.data[:helper.find_start_index(self.data) + 2]
                else:
                    self.data = ['0']

        # передача массива с историей операций объекту вывода
        self.output_handler.print(self.data)
