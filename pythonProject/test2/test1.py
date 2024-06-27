class a:
    b="Life is too short, you need python"
    def c(self):
        if "wife" in self.b:
            print ("wife")
        elif "python" in self.b and "you" not in self.b:
            print("python")
        elif "shirt" not in self.b:
            print("shirt")
        elif "need" in self.b:
            print("need")
a.c(a)
print("wife 는 없으니 출력이안돼고 python은있으나 you도 있어서 출력이안됌, shirt는 있으니 출력이되고 마지막은 elif므로 if문을 탈출하여 출력하지 않는다")