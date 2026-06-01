fruits = ["bananna","apple", "orange", "bananna", "coconut"]
fruits[1] = "pineapple"
fruits.append("grape") #adds grape at the end of list
fruits.remove("grape")
fruits.insert(3,"watermelon") #inserts value at index 0
# fruits.sort() #sorts alphabetically
fruits.reverse()
# fruits.clear()
print(fruits.index("bananna"))
print(fruits.count("bananna"))
for x in fruits:
    print(x)
print("apple" in fruits)
print("pineapple" in fruits)
print(len(fruits))
# print(help(fruits))  
#   
