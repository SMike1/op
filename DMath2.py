import math


def perVirag(k, b,z,x ):
    d = (1-0.5*k)/b*math.sqrt(math.fabs(z))
    q = math.log(k)*x
    r = 0.025*math.log(b, 5)*math.pow(k,3)
    a = q + d - r
    return a


def cVirag(z, k, x):
    q = (math.pow(math.sin(z),2) + math.cos(math.pow(k,2)) * x) * 8
    r = math.exp((k * x +2.5))
    c = q + r
    return c

print(cVirag(0, 0, 2))
print(perVirag(1, 0.5, 1, 0))


