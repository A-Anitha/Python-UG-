print("-----------List operations------------")
l1=["english",100,"tamil",99]
l2=[55,66,22,11,88,66]
print("LIST ONE:",l1)
print("LIST TWO:",l2)
print("1.Append \n2.Insert \n3.Extend \n4.Remove \n5.pop \n6.Reverse \n7.Length \n8.Maximum of the list \n9.Minimum of the list \n10.To count the occurance \n11.Sort \n12.To fetch index value of an element \n13.Concatenation of two list \n14.To repeate the list \n15.To clear")
print("-----------------------------------------------")
n=int(input("enter you choice:"))

if(n==1):
    print("Adding a string maths:")
    l1.append("maths")
    print(l1)
elif(n==2):
    print("Adding a element in particular index:")
    l1.insert(4,"science")
    print(l1)
elif(n==3):
    print("To extend elements:")
    l1.extend(["social",97])
    print(l1)
elif(n==4):
    print("Removing a element:")
    l1.remove(99)
    print(l1)
elif(n==5):
    print("Poping up an indexing element")
    l1.pop(2)
    print(l1)
elif(n==6):
    print("Reversing a list:")
    l1.reverse()
    print(l1)
elif(n==7):
    print("Length of 1st list is:",len(l1))
    print("Length of 2nd list is:",len(l2))
elif(n==8):
    print("Maximum of 2nd list:",max(l2))
elif(n==9):
    print("Minimun of 2nd list id:",min(l2))
elif(n==10):
    print("occurance of 22 is:",l2.count(22))
elif(n==11):
   print("Sorting 2nd list:",l2.sort())
   print(l2)
elif(n==12):
    print(l2.index(4))
elif(n==13):
    print("Concatenating two lists:")
    print(l1+l2)
elif(n==14):
    print("Repeating a list for 2 times:")
    print(l2*2)
elif(n==15):
    print("Clearing list 1:")
    l1.clear()
    print(l1)
else:
    print("Invalid input,choose number from 1 to 15")
