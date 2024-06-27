class Calculator:
    def a(self):
        test = [1, 2, 3, 4]
        result = list(map(lambda x: x * 3, test))
        print(result)

b = Calculator()
b.a()  