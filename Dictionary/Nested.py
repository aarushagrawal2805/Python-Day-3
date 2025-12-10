data = {'person': {'name': 'Amit', 'age': 30}}

def get_age(info):
    return info["person"]["age"]
#Nested Dictionary
dict1=get_age(data)
print("Amit Age is :",dict1)