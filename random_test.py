from cgi import print_arguments
import random

list1 = ["din mamma", "din papap"]

print(random.choices(list1, chanse=(90, 10),k=2 ))