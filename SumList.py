#def add(num):
 #   tot=0;
  #  for i in num:
   #     tot+=i;
    #return tot;
#lists=[12,2,3,15,16];
#print("The list is ",lists);
#print("The sum of all items in the list is ",add(lists));
#By using recursion methord
def add(num):
    if len(num)==1:
        return num[0];
    else:
        return (num[0]) + add(num[1:]);
print("The sum of list is: ",add([1,2,3]));