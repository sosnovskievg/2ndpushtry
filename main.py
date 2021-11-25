import random
mult=1
for i in range(1,100):
    if i %2 != 0:
        mult*=i
print(mult)

arr=[]
for i in range (1,500):
    if i%5 == 0:
        arr.append(i)
print(arr)

for i in range(1,497):
    if i%2==0:
        print(i, end=(" "))

given=[]
for i in range(100):
    given.append(random.randint(1,100))
repeated=[]
for i in given:
    if repeated.count(i)>0:
        continue
    elif given.count(i) > 2:
        repeated.append(i)

print('\n',given)
print(repeated)
