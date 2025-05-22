"""
# single inheritance

class father :
    x =100
    y =2

    def subtraction(self):
        minus = self.x - self.y
        print(minus)



class son (father) :
    pass

obj= son()
obj.subtraction()
print(obj.x)

obj= father()
obj.subtraction()
print(obj.x)
print(obj.y)
"""
from test import father


# multiple inheritance

class Father :

    x = 10
    y =5

    def add(self):
        print(self.x + self.y)

    def mul(self):
        print(self.x * self.y)




# this is mother class
class Mother  :

    a =4
    b =8

    def biyog(self):
        print(self.a - self.b)

    def vag(self):
        print(self.a / self.b)




# this is son class
class Son (Father,Mother):
    pass

obj = Son()

# father
obj.add()

# mother
obj.biyog()




"""
# Multilevel Inheritance 

class GrandFather :
    x =10
    y =30

    def add(self):
        print(self.x + self.y)

    def biyog(self):
        print(self.y - self.x)

class Father(GrandFather):
    pass

class Son(Father):
    pass


obj = GrandFather()
obj.add()
"""









