import os

class Calculator:
    path = "C:\\Users\\user\\Desktop\\workspace\\pythonProject\\test4"

    file_list = os.listdir(path)
    def a(self):
        print(self.file_list)

b = Calculator()
b.a() #doit폴더없어서 현재폴더 절대경로를 지정함