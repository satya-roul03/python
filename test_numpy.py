import numpy as np
import statistics as stats
a=np.array([1,3,2]);
b=np.array([4,5,6]);
c=np.array([[1,2,3],[4,5,6],[7,8,9]]);
print("Array A is:- \n",a);
print("Array B is:- \n",b);
print(" The addition of two arrays:-")#we can use np.add(a,b);
print(a+b);

print(" The subtaction of two arrays:-")#np.subtract(a,b);
print(a-b);

print(" The divition of two arrays:-")#np.divide(a,b);
print(a/b);

print(" The multiply of two arrays:-")#np.multiply(a,b);
print(a*b);

print(" The exponent of  arrays:-",np.exp(a));

print(" The power of  arrays:-",np.power(a,b));

print(" The squer root of  arrays:-",np.sqrt(a));

print("The number of 2nd position in A array is:- ",a[1]);
print("print the 2nd to 3rd pos. of A array is :- ",a[1:3]);
print("Print the 2 incrimet in B array:- ",b[0:3:2]);
print("print C aarray it is multi dimentional array:- ",c);
print(" ");
print(c[1:3]);
print(" ");
print(c[1,2]);
print(" ");
print(c[2,0:3]);
print(" ");
print("Show shape(row & column) of C array:- ",np.shape(c)); # for show shape(row & column) of c array
print("Show shape(row & column) of A array:- ",np.shape(a));
print("Size of C array:- ",np.size(c)); # for size of array
print("Size of B array:- ",np.size(b));
print("Number of dimention of C array:- ",np.ndim(c));# for number of dimention of array
print("Number of dimention of A array:- ",np.ndim(a));
print("Show what is the data type used of  C array:- ",c.dtype); # for show what is the data type used in array
print("Show what is the data type used of  A array:- ",a.dtype);
print("The length of C array is:- ",len(c));
print("The length of A array is:- ",len(a));
print("Convertion of data of array A:- ",a.astype(int));
print("The sum of the A array:- ",np.sum(a));
print("The min in A array:- ",np.min(a));
print("The max in A array:- ",np.max(a));
print("The sort of A array:- ",np.sort(a));
s=np.where(a == 3);
print("Find 3 in A Array:- ",s);
ss=np.searchsorted(a,3);
print(ss,"\n");
print("The mean of A array:- ",np.mean(a));
print("The median of A array:- ",np.median(a));
print("The mode of A array :- ",stats.mode(a));
print("The stander deviation of A Array:- ",np.std(a));
print("The squer of STD is:- ",(np.std(a)**2));
print("The varition of a array:- ",np.var(a));
print("The co-efficient of co reletion A and B:- ",np.corrcoef([a,b]));
print("The cumunity sum of A array:- ",np.cumsum(a));
print("The cumunity sum of A and B array:- ",np.cumsum([a,b]));
print("The cumulity product of A array:- ",np.cumprod(a));
print("The cumunity product of A and B array:- ",np.cumprod([a,b]));
