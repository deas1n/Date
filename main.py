class Date:
    """
    This is a class for representing and working with a calendar date

    Attributes:
    _day (int): (1-31 still depends on the month or year)
    _month (int): (1-12)
    _year (int): (integers)
    """

    def __init__(self, year: int, month: int, day: int):
        """
        Initializing the Date object with validation

        Parameters:
            day (int): day
            month (int): month
            year (int): year

        Causes:
            TypeError: if the types are not integers
            ValueError: when the values do not meet the permissible limits
        """
        if not all(isinstance(i, int) for i in [year, month, day]):
            raise TypeError("Parameters must be integers")

        if year < 0:
            raise ValueError("The year cannot be negative")

        if not 1 <= month <= 12:
            raise ValueError("The month must be between 1 and 12")

        if not 1 <= day <= Date.days_in_month(month, year):
            raise ValueError(f"Wrong day of the month {month} in the year {year}")

        self._day = day
        self._month = month
        self._year = year

    @staticmethod
    def days_in_month(month, year):
        """
        It returns the number of days in a given month, taking into account the lean year

        Parameters:
            month (int): month
            year (int): year

        return:
            int number of days
        """
        if month == 2:
            return 29 if Date.is_leap_year_static(year) else 28
        if month in [4, 6, 9, 11]:
            return 30
        return 31

    @staticmethod
    def is_leap_year_static(year):
        """
        Checks if the year is a leap year
        """
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def is_leap_year(self):
        """
        Checks whether the year of the object is a leap year

        return:
            True if the year is leap year
        """
        return Date.is_leap_year_static(self._year)

    def iso_format(self):
        """
        Checks the date in the format YYYY-MM-DD


        return:
            date in ISO format
        """
        return f"{self._year:04d}-{self._month:02d}-{self._day:02d}"

    def day_of_year(self):
        """
        Checks the sequential number of the day in the year (from 1 to 365/366)

        return:
            day number in the year
        """
        days = 0
        for m in range(1, self._month):
            days += self.days_in_month(m, self._year)
        return days + self._day

    def __str__(self):
        """
        Returns a string value of the date

        return:
             Format YYYY-MM-DD
        """
        return f"{self._day:02d}-{self._month:02d}-{self._year:04d}"

    def __eq__(self, other):
        """
        Checks for equality of two dates
        """
        return (self._day, self._month, self._year) == (other._day, other._month, other._year)

    def __lt__(self, other):
        """
        Check if the current date is less than another date
        """
        return (self._day, self._month, self._year) < (other._day, other._month, other._year)

    def __gt__(self, other):
        """
        Checks whether the current date is greater than another
        """
        return (self._day, self._month, self._year) > (other._day, other._month, other._year)

    def __sub__(self, other):
        """
        Calculates the difference between two dates in days

        return:
            number of days of difference
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
        print(f"Error creating a date: {e}")

    print(d1)
    print(d2.iso_format())

    print(d2.is_leap_year())
    print(d2.day_of_year())

    print(d1 == d2)
    print(d1 < d2)
    print(d1 > d2)

    print(d2 - d1)

