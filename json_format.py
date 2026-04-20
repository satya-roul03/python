#Convert following dictonary format to JSON formate
import json
student_data={"Name":"Satya","Age":21,"Mark":76};
print(type(student_data));
print(student_data);
data=json.dumps(student_data);
print(type(data));
print(data);
#access the value of age from following the JSON data
student_d="""{"Name":"Satya","Age":21,"Mark":76}""";
d=json.loads(student_d);
print ("The age of Satya is ",d['Age']);
