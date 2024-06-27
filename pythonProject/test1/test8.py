class a:
    c=(1,2,3)
    def b(self):
        d=list(self.c)
        d.append(4)
        self.c=tuple(d)
        print(self.c)
a.b(a)
