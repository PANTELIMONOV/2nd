
# Создать класс Работник (свойства: ФИО (одно поле), позиция, зарплата, опыт работы).
# Реализовать методы:
# 1. выделять только имя или только фамилию из ФИО;
# 2. высчитывать зарплату на N месяцев;
# 3. вывести позицию с уровнем опытности (Junior, Middle, Senior <position>). Junior — менее 3 лет, Middle — от 3 до 6 лет, Senior — больше 6 лет.

class Employee:
    common_list=[]
    def __init__(self,fullname = None ,position= None,salary=0,experience = None):
        self.fullname=fullname
        self.position=position
        self.experience=experience
        self.salary=salary

    def set_surname(self):
       fullname=self.fullname
       surname=fullname.split()[0]
       return surname
    def calc_income (self,months_amount):
        self.mounths = months_amount
        return self.salary*self.mounths
    def set_position(self):
        if self.experience<=3:
            position ='Junior'
        elif self.experience>6:
            position = 'Senior'
        else:
            position ='Middle'
        return position

if __name__=="__main__":
    s=Employee(fullname = 'Petrov Ivan Olegivich',position= None,salary=800,experience = 4)
    print(s.set_surname())
    print(s.calc_income(12))
    print(s.set_position())


