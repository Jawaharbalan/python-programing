n=int(input("enter n:"))
rev=0
while(n>0):
    Rem=n%10
    rev= (rev*10)+Rem
    n=n//10
print(rev)
