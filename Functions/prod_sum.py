def product_or_sum(n1,n2):
  sum=0
  rem=0
  product=n1*n2
  if(product > 500):
    print("product of ",n1," and ",n2," is greater than 500 ")
    print("Their product is : ",product)
    while(product>0):
      rem = product % 10
      sum=sum+rem
      product=product//10
    print("So, sum of their product is: ",sum)
  else:
    print("product is : ",product)

num1=int(input("enter number1: "))
num2=int(input("enter number2: "))
product_or_sum(num1,num2)
