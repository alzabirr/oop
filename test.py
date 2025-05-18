"""
# 1. class blue print
class myclass :
    x = 10
    y = 20
    z = 30
    ans = x+y+z
obj1 = myclass()
print(obj1.x)


obj2 = myclass()
print(obj2.ans)
"""
from mimetypes import add_type

# from problem import my_class

"""
# class method 
class myclass:
    a = 1
    b =4
    def fun(self):
        sum = self.a + self.b
        return sum

obj = myclass()
print(obj.fun())





class my :

    def fun(self,x,y):
        sum = x+y
        return sum

    def fun2(self):
        print("okk man i am done")



obj = my()

print(obj.fun(1,6))
obj.fun2()


"""

"""
conostructor method

class my_class :
    def __init__(self):
        print("okk")


obj = my_class()



class my :

    a = 1
    b = 2
    def __init__(self):
        sum = self.a + self.b
        print(sum)
obj1 = my()
"""
"""
# conostructor  with parameters
class my :

    def __init__(self,a,b):
        add = a+b
        print(add)

obj1 = my(1,5)
"""





#
# class my :
#     x =10
#     y =20
#
#     def __init__(self,z):
#         self.z = z
#         # print(z)
#
# obj1 = my(100)
# print(obj1.z)




"""
# change class variable using consontructor paramiters
class my :
    x = 10
    y =2

    def __init__(self,z_value,x_value):
        self.z =z_value
        self.x = x_value
        print(z_value+x_value)


obj = my(200,100)

"""










# class my_class:
#
#     @staticmethod
#     def addtwo(a,b):
#         z = a+b
#         print(z)
#
# # my_class.addtwo(1,5)
# obj = my_class()
# obj.addtwo(1,5)




# class my_class:
#     a = 10
#     b = 2
#     z = a+b
#     print(z)
#
# obj = my_class()
# obj.z



"""
# static method
#
# class myclass :  eta ke static method a porinoto
#     x = 1
#     y = 2
#
#     def addtwo(self):
#         z = self.x + self.y
#         print(z)
#
# obj= myclass()
# obj.addtwo()


class myclass :
    x =10
    y = 2

    @staticmethod
    def addtwo():
        z = myclass.x+ myclass.y
        print(z)
myclass.addtwo()
print(myclass.x)
"""
# static variable
#
# class myclass :
#     x = 10
#     y = 3
# print(myclass.x)
#

# class my :
#     a =1
#     b = 2
#
#     def myfun(self,x,y):
#         sum = x+y
#         return sum
# obj1 = my()
# print(obj1.myfun(1,6))

# class my :
#     a = 1
#     b =3
#
#     def __init__(self):
#         z = self.a + self.b
#
#         print(z)
#
#
# obj1 = my()


# static


class my :
    x = 1
    y =3
    z =x+y

print(my.x)
print(my.z)






















































