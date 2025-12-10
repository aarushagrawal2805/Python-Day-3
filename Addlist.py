#write a program to add all of its elements into a given set
Color = {"Yellow", "Orange", "Black"}
ColorList1 = ["Blue", "Green", "Red"]

#Convert Set into List
List2=list(Color)
print("Set Convert into List :",List2)

#Now Extend Both list
ColorList1.extend(List2)
print("Extend Lists :",ColorList1)

#Now Convert List into Set
Set1=set(ColorList1)
print("Combine of Sets are :",Set1)
