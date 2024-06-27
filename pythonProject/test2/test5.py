class a:
    b=[70,60,55,75,95,90,80,80,85,100]
    def c(self):
        total=0
        for i in self.b:
            total += i
        average=total/len(self.b)
        print(average)
a.c(a)
