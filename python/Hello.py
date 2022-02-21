#print("Hello World")

# def say():
#     return 'Hi'

# a = say()
# print(a)

# def add(a,b):
#     print("%d, %d의 합은 %d입니다." % (a, b, a+b))
    
# add(5,3)    

# def say():
#     print('Hi')

# say()

# def add(a,b):
#     result = a + b
#     return result

# result = add(5,3)
# print(result)

# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i
#     return result  

# result = add_many(1,2,3,4,5,6,7,8,9,10)
# print(result)

def add_and_mul(a,b):
    return a+b,a*b

result1, result2 = add_and_mul(3,4)
print(result1)
print(type(result1))
