#Python program to convert a string with binary digits to integer.
mystr = input("Enter any Binary number :");

def strtoint(mystr):
   for x in mystr:
      if x not in '01': return "Error. String with non-binary characters";
   num = int(mystr, 2);
   return num;
print ("binary:{} integer: {}".format(mystr,strtoint(mystr)));