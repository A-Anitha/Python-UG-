print("----------------------------------------------")
print("Tuple Operations")
print("----------------------------------------------")
t1=('english',91,'tamil',90.5)
t2=(11,33,100,88,4)
t4=("Pythonprogramming")
t5=("Python","Cloudcomputing","linux")
print("TUPLE ONE:",t1)
print("TUPLE TWO:",t2)
print("TUPLE THREE:",t4)
print("TUPLE FOUR:",t5)
print("----------------------------------------------")
print("1.Datatype of a tuple \n2.Length of the tuple \n3.To repeat the tuple \n4.To get element of the index \n5.Unpacking the elements \n6.concatenation of two tuples \n7.Removing an element from fist \n8.Excluding some characters from last \n9.Reversing tuple \n10.fetching elements of tuple \n11.fetching a portion from string tuple \n12.To delete a tuple \n13.Maximum of tuple \n14.Minimum of tuple \n15.sum of tuple \n16.sorting a tuple \n17.reverse sorting a tuple \n18.To convert elements \n19.Reverse indexing")
print("-----------------------------------------------")
n=int(input("enter your choice:"))

if(n==1):
    print("Datatype of tuple one is:",type(t1))
    print("Datatype of tuple two is:",type(t2))
elif(n==2):
    print("Length of tuple one:",len(t1))
    print("Length of tuple two:",len(t2))
elif(n==3):
    r=int(input("enter the no.of times to be repeat:"))
    print("Repeatation of tuple one:",t1*r)
    print("Repeatation of tuple two:",t2*r)
elif(n==4):
    i=int(input("enter the index number you want:"))
    print("element in the index value",i,"is :",t1[i])
    print("element in the index value",i,"is :",t2[i])
elif(n==5):
    a,b,c,d=t1
    print(a)
    print(b)
    print(c)
    print(d)
elif(n==6):
    t3=t1+t2
    print(t3)
elif(n==7):
    print(t4)
    rem=int(input("enter the places want to remove from first:"))
    print(t4[rem:])
elif(n==8):
    print(t4)
    rem=int(input("enter the place you want to remove from last:"))
    print(t4[:-rem])
elif(n==9):
    print(t4)
    print(t4[::-1])
elif(n==10):
    print(t4)
    e1=int(input("enter the starting range:"))
    e2=int(input("enter the ending range:"))
    print(t4[e1:e2])
elif(n==11):
    print(t5)
    i1=int(input("enter the index value :"))
    e1=int(input("enter the starting range:"))
    e2=int(input("enter the ending range:"))
    print(t5[i1][e1:e2])
elif(n==12):
    d=str(input("enter the tuple you want to delete (t1/t2/t4/t5): "))
    del(d)
elif(n==13):
    print(t2)
    print("Maximum of tuple two is :",max(t2))
elif(n==14):
    print(t2)
    print("Minimum of tuple two is :",min(t2))
elif(n==15):
    print(t2)
    print("Sum of the tuple two is :",sum(t2))
elif(n==16):
    print(t2)
    print("Sorting the tuple two :",sorted(t2))
elif(n==17):
    print(t2)
    print("Reverse sorting the tuple two:",sorted(t2,reverse=True))
elif(n==18):
    n="Python is a open source language"
    print(n)
    print("DataType before :",type(n))
    t3=tuple(n)
    print("DataType after changing :",type(t3))
elif(n==19):
    n="Python is a open source language"
    i=int(input("enter an index value:"))
    print("displaying an element of the index by reversing :",n[-i])
    print("Removing the indices by reversing :",n[:-i])
    print("reversing and also removing the particular index from tuple :",n[::-i])
else:
    print("invalid input!")
