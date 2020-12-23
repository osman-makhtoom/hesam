import math

class Mathmatic():
    
    def __init__(self, first_num = 1, last_num = 1):
        self.first_num = first_num
        self.last_num = last_num
        
    def plus(self):
        if type(self.first_num) == int and type(self.last_num) == int:
            return self.first_num * self.last_num
        else:
            return 'Invalid Number! Please enter Integer'