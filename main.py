class Date:
    """
    Це клас для представлення та роботи з календарною датою

    Артрибути:
    _day (int): день (1-31 ще залежить від місяця чи року)
    _month (int): місяць (1-12)
    _year (int): рік (цілі числа)
    """

    def __init__(self, year: int, month: int, day: int):
        """
        Ініціалізація об'єкту Date з валідацією

        Параметри:
            day (int): день
            month (int): місяць
            year (int): рік

        Викликає:
            TypeError: якщо типи не є цілими числами
            ValueError: коли значення не відповідають допустимим межам
        """
        if not all(isinstance(i, int) for i in [year, month, day]):
            raise TypeError("Параметри повині бути цілими числами")

        if year < 0:
            raise ValueError("Рік не може бути від'ємним")

        if not 1 <= month <= 12:
            raise ValueError("Місяць має бути в межі від 1 до 12")

        if not 1 <= day <= Date.days_in_month(month, year):
            raise ValueError(f"Неправильний день в місяці {month} у році {year}")

        self._day = day
        self._month = month
        self._year = year

    @staticmethod
    def days_in_month(month, year):
        """
        Він повертає кіл-ть днів у даному місяці з урахуванням викосного року

        Параметри:
            month (int): місяць
            year (int): рік

        return:
            int кіл-ть днів
        """
        if month == 2:
            return 29 if Date.is_leap_year_static(year) else 28
        if month in [4, 6, 9, 11]:
            return 30
        return 31

    @staticmethod
    def is_leap_year_static(year):
        """
        Перевіряє, чи є рік високосним
        """
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def is_leap_year(self):
        """
        Перевіряє чи є рік об'єкта високосним

        Повертає:
            True, якщо рік високосний
        """
        return Date.is_leap_year_static(self._year)

    def iso_format(self):
        """
        Перевіряє дату у форматі YYYY-MM-DD


        return:
            дата в форматі ISO
        """
        return f"{self._year:04d}-{self._month:02d}-{self._day:02d}"

    def day_of_year(self):
        """
        Переверіє порядковий номер дня в році ( от 1 до 365/366)

        return:
            номер дня в році
        """
        days = 0
        for m in range(1, self._month):
            days += self.days_in_month(m, self._year)
        return days + self._day

    def __str__(self):
        """
        Повертає строкове значення дати

        return:
             Формат YYYY-MM-DD
        """
        return f"{self._day:02d}-{self._month:02d}-{self._year:04d}"

    def __eq__(self, other):
        """
        Перевіряє на рівність дві дати
        """
        return (self._day, self._month, self._year) == (other._day, other._month, other._year)

    def __lt__(self, other):
        """
        Перевіріє чи менша поточна дата іншій
        """
        return (self._day, self._month, self._year) < (other._day, other._month, other._year)

    def __gt__(self, other):
        """
        Перевіряє чи більша поточна дата за іншу
        """
        return (self._day, self._month, self._year) > (other._day, other._month, other._year)

    def __sub__(self, other):
        """
        Обчислює різницю між двома датами в днях

        return:
            кількість днів різниці
        """
        from datetime import date
        d1 = date(self._year, self._month, self._day)
        d2 = date(other._year, other._month, other._day)
        return abs(d1 - d2).days


if __name__ == "__main__":
    try:
        d1 = Date(2001, 9, 11)
        d2 = Date(2000, 2, 29)
        d_invalid = Date(1999, 4, 31)
    except (ValueError, TypeError) as e:
        print(f"Помилка при створенні дати: {e}")

    print(d1)   
    print(d2.iso_format())

    print(d2.is_leap_year())
    print(d2.day_of_year())

    print(d1 == d2)
    print(d1 < d2)
    print(d1 > d2)

    print(d2 - d1)