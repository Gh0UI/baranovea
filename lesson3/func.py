import math
 
print("ax\u00b2 + bx + c = 0")
a = int(input("коэффицент a: "))
b = int(input("коэффицент b: "))
c = int(input("коэффицент c: "))
 
discr = b **2-4*a*c
print("Дискриминант: ", discr)
 
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 =",x1, '\nx2 =',x2)
elif discr == 0:
    x = -b / (2 * a)
    print("x =", x)
else:
   real=-b / (2 * a)
   imag=math.sqrt(-discr)/ (2 * a)
   res=complex(real,imag)
   print ('x1=',res,'\nx2=',res.conjugate())