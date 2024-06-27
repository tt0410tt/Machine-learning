import datetime

class Calculator:
    def a(self):
        data1 = datetime.datetime(1995,12,15)
        data2 = 19981006
        data1.date(data2)
        
        print(data1)

b = Calculator()
b.a()