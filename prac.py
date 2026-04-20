import pandas as pd
import numpy as np
from io import StringIO
rd=pd.read_excel("test.xlsx");
print(rd);
print(rd.describe());
print(rd.head(3));
print(rd.tail(3));
print(rd.duplicated().sum());
print(rd.info());
print(rd.drop_duplicates());
print(rd.isnull().sum());
print();
print(rd.dropna());
print(rd.replace(np.nan,"Empty"));
rd["Customer_ID"]=rd["Customer_ID"].replace(np.nan,60);
print(rd);
#rd["Customer_ID","Discount","Payment_Method"]=rd["Customer_ID","Discount","Payment_Method"].replace(np.nan,60,10,"UPI");
#print(rd);
rd.loc[(rd["Discount"]==0), "Is_Discount"]="No";#add new column (Is_Discount)
rd.loc[(rd["Discount"]>0, "Is_Discount")]="Yes";
print(rd);
#print(rd.fillna(method = "bfill"));
#print(rd.fillna(method = "ffill"));
# Create string representing CSV data
data = """S.No,Name,Age,City,Salary
1,Tom,28,Toronto,20000
2,Lee,32,HongKong,3000
3,Steven,43,Bay Area,8300
4,Ram,38,Hyderabad,3900"""
# Use StringIO to convert the string data into a file-like object
obj = StringIO(data)
# read CSV into a Pandas DataFrame
df = pd.read_csv(obj)
print(df)
d1={"Emp_Id":[101,102,103],
"Emp_Name":["Ram","Syam","Jadu"],
"Age":[21,25,20]};
d2={"Emp_Id":[101,102,103],
"Salary":[15000,20000,30000]};
df1=pd.DataFrame(d1);
df2=pd.DataFrame(d2);
print(df1);
print();
print(df2);
print();
print(pd.merge(df1,df2,on = "Emp_Id",how="left"));
print();
print(pd.concat([df1,df2]));
df3=df1.copy();
print();
print(df3);
df3.loc[0,"Salary"]=25000;
df3.loc[1,"Salary"]=30000;
df3.loc[2,"Salary"]=35000;
print(df3);
#print(df1.compare(df3,align_axis=0,keep_equal=2));
t1={"Keys":["k1","k2","k1","k2"],
"Names":["Ram","Syam","jadu","Arthorb"],
"Colors":["Red","Blue","Green","White"],
"Grade":["1st","2nd","3rd","4th"]};
df4=pd.DataFrame(t1);
print(df4);
print(df4.pivot(index="Keys",columns="Names",values=["Colors","Grade"]));
#print(pd.melt(df4, id_vers=["Names"],value_vars=["Colors"]));
print(pd.melt(df4));