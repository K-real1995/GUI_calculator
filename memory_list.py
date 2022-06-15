from memory_cell import MemoryCell

# класс-список для ячеек памяти способный находить нужную ячейку по ключу кнопки
class MemoryList(object):
    def __init__(self, memCount):
        self.mem_list = []
        for i in range(memCount):
            self.mem_list.append(MemoryCell())

    def getMemList(self):
        return self.mem_list

    def getMemCell(self, key):
        index = ""
        for char in key:
            if char.isnumeric():
                index += char
        return self.mem_list[int(index)]

