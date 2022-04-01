def num(st,ed):
  print("excluding numbers from 1 to 25: :")
  for i in range(st,ed+1):
    if(i%5 != 0):
      print(i)

st=int(input("enter the starting range : "))
ed=int(input("enter the ending range : "))
num(st,ed)
