class a:
    c=13
    def b(self):
        d=self.c%2
        if d ==1 :
            print("%d은 홀수입니다."%self.c)
        else:
            print("%d는 짝수입니다."%self.c)

a.b(a)
