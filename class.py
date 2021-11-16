class UniversityEmployee:
    def __init__(self, code, s_name, name, p_name, position, emp_date, wage):
        self.__c = code
        self._s = s_name
        self._n = name
        self._pn = p_name
        self._p = position
        self.__e = emp_date
        self.__w = wage

    def print_date(self):
        print('Сотрудник университета ', self._s, self._n, self._pn, ', код сотрудника:', self.__c, ', должность: ',
              self._p, ', дата приема на работу:', self.__e, ', заработная плата: ', self.__w, 'рублей')


people1 = UniversityEmployee(13098, 'Иванов', 'Иван', 'Иванович', 'Системный администратор', '12 января 2007', 120000)
people2 = UniversityEmployee(21031, 'Кузьмин', 'Игорь', 'Петрович', 'Начальник отдела кадров', '21 марта 2013', 140000)
people1.print_date()
people2.print_date()
