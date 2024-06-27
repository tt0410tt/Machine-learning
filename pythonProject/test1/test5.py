class a:
    c="a:b:c:d"
    def b(self):
        d=self.c.replace(":","#")
        print(d)
        
a.b(a)
