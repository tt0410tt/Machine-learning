import random

class Calculator:
    def a(self):
        list1 = []
        while len(list1) < 7:
            number = random.randint(1, 45)
            if number not in list1:
                list1.append(number)
        print(list1)

b = Calculator()
b.a()