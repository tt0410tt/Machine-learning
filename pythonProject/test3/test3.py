class a:
    b=1
    def c(self,numbers):
        input1= input("첫번째 숫자를 입력하세요:")
        input2= input("두번쨰 숫자를 입력하세요:")
        total= float(input1)+float(input2)
        return print("두수의합은 %d입니다"%total)
a.c(a,[1,3,5,6,7,8,9])
