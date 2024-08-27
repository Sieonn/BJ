from math import gcd

def solution(numer1, denom1, numer2, denom2):
    A = denom1 * numer2 + denom2 * numer1
    denom3 = denom1 * denom2
    frac_gcd = gcd(A, denom3) #최대공약수
    return [A//frac_gcd, denom3//frac_gcd] 
    