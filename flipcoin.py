
#this is a simple version it this this was too easy to do tok me 10 mins to figer out but i got it


#import random 
#heads = 0
#tails = 0
#flips = 0

#while flips < 1:
#    flips = 1
#    c = random.randint(1, 2)
#    if c == 1:
#        print("heads got job now give me some! ")
#        heads = 1
#    else:
#        print("tails good jobb you got one tail now go be a emo")
#        tails = 1
#print("hi")


#this a better a more challenging version to me 1 google to do i unli google the while thing it flips 100 times end show you the total 
import random

tails = 0
heads = 0
flips = 0

while flips < 100:
    flips += 1
    coin = random.randint(1, 2)
    if coin == 1:
        print("you got heads")
        heads += 1
    else:
        print("you got tails")
        tails += 1
total = flips

print("___________________________________________________________________________________________________________________________________________")
print(total, "total flips")
print("total of heads", heads)
print("total of tails", tails)
print("___________________________________________________________________________________________________________________________________________")
