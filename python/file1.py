#f = open("python/새파일.txt", 'r')
#lines = f.readlines()
#for line in lines:
#    print(line)
#f.close() 


#f = open("python/새파일.txt", 'r')
#lines = f.readlines()
#for line in lines:
#    print(line, end='')
#f.close() 

#f = open("python/새파일.txt", 'r')
#data = f.read()
#print(data)
#f.close()

import sys

args = sys.argv[1:]
for i in args:
    print(i)
    
