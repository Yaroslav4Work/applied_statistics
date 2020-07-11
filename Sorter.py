# Создаем класс сортировщик
class Sorter:
    def __init__(self, array, sort_type='quick'):
        self.array = array
        self.sort_type = sort_type

    # Метод сортировки
    def sort(self):
        if self.sort_type == 'quick':  # Определяем тип сортировки, пока есть только 1 - быстрая
            i = 0  # Стартовый индекс сортируемого списка
            storage = self.array[i]  # Хранилище для замены элементов списка
            while i < len(self.array) - 1:  # Цикл для прохода по списку
                j = i + 1  # Индекс для дальнейшего прохода по списку
                while j < len(self.array): # Цикл для дальнейшего прохода по списку
                    # Сравниваем значение текущего элемента списка с последующими
                    if self.array[i] > self.array[j]:
                        # Если условие верно, то записываем в хранилище найденный меньший элемент
                        storage = self.array[j]
                        # Меняем найденный меньший элемент на текущий
                        self.array[j] = self.array[i]
                        # Заменяем текущий элемент, на найденный меньший элемент из хранилища
                        self.array[i] = storage
                    j += 1
                i += 1
            return self.array  # Возвращаем изменненый список


# Проверяем
if __name__ == '__main__':
    arr = [1, 5, 7, 9, 10, 11, 52, 4, 3]
    quick_sort = Sorter(arr)
    print(quick_sort.sort())
