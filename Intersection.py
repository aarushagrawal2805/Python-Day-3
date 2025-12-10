#Intersection between to 2 sets
Set1={1,2,3,10,23,20,40,50}
Set2={2,40,30,50,4,5,6}

#Intersection First Way .intersection
Set3=Set1.intersection(Set2)
print("Intersection Set ('.intersection'):",Set3)

#Intersection Second Way &
Set4=Set1&Set2
print("Intersection Set ('&') :",Set4)
