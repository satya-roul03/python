index=int(input("Enter the number of items to be insert in the list: "));
l=[];
for i in range(index):
    lists=input("Enter the items no {}: ".format(i+1));
    l.append(lists);
print("The list is: ",l);