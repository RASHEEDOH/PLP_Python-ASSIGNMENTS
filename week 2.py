#create empty list
my_list = []

#append items into the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert a new list item at index 1 of the list
my_list.insert(1, 15)

#create second list and extent it with my_list
second_list =[50,60,70]
my_list.extend(second_list)

#remove items from my_list
my_list.pop()

#sort items on my_list
my_list.sort()

#find and prints item at index 
item_list= my_list.index(30)
print(item_list)

#prints new list with all items
print(my_list)

