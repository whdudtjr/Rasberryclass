
num = int(input())
count = 0
result = num
while True:
    count = count + 1
    New = int((result/10)) + (result%10)
    result = (result%10)*10 + (New%10) 

    if num == result:
        break
        
print(count)