# class car:
#     def __init__(self,make ,model):
#         self.make=make
#         self.model=model

#     def drive(self):
#         print(f"the {self.make}   {self.model}")

# car1 = car("toyota","innova")
# car2= car("honda","civic")

# # car1.drive()
# # car2.drive()
    




# # class Myclass:
# #     x=10

# # a1=Myclass()

# # print(a1.x)





# class Person:
#     class_att="hello"
#     def __init__(sf,name,age):
#         sf.name=name
#         sf.age=age

#     def myfunc(s):
#         print(s.name)

# p1=Person("jhon",25)
# p2=Person("shiva",25)

# print(p2.class_att)
# print(p1.class_att)
# print(p1.myfunc())


class calc:
    def add(self,a ,b=0,c=0):
        return a+b+c
    
c=calc()
print(c.add(5))
print(c.add(5,1))
print(c.add(4,5,6))