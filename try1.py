c = 0
a = [1,2,3]
try:
    c = 4 / 0
    print(a[2])
    
# except ZeroDivisionError as e:
#     print(e)

# except:
#     print("오류가 발생했습니다.")

# except ZeroDivisionError:
#     print("오류가 발생했습니다.")

# 0으로 나누기
except ZeroDivisionError:
    print("0으로 나누기 했습니다.")

# 인덱스 오류    
except IndexError as e:
    print(e)    
 
else:     
    print("오류가 없을때만 실행") 

print("항상실행됨")           