class a:
    a = {'A' : 90,'B':80,'C':70}
    def b(self):
        result= self.a.pop('B')
        print(result)
        print(self.a)
        
a.b(a)
