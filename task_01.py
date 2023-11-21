class ListStatistics:
    """
    Класс для различных вычислений со значениями списков. В данном случае определенного среднего значения
    """
    def __init__(self, numbers):
        """
        Конструктор класса, инициализирует значения для списка
        :param numbers: Значения
        """
        self.numbers = numbers

    def calculate_average(self):
        """
        Вычисление среднего значения в списке
        :return: Среднее значение для списка
        """
        if not self.numbers:
            return 0

        return sum(self.numbers) / len(self.numbers)


class ListComparer:
    """
    Класс для сравнения списков. В данной реализации только средних значений списков
    """
    def __init__(self, list1, list2):
        """
        Конструктор класса, инициализирует экземпляры класса - списки list1_stats и list2_stats
        :param list1:
        :param list2:
        """
        self.list1_stats = ListStatistics(list1)
        self.list2_stats = ListStatistics(list2)

    def compare_averages(self):
        """
        Сравнивает средние значения двух списков и выводит результат.
        :return: Возвращает строку с результатом
        """
        avg_list1 = self.list1_stats.calculate_average()
        avg_list2 = self.list2_stats.calculate_average()

        if avg_list1 > avg_list2:
            return "Первый список имеет большее среднее значение"
        if avg_list2 > avg_list1:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
