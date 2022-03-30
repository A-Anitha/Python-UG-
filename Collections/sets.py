print("SET OPERATIONS")
s1={1,2,10.2,"python",(3,4,5)}
s2=set([10,22,6,44])

print("SET ONE : ",s1)
print("SET TWO : ",s2)
print("-------------------------------------------------------------")
print("\n1.To print set elemenets \n2.datatype of sets \n3.To add an element to set one \n4.To update elements  \n5.To discard \n6.To remove \n7.To clear s1 \n8.Union of two sets\n9.Intersection of two sets\n10.Difference of two sets\n11.Symmetric difference of two sets \n12.To check  set2 is disjoint of set1 \n13.To check  set2 is subset of set1 \n14.To pop \n15.To copy \n16.To display elements(USING FOR LOOP)  \n17.To display maximum value \n18.To display minimum value \n19.Sum of elements in set2 \n20.To sort \n21.Length of setS")
print("--------------------------------------------------------------")
n=int(input("\nenter your choice : "))

if(n==1):
  print("s1 elements : ",s1)
  print("s1 elements : ",s2)
elif(n==2):
  print("datatype of set1 : ",type(s1))
  print("datatype of set2 : ",type(s2))
elif(n==3):
  e=str(input("enter a string element to be added to the s1 : "))
  s1.add(e)
  print(s1)
elif(n==4):
  s2.update([11,22,33,44,55])
  print("updated elements in set2 : ",s2)

elif(n==5):
  s2.discard(2)
  print("2 in set2 is discarded",s2)
elif(n==6):
  s2.remove(4)
  print("element 4 is removed from set2",s2)
elif(n==7):
  s1.clear()
  print("set1 is cleared : ",s1)

elif(n==8):
  print("Union of set1 and set2 : ",s1|s2)
elif(n==9):
  print("Intersection of set1 and set2 : ",s1&s2)
elif(n==10):
  print("difference of set1 and set2 : ",s1-s2)
elif(n==11):
  print("symmetric difference of set1 and set2 : ",s1^s2)
elif(n==12):
  print("set2 is disjoint of set1 :  ",s1.isdisjoint(s2))
elif(n==13):
  print("set2 is superset of set1 : ",s1.issuperset(s2))

elif(n==14):
  v=s1.pop()
  print("poped element from set1 : ",v)
  print("set1 after poping: ",s1)
elif(n==15):
  s3=s1.copy()
  print("set1 copied to set3 : ",s3)
elif(n==16):
  print("elements in set1 : ")
  for i in set(s1):
    print(i)

elif(n==17):
  print("maximum value in set2 is : ",max(s2))
elif(n==18):
  print("minimum value in set2 is : ",min(s2))
elif(n==19):
  print("sum of elements in set2 : ",sum(s2))
elif(n==20):
  print("elements of set2 is sorted : ",sorted(s2))
elif(n==21):
  print("length of set1 is : ",len(s1))
else:
    print("invalid input!")
