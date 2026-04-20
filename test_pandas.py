import pandas as pd
data={"Name":["Hari","Ram","Jadu"],
"Age":[21,23,25],
"Salary":[30000,35000,40000]};
df=pd.DataFrame(data);
print(data);
print(df);
print("Get data from CSV file");
rdcsv=pd.read_csv("sales_data.csv");
print(rdcsv);
print("Get data from Excel file");
rdxl=pd.read_excel("sales_data.xlsx");
print(rdxl);
print("Show data  upper 3 data ")
print(rdxl.head(3));
print("Show data  buttom 3 data ")
print(rdxl.tail(3));
print("The information of data");
print(rdxl.info());
print("Describe the data");
print(rdxl.describe());
print("Show the data isnull or not in side data");
print(rdxl.isnull());
print("Show columan wise")
print(rdxl.isnull().sum());
print("Check duplicated");
print(rdxl["Order ID"].duplicated().sum());
print("Remover/drop duplicate order id from sales.xlxs file ");
print(rdxl.drop_duplicates("Order ID"));