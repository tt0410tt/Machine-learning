class a:
    a = b=[1,2,3]
    def d(self):
        self.a[1]=4
        
a.d(a)
print(a.b[1])
print("b는 a를 참조했기때문에 a의 값이 변하면 b도 값이 변하게 보이게 된다")