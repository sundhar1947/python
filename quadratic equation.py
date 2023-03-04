import math


a=int(input("enter a :"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if a==0:
    print("enter the coeff :")
else:
    disc=b*b-4*a*c
    sqrt_val=math.sqrt(abs(disc))
if disc>0:
    print("real and different roots")
    print((-b+sqrt_val)/(2*a))
    print((-b-sqrt_val)/(2*a))
elif disc==0:
    print("real and same roots:")
    print(-b/(2*a))
else:
    print("complex roots exits:")
    print(-b/(2*a),"+i",sqrt_val)
    print(-b/(2*a),"-i",sqrt_val)
