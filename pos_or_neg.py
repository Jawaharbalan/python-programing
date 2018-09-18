import sys
try:
    a=int(input("input:"))

except ValueError:
    print ("Error..numbers only")
    sys.exit()
if(a>0):
    print("output:positive")
elif(a<0):
    print("output:negative")
else:
    print("output:zero")
