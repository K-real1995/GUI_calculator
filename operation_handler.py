import math

from memory_list import MemoryList
import math
import helper

# класс реализующий логику операций, включая операции с памятью
class OperationHandler(object):
    def __init__(self, maxValueLen, memory_cells_count):
        self.CHARACTERS = maxValueLen
        self.memory_list = MemoryList(memory_cells_count)

    def prettifyNumber(self, value):
        result = value if value % 1 != 0 else int(value)
        if len(str(result)) > self.CHARACTERS:
            result = f'{result:.4e}'
            if len(str(result)) > self.CHARACTERS + 1:
                result = "Error"
        return str(result)

    def doUnaryOperation(self, string, val):
        try:
            if string not in helper.UNARY_OPERATIONS:
                print("Operation " + string + " is not in UNARY_OPERATIONS")
                return
            if string == '+/-':
                return self.prettifyNumber((float(val) * (-1)))
            elif string == 'sqrt':
                if float(val) < 0:
                    return "Error"
                else:
                    return self.prettifyNumber(math.sqrt(float(val)))
            elif string == '1/x':
                return self.prettifyNumber(1/float(val))
            elif string == "DMS":
                degrees = round(float(val))
                temp = 60 * (float(val) - degrees)
                minutes = int(temp)
                seconds = int(round(60 * (temp - minutes)))
                return f'''{abs(degrees)}° {abs(minutes)}' {abs(seconds)}" '''
            elif string == "Pi":
                return self.prettifyNumber(math.pi)
            elif string == "10^x":
                return self.prettifyNumber(10**float(val))
            elif string == "tanh":
                return str(math.tanh(float(val)))
            elif string == "Ln":
                return str(math.log(float(val)))
        except ValueError:
            return 'Error'

    def doBinaryOperation(self, val_1, operation, val_2):
        try:
            if operation not in helper.BINARY_OPERATIONS:
                print("Operation " + operation + "is not in BINARY_OPERATIONS")
                return
            val_1 = float(val_1)
            val_2 = float(val_2)
            if operation == "+":
                result = val_1 + val_2
            elif operation == "-":
                result = val_1 - val_2
            elif operation == "*":
                result = val_1 * val_2
            elif operation == "/":
                result = val_1 / val_2
            elif operation == "ex":
                result = val_1 ** val_2
            elif operation == "%":
                result = val_1 * (val_2 / 100)
            elif operation == "log_xy":
                if val_1 < 0 or val_2 < 0 or val_2 == 1:
                    return "Error"
                result = math.log(val_1, val_2)
        except ValueError:
            return "Error"
        return self.prettifyNumber(result)

    def doMemoryOperation(self, string, value=0):
        memCell = self.memory_list.getMemCell(string)
        event = string[:2]
        if event == 'MS':
            memCell.memSave(value)
        elif event == "MC":
            memCell.memClear()
        elif event == "M+":
            memCell.memPlus(value)
        elif event == "M-":
            memCell.memMinus(value)
        elif event == "MR":
            return self.prettifyNumber(memCell.memRead())
        return 'Memory operation complete'

    def doResultFromList(self, data):
        startIndex = helper.find_start_index(data)
        if startIndex >= 0:
            startIndex = startIndex + 1
        else:
            startIndex = 0
        if len(data[startIndex:]) < 3:
            return 'Error'
        result = float(data[startIndex])
        for i in range(startIndex, len(data)):
            if data[i] in helper.BINARY_OPERATIONS:
                try:
                    result = float(self.doBinaryOperation(result, *data[i:i+2]))
                except ValueError:
                    return 'Error'
        return self.prettifyNumber(result)

    def decdeg2dms(dd):
        mult = -1 if dd < 0 else 1
        mnt, sec = divmod(abs(dd) * 3600, 60)
        deg, mnt = divmod(mnt, 60)
        return mult * deg, mult * mnt, mult * sec

