import random 

#random_number = random.randint(1, 1000)
#random_number = random.random() * 100
#print(random_number)

i = 100 
j = 20e7

a = random.randrange(i, j)

try:
     b = random.randrange(j, i)

except ValueError:
     print("valueerror an randrange() since start < stop")

c = random.randint(100, 200)

try:
     d = random.randint(200, 100)

except ValueError:
     print("valueError on randint() sinc 200 > 100")

     
print('i=', i, ' and j =', j)
print("randrange() generated number:", a)
print("randint() generatednumber:", c)

    
