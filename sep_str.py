#Python program to drop all digits from a string.
digits = [str(x) for x in range(10)];
mystr = 'He12llo, Py00th55on!';
chars = [];
for x in mystr:
   if x not in digits:
      chars.append(x);
newstr = ''.join(chars);
print (newstr);
#another way
#mystr = 'He12llo, Py00th55on!'
#newstr = ''.join([x for x in mystr if not x.isdigit()])
#print(newstr)