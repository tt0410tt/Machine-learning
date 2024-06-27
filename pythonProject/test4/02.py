class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

    def minus(self, val):
        self.value -= val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        super().add(val)
        if self.value > 100:
            self.value = 100

a = MaxLimitCalculator()
a.add(50)
a.add(60)
print(a.value)