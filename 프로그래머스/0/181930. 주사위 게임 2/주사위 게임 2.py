def solution(a, b, c):
    if [a,b,c].count(a) == 3:
        return 3*a*3*(a**2)*3*(a**3)
    elif a!= b and b != c and c!=a:
        return a+b+c
    else:
         return (a+b+c)*(a**2+b**2+c**2)
        
        