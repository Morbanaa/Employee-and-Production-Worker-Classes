class Employee():
    def __init__(self,name,number):
        self.name = name
        self.number = number


class Production_Worker(Employee):
    def __init__(self,name,number,shift_num,pay_rate):
        super().__init__(name,number)
        self.shift_num = shift_num
        self.pay_rate = pay_rate

    def display(self):
        print(f"{self.name:<20}{self.number:<20}{self.shift_num:<20}${self.pay_rate:.2f}")