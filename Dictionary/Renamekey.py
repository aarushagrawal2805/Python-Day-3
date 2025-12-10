Data = {"name": "Amit", "age": 20, "city": "Indore", "marks": 88}

#Rename key of dict
Data["Address"]=Data.pop("city")
print(Data)