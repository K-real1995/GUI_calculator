# функции для формирования графического интерфейса калькулятора

import PySimpleGUI as sg

# генерирует блок управления памятью, где cellsCount - количество ячеек памяти
def memoryWindowGenerator(cellsCount):
    memory_table = []
    if cellsCount > 1:
        memory_table.append([sg.Text("Блок управления памятью")])
    for i in range(cellsCount):
        memory_row = [
            sg.Button("MC", size=(6, 1), button_color=("white", "grey"), key="MC" + str(i)),
            sg.Button("MR", size=(6, 1), button_color=("white", "grey"), key="MR" + str(i)),
            sg.Button("MS", size=(6, 1), button_color=("white", "grey"), key="MS" + str(i)),
            sg.Button("M+", size=(6, 1), button_color=("white", "grey"), key="M+" + str(i)),
            sg.Button("M-", size=(6, 1), button_color=("white", "grey"), key="M-" + str(i)),
        ]
        if cellsCount > 1:
            memory_row.append(sg.Text(str(i + 1)))
        memory_table.append(memory_row)
    return memory_table

# генерирует цифровой экран вывода обычного режима
def generateSimpleModeOutput():
    return [[sg.Input('0', size=(10, 1), font=("Helvetica", 42), text_color="white", key='simpleInput', justification='r',
                readonly=True, disabled_readonly_background_color='grey')]]

# генерирует цифровой экран вывода расширенного режима с заданным количеством строк
def generateAdvancedModeOutput(rowCount):
    return [[sg.Multiline('\n' * (rowCount - 1) + '0', size=(19, rowCount), font=("Helvetica", 22), text_color="white",
                  no_scrollbar=True, justification='right', autoscroll=True)]]

# генерирует кнопки управления
def generateControlButtons():
    return [[sg.Button('≡', font=("Helvetica", 10), button_color=("white", "red"), size=(6, 1), key='mode'),
     sg.T(' ' * 45),
     sg.Button("C", size=(6, 1), button_color=("white", "red"))]]

# стандартные кнопки калькулятора
def generateCommonButtons():
    return  [
        [
            sg.Button("7", size=(6, 1), button_color=("blue", "white")),
            sg.Button("8", size=(6, 1), button_color=("blue", "white")),
            sg.Button("9", size=(6, 1), button_color=("blue", "white")),
            sg.Button("/", size=(6, 1), button_color=("white", "grey")),
            sg.Button("x^ⁿ", size=(6, 1), button_color=("white", "grey"), key="ex"),
        ],
        [
            sg.Button("4", size=(6, 1), button_color=("blue", "white")),
            sg.Button("5", size=(6, 1), button_color=("blue", "white")),
            sg.Button("6", size=(6, 1), button_color=("blue", "white")),
            sg.Button("*", size=(6, 1), button_color=("white", "grey")),
            sg.Button("√", size=(6, 1), button_color=("white", "grey"), key="sqrt"),
        ],
        [
            sg.Button("1", size=(6, 1), button_color=("blue", "white")),
            sg.Button("2", size=(6, 1), button_color=("blue", "white")),
            sg.Button("3", size=(6, 1), button_color=("blue", "white")),
            sg.Button("-", size=(6, 1), button_color=("white", "grey")),
            sg.Button("+/-", size=(6, 1), button_color=("white", "grey")),
        ],
        [
            sg.Button("0", size=(14, 1), button_color=("blue", "white")),
            sg.Button(".", size=(6, 1), button_color=("blue", "white")),
            sg.Button("+", size=(6, 1), button_color=("white", "grey")),
            sg.Button("=", size=(6, 1), button_color=("white", "blue")),
        ]
    ]

# расширенный функционал калькулятора
def generateAdvancedCommonButtons():
    return [
        [
            sg.Button("%", size=(6, 1), button_color=("white", "blue")),
            sg.Button("←", size=(6, 1), button_color=("white", "blue"), key="backSpace"),
            sg.Button("1/x", size=(6, 1), button_color=("white", "blue")),
            sg.Button("x²", size=(6, 1), button_color=("white", "blue"), key="square"),
            sg.Button("CE", size=(6, 1), button_color=("white", "red")),
        ],
        [
            sg.Button("DMS", size=(6, 1), button_color=("white", "blue")),
            sg.Button("10^x", size=(6, 1), button_color=("white", "blue")),
            sg.Button("Pi", size=(6, 1), button_color=("white", "blue")),
            sg.Button("tanh", size=(6, 1), button_color=("white", "blue")),
            sg.Button("Ln", size=(6, 1), button_color=("white", "blue")),
        ]
    ]

# окно с пользовательской информацией для расширенного режима
def generateAdvancedModeUserWindow(user_id):
    return [
        [sg.Text("Соклаков Кирилл Федорович", font=("Helvetica", 16))],
        [sg.Text("ID"), sg.Input(str(user_id), size=(31, 1), key='id'), sg.Button("<>", size=(6, 1), button_color=("white", "red"))],
        [sg.Text(" ", size=(35, 1), key="message", text_color="red")]
    ]