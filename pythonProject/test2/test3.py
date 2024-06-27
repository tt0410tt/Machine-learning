class a:
    b=1
    def c(self):
        i=0
        while True:
            i+=1
            if i>5:
                break
            print("*"*i)
a.c(a)
