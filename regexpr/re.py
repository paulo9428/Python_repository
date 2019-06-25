import re

string = "123?45yy7890 hi 999 hello"

m1 = re.findall("\d", string)
m2 = re.findall("[0-9]{1,2}", string)
m3 = re.findall("[1-5]{1,2}", string)

print("m1=", m1)
print("m2=", m2)
print("m3=", m3)

