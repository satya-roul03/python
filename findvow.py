#Python program to find number of vowels in a given string.
mystr = "All animals are equal. Some are more equal";
vowels = "aeiou";
count=0
for x in mystr:
   if x.lower() in vowels: count+=1
print ("Number of Vowels:", count);