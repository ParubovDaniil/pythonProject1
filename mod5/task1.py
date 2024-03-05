class Node:
    # Вспомогательный класс для узлов списка
    def init(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:
    # Основной класс для стека
    def init(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        # возвращение последнего элемента из списка с удалением его из списка
        if self.end is None:
            return None
        else:
            val = self.end.data
            self.end = self.end.pref
            return val

    def push(self, val):
        # добавление элемента val в конец списка
        new_node = Node(val)
        if self.end is None:
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end = new_node

    def print(self):
        # вывод на печать содержимого стека
        current = self.end
        while current:
            print(current.data)
            current = current.pref