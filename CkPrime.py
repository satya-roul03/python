num=int(input("Enter the number for cheack the number is prime or not : "));
if num==1:
    print(num," is not a peime number");
#if num==2:
   # print(num," is a prime number");
for i in range(2,num):
    if num%i==0:
        print(num," is not a prime number");
        break;
else:
    print(num," is a prime number");