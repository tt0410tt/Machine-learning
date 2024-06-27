class a:
    b=1
    def c(self):
        e=3
        while e<=1000:
            self.b=self.b+e
            e=e+3
        print(self.b)
a.c(a)
