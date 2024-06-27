class a:
    b=[1,2,3,4,5]
    def c(self):
        result=[x*2 for x in self.b if x%2==1]
        print(result)

a.c(a)
