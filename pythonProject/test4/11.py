import time

class Calculator:
    path = time
    def a(self):
        print(str(self.path.localtime().tm_year)+"/"+
              str(self.path.localtime().tm_mon)+"/"+
              str(self.path.localtime().tm_mday)+" "+
              str(self.path.localtime().tm_hour)+":"+
              str(self.path.localtime().tm_min)+":"+
              str(self.path.localtime().tm_sec))

b = Calculator()
b.a() 