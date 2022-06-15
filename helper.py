# Представление всех ивентов передаваемых с интерфейса.
INPUT_SYMBOLS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
BINARY_OPERATIONS = ["/", "*", "-", "+", "ex", "%", "log_xy"]
UNARY_OPERATIONS = ["+/-", "sqrt", "1/x", "DMS", "Pi", "10^x", "tanh", "Ln"]
MEMORY_OPERATIONS = ["MS", "MC", "MR", "M+", "M-"]
RESULT_OPERATIONS = ["="]
EDIT_OPERATIONS = ["C", "CE", "backSpace"]

# является ли строка числом, в том числе отрицательным или с плавающей точкой
def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

# найти самый последний индекс вхождения
def list_rindex(li, x):
    for i in reversed(range(len(li))):
        if li[i] in x:
            return i
    return -1

# находит точку остановки, откуда начинается текущая операция
def find_start_index(li):
    digit = False
    for i in reversed(range(len(li))):
        if li[i] in RESULT_OPERATIONS or (is_digit(li[i]) and digit == True) or li[i] == 'Error':
            return i
        digit = is_digit(li[i])
    return -1

# сумма числа
def value_sum(value):
    result = 0
    while value > 0:
        digit = value % 10
        result = result + digit
        value  = value // 10
    if len(str(result)) > 1:
        return value_sum(result)
    return result
