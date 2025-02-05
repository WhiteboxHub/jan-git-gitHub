# # age = 29
# # has_license = False

# # if age >= 18: # Outer condition
# #     if has_license: # Inner condition
# #        print("You can drive.")
# #     else:
# #        print("You need a driving license.")
# # else:
# #   print("You are too young to drive.")

# # #output : You can drive.






# # fruits = ["apple", "banana", "cherry"]


# # for fruit in fruits:
# #    print(fruit)







# #  /from 0 to 3


# # for i in range(4):
# #    if i == 1:
# #      pass
# #    print(f"Number: {i}")



# # for i in range(3):
# #     for j in range(3):
# #         print(i,j)









# #  else in loops 

# for i in range(5):
#     if i ==3:
#         break
#     print(i)
# else:
#     print("loop is finished")






# #  from 2 to 10
# for i in range(2, 11):
#    print(i)
# from 0 to 10, step 2
# for i in range(0,10,3):
#  print(i)





#  0 to 4 by while 
# x =0

# while(x<=4):
#     print(x)
#     x+=1










# x =5
# y=x
# y=10
# print(x)
# print(y)



# a =[1,2,4]
# b=a
# b.append(5)
# print(a)
# print(b)



# x = 10 
# y = 5.5
# result = x + y
# print(result)



# x = '10'
# print(type(x))
# y = int(x)
# print(y)
# print(type(y))









# my_dict = {
#     'name' :'mick',
#     'age':25,
#     'city':'New York'}
# print(my_dict['age'])
# my_dict['age']=26
# my_dict['email']="example@gmial.ocm"
# Value=my_dict.pop('city')
# print(Value)
# del my_dict["email"]

# print(my_dict.items())



# my_set = {1,2,3,4}
# my_set.discard(9)
# print(my_set)





my_str= "  hlo"
str2 = "world     "


age= 20


print('mystr : %s,age :%d'%(my_str,age))


print(f'mystr :{my_str},AGe:{age}')
print("MY_str:{} , Age:{}".format(my_str,age))

# print(my_str[0:3])



res = my_str + " " + str2
print(res.strip())

# print(my_str.upper())

# print(my_str[0])
# print(len(my_str))
