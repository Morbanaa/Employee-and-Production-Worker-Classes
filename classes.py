class Employee():
    # Constructor
    def __init__(self,name,number):
        self.name = name
        self.number = number


class Production_Worker(Employee):
    # Constructor
    def __init__(self,name,number,shift_num,pay_rate):
        super().__init__(name,number)
        self.shift_num = shift_num
        self.pay_rate = pay_rate
    
    # Getters
    def get_shift_num(self):
        return self.shift_num

    def get_name(self):
        return self.name

    # Setters
    def set_name(self,name):
        self.name = name

    def set_number(self,number):
        self.number = number

    def set_shift_number(self,shift_number):
        self.shift_num = shift_number

    def set_pay_rate(self,pay_rate):
        self.pay_rate = pay_rate

    # Display Method
    def display(self):
        print(f"{self.name:<20}{self.number:<20}{self.shift_num:<20}${self.pay_rate:.2f}")