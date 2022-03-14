# 클래스의 상속

class FourCal:
    #생성자
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
class MoreFourCal(FourCal):
    # add(), mul(), sub(), div() -> class FourCal
    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second    

# a = MoreFourCal(4,2)
# print(a.add())
# print(a.pow()) 

# a = FourCal(4,0)
# print(a.div())

# a = SafeFourCal(4,0)
# print(a.div())

a = FourCal(4,2)
b = FourCal(6,2)