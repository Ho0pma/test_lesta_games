class FifoBuffer:
    def __init__(self, capacity):
        self.capacity = capacity        # вместимость буфера
        self.head = None                # ссылка на голову
        self.tail = None                # ссылка на конец массива
        self.length = 0                 # текущая длинна

    # Класс для создания узлов (нод)
    class Node:
        next_node = None    # ссылка на следующую ноду
        element = None      # ссылка на значение элемента

        def __init__(self, element, next_node=None):
            self.next_node = next_node
            self.element = element

    def _is_full(self):
        return self.length == self.capacity

    def append(self, element):
        # проверяем заполнен ли буфер
        if self._is_full():
            raise RuntimeError('The buffer is full. Use the function: pop()')

        self.length += 1

        # случай, если в массиве еще нет элементов:
        if not self.head:
            self.head = self.Node(element)

            return element

        #  случай, если в массиве есть один элемент (те только head):
        elif not self.tail:
            self.tail = self.Node(element, next_node=None)
            self.head.next_node = self.tail

            return element

        # случай, когда уже есть head и tail:
        else:
            node = self.Node(element, next_node=None)
            self.tail.next_node = node
            self.tail = node

            return element

    # функция для вывода нод:
    def __iter__(self):
        node = self.head

        while node:
            yield node.element
            node = node.next_node

    def pop(self):
        # проверяем есть ли что-то в буфере
        if self.length == 0:
            raise RuntimeError('The buffer is empty. Use the function: append()')

        # переопределяем голову, старые ссылки удаляются
        self.head = self.head.next_node
        self.length -= 1


if __name__ == '__main__':
    fifo_buffer = FifoBuffer(5)     # задаем буфер вместимостью 5 элементов

    # если попробуем удалить из пустого массива:
    # fifo_buffer.pop()             # output: RuntimeError: The buffer is empty. Use the function: append()

    # добавляем 5 элементов:
    fifo_buffer.append(1)           # output: [1]
    fifo_buffer.append(2)           # output: [1, 2]
    fifo_buffer.append(3)           # output: [1, 2, 3]
    fifo_buffer.append(4)           # output: [1, 2, 3, 4]
    fifo_buffer.append(5)           # output: [1, 2, 3, 4, 5]

    # если попробуем добавить 6‑й элемент
    # fifo_buffer.append(6)         # output: RuntimeError: The buffer is full. Use the function: pop()

    # удаляем два элемента, которые вошли в массив первыми:
    fifo_buffer.pop()               # output: [2, 3, 4, 5]
    fifo_buffer.pop()               # output: [3, 4, 5]

    # добавляем новый элемент:
    fifo_buffer.append(6)           # output: [3, 4, 5, 6]

    # удаляем следующий по очереди:
    fifo_buffer.pop()               # output: [4, 5, 6]

    # вывод текущего буфера:
    print([i for i in fifo_buffer])