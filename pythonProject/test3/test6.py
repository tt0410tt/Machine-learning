class a:
    b=1
    def c(self,numbers):
        data=""
        while(True):
            user_input=input("적고싶은말을 적어주세요 종료0:")
            f=open("test1.txt",'a+')
            if user_input=="0":
                f.close()
                break
            f.write(user_input)
            print(user_input)
            f.close()
        
        print("이때까지 적은것은 이것입니다."+open("test1.txt",'r+').read())
a.c(a,[1,3,5,6,7,8,9])
