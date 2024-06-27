import sys
class a:
    def c(self,numbers):
        arg=sys.argv[1:]
        result=0
        for i in arg:
            result+=float(i)
        print(result)
a.c(a,[1,3,5,6,7,8,9])
