# write a program to separate the folloeing string into coma(,)separete value
a="auto.value.coma";
b=a.split(",");
print(b);
c=a.replace(".","-");
print(c);
inp=input("Enter a string : ");
d=inp[::-1];
print("The reverse from of string is: ",d);
if inp == d:
    print(inp," is palindrome");
else:
    print(d," is not palindrome");
lists=['1','Hello','everyone1','how','are','you','are','u','fine','?'];
print(lists);
print(lists[1:3]);
print(lists[3:6]);
print(lists[6:10]);
print(lists[::-1]);
print(lists[-1:-5:-1]);
print(lists[1:10:2]);
#for i in lists:
 #   print(i);
#for i in range(len(lists)): #print by  renge methord
 #   print(i,":",lists[i]);
[print(i) for i in lists] #short hand for loop
e=lists.append('satya');
print(e);
f=['for','extend'];
g=lists.extend(f);
print(g);
#print(lists.index('Satya'));
co=lists.copy();
print(co);
print(lists.reverse());
print(lists.sort());
print(lists.clear());