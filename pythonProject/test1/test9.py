class a:
    c=dict()
    def b(self):
        self.c['name']='python'
        self.c[('a',)]='python'
        print("self.c[[1]]='python' 딕셔너리의 인자로 리스트를 받을수는 없어서")
        self.c[250]='python'
        
a.b(a)
