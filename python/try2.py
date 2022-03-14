# try:
#     age=int(input('나이를 입력하세요: '))
# except:
#     # print('입력이 정확하지 않습니다.')
#     pass
# else:
#     if age <= 18:
#         print('미성년자는 출입금지입니다.')
#     else:
#         print('환영합니다.')      

class Bird:
    def fly(self):
        raise NotImplementedError
    
class Eagle(Bird):
    def fly(self):
        print("하늘을 날 수 있다")         

eagle = Eagle()
eagle.fly()