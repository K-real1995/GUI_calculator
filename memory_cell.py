
# класс реализующий ячеку памяти и ее методы
class MemoryCell(object):
    def __init__(self, num=0):
        self.data = float(num)

    def memClear(self):
        self._memClear()

    def memRead(self):
        return self._memRead()

    def memSave(self, num):
        self._memSave(float(num))

    def memPlus(self, num):
        self._memPlus(float(num))

    def memMinus(self, num):
        self._memMinus(float(num))

    def _memClear(self):
        self.data = 0

    def _memRead(self):
        return self.data

    def _memSave(self, num):
        self.data = num

    def _memPlus(self, num):
        self.data += num

    def _memMinus(self, num):
        self.data -= num
