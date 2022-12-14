#fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
#fruits.count('apple')
#fruits.count('tangerine')
#fruits.index('banana')
##fruits.index('banana', 4)

##fruits.reverse()
#print(fruits)

#fruits.append('grape')
#print(fruits)

#fruits.sort()
#print(fruits)

#fruits.pop()
#print(fruits)



# Make a list of colors. Duplicate colors are allowed, meaning you can use the same color name twice and print it out

color = ["red", "blue", "orange", "yellow", "perpule", "pink"]
# Add a single new color to the list you have created and print it out
color.append("black")
print(color)
# Add multiple colors to the list you have created and print it out
color.extend(["purpule", "whait"])
print(color)
# Print the index of your favorite color from the list
a = color.index("perpule")
print(a)
# Remove the last item is the colors list
color.pop()
print(color)

# Sort all the items in the list
color.sort()
print(color)