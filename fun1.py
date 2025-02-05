# def greet(name ):
#     return f"Hello {name }  age is {age}"

# print(greet(age=25,name='jhon'))


# def info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")
  


# info(name="jhon",age =20,country="USA")






# def divide(a, b, /, c, *, d):
#  return (a + b) / (c + d)
# # Valid calls:
# print(divide(5, 3, 2, d=1)) # Output:
# 2.6666666666666665
# # Invalid call:
# # print(divide(a=5, b=3, 2, d=1)) # SyntaxError





# def loacl():
#     x=10
#     print(x)

# loacl()
# print(x)



def outer_function():
     y = 20 # Enclosing variable
     def inner_function():
       print(y) # Accessible in the inner function


     inner_function()



outer_function()



len = 10
print(len("hello"))