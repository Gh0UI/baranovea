import math

def func1(a,b,c):
    print("ax\u00b2 + bx + c = 0")
    """Квадратное уравнение, возвращает корни"""

    
    discr = b**2 - 4*a*c
    """Дискриминант"""
    
    if discr > 0:
        """Дискриминант больше 0, возвращает 2 корня"""
        x1 = (-b + math.sqrt(discr)) / (2*a)
        x2 = (-b - math.sqrt(discr)) / (2*a)
        print("x1 =",x1, '\nx2 =',x2)
        return x1, x2

    elif discr == 0:
        """Дискриминант равен 0, возвроащает 1 корень"""
        x = -b / (2*a)
        print("x =", x)
        return x
    else:
        """Дискриминант меньше 0, возвращает 2 корня с мнимой частью""" 
        real=-b / (2*a)
        imag=math.sqrt(-discr) / (2*a)
        res=complex(real,imag)
        print ('x1=',res,'\nx2=',res.conjugate())
        return res, res.conjugate()
    

