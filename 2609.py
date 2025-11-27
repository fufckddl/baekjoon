from math import gcd


a,b= list(map(int, input().split()))
lcm = a * b / gcd(a,b)
r = 1
while a % b != 0:
    r = a % b
    a = b
    b = r

print(b)
print(int(lcm))
    