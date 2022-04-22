print("DICTIONARY OPERATIONS")
print("----------------------------------")
dic1={"sub":"english","color":"blue","flavour":"vanilla"}
print("1.Display the dictionary elements \n2.Display the datatype \n3.length of a dictionary \n4.To add items to the dictionary \n5.To update the value of a key \n6.create a copy of the dictionary \n7.remove items from the dictionary \n8.remove all the items from the dictionary \n9.display only keys \n10.display only values \n11.display full dictionary using for loop \n12.check whether an element exists or not" )
print("----------------------------------")
n=int(input("enter your choice:"))

if(n==1):
    print("Displaying dictionary items:",dic1)
elif(n==2):
    print("Datatype of the elements:",type(dic1))
elif(n==3):
    print("Length of the dictionary:",len(dic1))
elif(n==4):
    dic1["flavour2"]="chocolate"
    print("adding elements to the dictionary:",dic1)
elif(n==5):
    dic1["flavour"]="Black current"
    print("Updated elements to the dictionary:",dic1)
elif(n==6):
    dic2=dic1.copy()
    print("Original dictionary:",dic1)
    print("Copied dictionary:",dic2)
elif(n==7):
    del dic1["sub"]
    print("Removed a element from the dictionary:",dic1)
elif(n==8):
    dic1.clear()
    print("Removed all the elements from the dictionary:",dic1)
elif(n==9):
    print("Displaying keys")
    for i in dic1.keys():
      print("keys -",i)
elif(n==10):
    print("Displaying values")
    for j in dic1.keys():
      print("Values -",j)
elif(n==11):
    print("Displaying both keys and values")
    for i,j in dic1.items():
      print(i,"related to",j)
elif(n==12):
  a=str(input("enter a key to check the existence:"))
  if(dic1.get(e)==None):
    print("No such element is exists")
  else:
    print("Element exists")
else:
    print("Invalid Input")
