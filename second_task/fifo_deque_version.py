from collections import deque

class FifoBuffer:
    def __init__(self, capacity):
        self.capacity = capacity        # вместимость буфера
        self.buffer = deque()           # создаем очередь
        self.length = 0                 # текущая длинна

    def _is_full(self):
        return self.length == self.capacity

    def append(self, element):
        # проверяем заполнен ли буфер
        if self._is_full():
            raise RuntimeError('The buffer is full. Use the function: pop()')

        self.buffer.appendleft(element)         # добавляем элемент в массив слева
        self.length += 1                        # увеличиваем значение length

        return element

    def pop(self):
        # проверяем есть ли что-то в буфере
        if self.length == 0:
            raise RuntimeError('The buffer is empty. Use the function: append()')

        returned_element = self.buffer.pop()    # возвращаем элемент из массива справа
        self.length -= 1                        # уменьшаем значение length

        return returned_element


if __name__ == '__main__':
    fifo_buffer = FifoBuffer(5)     # задаем буфер вместимостью 5 элементов

    # если попробуем удалить из пустого массива:
    # fifo_buffer.pop()             # output: RuntimeError: The buffer is empty. Use the function: append()

    # добавляем 5 элементов:
    fifo_buffer.append(1)           # output: deque([1])
    fifo_buffer.append(2)           # output: deque([2, 1])
    fifo_buffer.append(3)           # output: deque([3, 2, 1])
    fifo_buffer.append(4)           # output: deque([4, 3, 2, 1])
    fifo_buffer.append(5)           # output: deque([5, 4, 3, 2, 1])

    # если попробуем добавить 6‑й элемент
    # fifo_buffer.append(6)         # output: RuntimeError: The buffer is full. Use the function: pop()

    # возвращаем два элемента, которые вошли в массив первыми:
    fifo_buffer.pop()               # output: deque([5, 4, 3, 2])
    fifo_buffer.pop()               # output: deque([5, 4, 3])

    # добавляем новый элемент:
    fifo_buffer.append(6)           # output: deque([6, 5, 4, 3])

    # возвращаем следующий по очереди:
    fifo_buffer.pop()               # output: deque([6, 5, 4])

    # вывод текущего буфера:
    print(fifo_buffer.buffer)
