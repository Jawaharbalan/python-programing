import sys
try:
    a=int(input("input:"))

except ValueError:
    print ("Error..numbers only")
    sys.exit()
if(a%2==0):
    print("even")
else:
    print("odd")
