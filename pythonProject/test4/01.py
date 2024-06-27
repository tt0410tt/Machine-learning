class Calculator:
    def __init__(self):
        self.value=0
    def add(self,val):
        self.value+=val
    def minus(self,val):
        self.value-=val

a=Calculator()
a.add(10)
a.minus(7)
print(a.value)
