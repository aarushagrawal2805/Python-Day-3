data = { "class": {"student": {"name": "Anil","marks": {    "physics": 70,    "history": 80}}}}
print("Initial Dict :",data)
data["class"]["student"]["name"]="Amit"
print("Modify Student Name is :",data)