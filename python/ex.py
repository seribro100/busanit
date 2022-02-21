# test_list = ['own', 'two', 'three']
# for i in test_list:
#      print(i)

# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a:
#     print(first +last)

# a = [(1,2), (3,4), (5,6)]
# for i in a:
#      print(i, "-->", type(i))

# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#     number = number +1
#     if mark >= 60:
#         print("%d번 학생은 합격입니다." % number)
#     else:
#         print("%d번 학생은 불합격입니다." % number)

# marks = [90, 25, 67, 45, 80]

# number = 0 
# for mark in marks: 
#     number = number +1 
#     if mark < 60:
#         continue 
#     print("%d번 학생 축하합니다. 합격입니다. " % number)    

# marks = [90, 25, 67, 45, 80]
# for number in range(len(marks)):
#     if marks[number] < 60:
#         continue
#     print("%d번 학생 축하합니다. 합격입니다." % (number+1))

# for i in range(1, 10):
#     for j in range(2,10):
#         print(j,"*",i,"=",i*j, end="  ")
#     print()    

# a = [1,2,3,4]
# result = []
# for num in a:
#     result.append(num*3)
    
# print(result)        

# a = [1,2,3,4]
# result = [num *3 for num in a]
# print(result)

a = [1,2,3,4]
result = []
for num in a:
    if num % 2 ==0:
        result.append(num*3)
print(result)
