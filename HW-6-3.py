class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
        print(
            f'Имя: {self.name}, фамилия: {self.surname}, должность: {self.position}, оклад: {self._income["wage"]}, премия: {self._income["bonus"]}')


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.surname} {self.name}')

    def get_total_income(self):
        print(f'Доход с учетом премии равен {self._income["wage"] + self._income["bonus"]} \n')


programmer = Position('Иван', 'Иванов', 'программист', 50000, 10000)
programmer.get_full_name()
programmer.get_total_income()

director = Position('Петр', 'Петров', 'директор', 200000, 50000)
director.get_full_name()
director.get_total_income()
