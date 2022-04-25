numbers = [273, 103, 5, 32, 65, 72, 800, 99]
Odd_sum = 0
Even_sum = 0
for i in numbers:
    if i % 2 == 0:
        Even_sum += i
    else:
        Odd_sum += i
    
print("짝수의 합:",Even_sum)
print("홀수의 합:",Odd_sum)                
