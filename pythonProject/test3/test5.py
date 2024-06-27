class a:
    b=1
    def c(self,numbers):
        f=open("test.txt",'w')
        f.write("Life is too short")
        f.close()
        f2=open("test.txt",'r')
        print(f2.read())

a.c(a,[1,3,5,6,7,8,9])
