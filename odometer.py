a ,li = int(input()),[i for i in range(12,100) if i % 10 != 0 if i % 10 > i // 10]
if a % 10 == 0 or a% 10 <= a // 10 or a < 10 or a > 99:print('invalid')
for j in range(len(li) - 1):
  if li[j] == a:print(li[j-1],li[j+1])
if a == li[len(li)-1]:print(li[len(li)-2],li[0])
    
    
  
