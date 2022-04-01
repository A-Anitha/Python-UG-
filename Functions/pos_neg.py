def posneg(n,ls):
  n=0;
  p=0;
  for i in ls:
    if(i<0):
      n=n+1
    else:
      p=p+1
  print("no. of positive numbers : ",p)
  print("no. of negative numbers : ",n)

ls=[]
n=int(input("enter the list's' length : "))
print("enter the list elements : ")
for i in range(0,n):
  element=int(input())
  ls.append(element)
posneg(n,ls)
