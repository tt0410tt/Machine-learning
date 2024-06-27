class Calculator:
    result=0
    def __init__(self):
         self.result=0
    def __init__(self,fix):
        self.result=fix
    def add(self, x):
        self.result= x + self.result

    def subtract(self, x):
         self.result= self.result-x 

    def multiply(self, x):
         self.result= x * self.result

    def divide(self, x):
        if x != 0:
             self.result= self.result/x 
        else:
             self.result= "0으로 나눌 수 없습니다."
        pass    
if __name__ == '__main__':
    a=Calculator
    a.show(a)