class Date:
    def __init__(self, str_date):
        self.srt_date = str_date

    def temp_metod_1(self):
        return Date.make_date_to_int(self.srt_date)

    def temp_metod_2(self):
        return Date.verify_date(self.srt_date)

    @classmethod
    def make_date_to_int(cls, str_date):
        try:
            str_date = list(map(int, str_date.split("-")))
            print(
                f'Преобразование из @classmethod {[el for el in str_date]} {[type(el) for el in str_date]}')
        except:
            print("Неверные параметры")

    @staticmethod
    def verify_date(str_date):
        try:
            print(
                f'Валидация из @staticmethod День-{"True" if int(str_date.split("-")[0]) > 0 and int(str_date.split("-")[0]) <= 31 else "False"} '
                f'Месяц-{"True" if int(str_date.split("-")[1]) > 0 and int(str_date.split("-")[1]) <= 12 else "False"} '
                f'Год-{"True" if int(str_date.split("-")[2]) > 1900 and int(str_date.split("-")[1]) <= 2021 else "False"}')
        except:
            print("Неверные параметры")


my_date1 = Date('24-01-1977')
print(my_date1.srt_date)
my_date2 = Date('01-06-1981')
print(my_date2.srt_date)
my_date3 = Date('32-15-1981')
print(my_date3.srt_date)
print()
Date.make_date_to_int(my_date1.srt_date)
Date.make_date_to_int(my_date2.srt_date)
Date.make_date_to_int(my_date3.srt_date)
print()
my_date1.temp_metod_1()
my_date2.temp_metod_1()
my_date3.temp_metod_1()
print()
Date.verify_date(my_date1.srt_date)
Date.verify_date(my_date2.srt_date)
Date.verify_date(my_date3.srt_date)
print()
my_date1.temp_metod_2()
my_date2.temp_metod_2()
my_date3.temp_metod_2()
