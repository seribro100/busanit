# 파일 열기
f = open("python/새파일.txt", 'w')

for i in range(11, 21):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)


# 파일 닫기
f.close()

