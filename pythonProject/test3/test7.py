class a:
    b=1
    def c(self,numbers):
        f=open("test7.txt",'w')
        f.write("Life is too short\nyou need java")
        f.close()
        f=open("test7.txt",'r')
        body=f.read()
        f.close()
        body.replace("java","python")
        f=open("test7.txt",'w')
        f.write(body)
        f.close()
a.c(a,[1,3,5,6,7,8,9])
