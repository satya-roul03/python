import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from io import StringIO
x=[98,67,96,80,99];
y=["Part1","Part2","Part3","Part4","Part5"];
colors=["red","blue","green","yellow","orange"];
plt.bar(y,x,color=colors,edgecolor="block");
plt.xlabel("Parts of Harry Potter",fontsize=17);
plt.ylabel("Populatity",fontsize=17);
plt.title("Populatity of different parts herry potter",fontsize=20);
#plt.show(); 


data=pd.read_excel("test.xlsx");
df=pd.DataFrame(data);
print(df);
plt.bar(df["Name"],df["Age"]);
#plt.show();


data = """S.No,Name,Age,City,Salary
1,Tom,28,Toronto,20000
2,Lee,32,HongKong,3000
3,Steven,43,Bay Area,8300
4,Ram,38,Hyderabad,3900"""
# Use StringIO to convert the string data into a file-like object
obj = StringIO(data);
# read CSV into a Pandas DataFrame
df = pd.read_csv(obj);
print(df);
group_by=df.groupby("Age")["Salary"].sum();
print(group_by);
plt.bar(group_by.index,group_by.values);
#plt.show();
plt.plot(y,x,marker="*",ls="--",color="red");
#plt.show();


x=[98,67,96,80,99];
y=["Part1","Part2","Part3","Part4","Part5"];
z=[80,90,100,75,85];
plt.plot(y,x,marker="*",ls="--",color="red",label="Part1");
plt.plot(y,z,marker="+",color="blue",label="Part2",alpha=0.5);
plt.legend();
#plt.show();


x=np.random.randint(1,10,50);
y=np.random.randint(10,100,50);
color=np.random.randint(10,100,50);
plt.scatter(x,y,marker="*",cmap="viridis",c=color);#we can use cmap="hot"/"cool" etc.
plt.colorbar();
#plt.show();


x=[30,10,20,30,10];
y=["Part1","Part2","Part3","Part4","Part5"];
#plt.pie(x);
c=["red","green","blue","yellow","orange"];
exp=[0,0,0,0,1];
plt.pie(x,labels=y,colors=c,explode=exp,shadow=True,autopct="%.2f",startangle=100);
#plt.show();

import matplotlib.pyplot as plt
l=[12,22,43,33,56,66,87,77,90];
#Lower Fourse(LF),Upper Fourse(UF)
#Q1=25/100*(Number of items+1) 25/100*(9+1)=2.5
#Q3=75/100(9+1)=7.5
#Inter Quader Range(IQR)=Q3-Q1=7.5-2.5=5
#LF=Q1-1.5(IQR)=2.5-1.5(5)=2.5-7.5=-5
#UP=Q3+1.5(IQR)=7.5+1.5(5)=7.5+7.5=15
#Min=1 Max=77 90 is outline element Median=874/10=87.4
plt.boxplot(l);
#plt.show();


l=[12,22,43,33,56,66,87,77,90];
l1=[10,20,30,40,50,60,70,80,90];
l2=[30,60,90];
#Lower Fourse(LF),Upper Fourse(UF)
#Q1=25/100*(Number of items+1) 25/100*(9+1)=2.5
#Q3=75/100(9+1)=7.5
#Inter Quader Range(IQR)=Q3-Q1=7.5-2.5=5
#LF=Q1-1.5(IQR)=2.5-1.5(5)=2.5-7.5=-5
#UP=Q3+1.5(IQR)=7.5+1.5(5)=7.5+7.5=15
#Min=1 Max=77 90 is outline element Median=874/10=87.4
addL=[l,l1,l2,l,l1];
plt.boxplot(addL);
#plt.show();

his=[10,20,12,23,22,34,33,45,44,56,55,67,66,78,77,89,88,90,99];
plt.hist(his,bins=12,egdecolor="black",color="pink");# we can use bins=len(his) means length of histogram
#plt.show();


violin=[10,20,30,60,40,50,20,40,50,0,60,30,50,40,80,30,80,90];
plt.violinplot(violin,showmedians=True);
#plt.show();

st=[10,30,60,90,80,70,60,80];
plt.stem(st,linefmt="--",markerfmt="D",basefmt="*",orientation="horizontal",);
#plt.plot(st);
#plt.show();

days=[1,2,3,4,5,6,7];
NOP1=[5,10,30,20,35,60,80];
NOP2=[50,60,30,75,80,90,120];
NOP3=[8,20,50,60,70,90,100];
plt.stackplot(days,NOP1,NOP2,NOP3,labels=["week1","week2","week3"]);
plt.legend();
#plt.show();

x=[1,2,3,4,5];
y=[10,20,30,40,50];
y1=[12,23,34,56,67];
y2=[11,22,33,44,55];
y3=[12,40,35,60,65];
plt.figure(figsize=[5,3]);
plt.plot(x,y,label="Male");
plt.plot(x,y1,label="Female");
plt.plot(x,y2,label="Kids");
plt.plot(x,y3,label="Blanks");
plt.legend(bbox_to_anchor=(.8,1.2),ncols=2);
#plt.show();



x=[1,2,3,4,5];
y=[10,20,30,40,50];
plt.subplot(3,3,1);
plt.bar(x,y);

x=[1,2,3,4,5];
y=[10,20,30,40,50];
plt.subplot(3,3,2);
plt.plot(x,y);

x=[1,2,3,4,5];
y=[10,20,30,40,50];
plt.subplot(3,3,3);
plt.scatter(x,y);
plt.colorbar();

x=[1,2,3,4,5];
y=[10,20,30,40,50];
plt.subplot(3,3,4);
plt.pie(x,labels=y);

x=[1,2,3,4,5];
y=[10,20,30,40,50];
plt.subplot(3,3,5);
plt.boxplot(x,y);

x=[1,2,3,4,5];
y=[10,20,30,40,50];
plt.subplot(3,3,6);
plt.hist(x);

x=[1,2,3,4,5];
y=[10,20,30,40,50];
plt.subplot(3,3,7);
plt.violinplot(x);

x=[1,2,3,4,5];
y=[10,20,30,40,50];
plt.subplot(3,3,8);
plt.stem(y);

x=[1,2,3,4,5];
y=[10,20,30,40,50];
plt.subplot(3,3,9);
plt.step(x,y);
plt.show(); 