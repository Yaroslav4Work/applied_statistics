# Создаем класс усреднитель
class Averager:
    def __init__(self, array, average_type='average'):
        self.array = array
        self.average_type = average_type

    def average(self):
        # Определяем тип усреднения, на данный момент присутствует несколько - среднее арифметическое и медиана
        if self.average_type == 'average':  # Если выбрали среднее арифметическое
            # Объяснять среднее арифметическое точно не стану...)
            items_summ = 0
            for i in self.array:
                items_summ += i
            return items_summ / len(self.array)
        elif self.average_type == 'mediana':  # Если выбрали медиану
            # Если по простому, то медиана - это центральная точка массива данных
            # Если кратно двум, то считаем среднее арифметическое между двумя центральными точками
            if len(self.array) % 2 == 0:  # Проверка с помощью деления по модулю
                middle = len(self.array) / 2
                return (self.array[middle] + self.array[middle + 1]) / 2
            # Иначе, берем центральное значение
            else:
                middle = len(self.array) // 2 + 1  # Целочисленное деление и сдвиг вправо
                return self.array[middle]


# Пробуем
if __name__ == '__main__':
    arr = [1, 5, 7, 9, 10, 11, 52, 4, 3]
    average_average = Averager(arr, 'average').average()
    mediana_average = Averager(arr, 'mediana').average()
    print(
        average_average,
        mediana_average
    )
