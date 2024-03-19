class FifoBuffer:
    def __init__(self, capacity):
        self.capacity = capacity        # вместимость буфера
        self.buffer = [None] * capacity # задаем фиксированное число элементов
        self.tail = 0                   # конец буфера
        self.length = 0                 # текущая длинна

    def _is_full(self):
        return self.length == self.capacity

    def append(self, element):
        # проверяем заполнен ли буфер
        if self._is_full():
            raise RuntimeError('The buffer is full. Use the function: pop()')
        
        self.buffer[self.tail] = element                 # заполняем буфер полученным значением
        self.tail = (self.tail + 1) % self.capacity      # увеличиваем значение tail
        self.length += 1                                 # увеличиваем значение length

        return element

    def pop(self):
        # проверяем есть ли что-то в буфере
        if self.length == 0:
            raise RuntimeError('The buffer is empty. Use the function: append()')

        returned_element = self.buffer.pop(0)            # возвращаем первый поступивший элемент
        self.buffer.append(None)                         # восполняем буфер до определенной длинны
        self.length -= 1                                 # уменьшаем значение length
        self.tail = self.length % self.capacity          # обновляем значение tail

        return returned_element


if __name__ == '__main__':
    fifo_buffer = FifoBuffer(5)     # задаем буфер вместимостью 5 элементов

    # если попробуем вернуть что-то из пустого массива:
    # fifo_buffer.pop()             # output: RuntimeError: The buffer is empty. Use the function: append()

    # добавляем 5 элементов:
    fifo_buffer.append(1)           # output: [1]
    fifo_buffer.append(2)           # output: [1, 2]
    fifo_buffer.append(3)           # output: [1, 2, 3]
    fifo_buffer.append(4)           # output: [1, 2, 3, 4]
    fifo_buffer.append(5)           # output: [1, 2, 3, 4, 5]


    # если попробуем добавить 6‑й элемент
    # fifo_buffer.append(6)         # output: RuntimeError: The buffer is full. Use the function: pop()

    # возвращаем два элемента, которые вошли в массив первыми:
    fifo_buffer.pop()               # output: [2, 3, 4, 5, None]
    fifo_buffer.pop()               # output: [3, 4, 5, None, None]
    #
    # добавляем новый элемент:
    fifo_buffer.append(6)           # output: [3, 4, 5, 6, None]
    #
    # возвращаем следующий по очереди:
    fifo_buffer.pop()               # output: [4, 5, 6, None, None]
    #
    # вывод текущего буфера:
    print(fifo_buffer.buffer)
