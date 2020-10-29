##############################################################################
## 
## optimalCurve.sage
##
## This is an algorithm for deciding whether an elliptic curve, here given by 
## its points (a1,a2,a3,a4,a6), is optimal or not.
##
#############################################################################

def isOptimal(a1,a2,a3,a4,a6, p, q):
    b2 = a1^2+4*a2
    b4 = a1*a3+2*a4
    b6 = a3^2+4*a6
    b8 = a1^2*a6-a1*a3*a4+a2*a3^2+4*a2*a6-a4^2

    delta = -b2^2*b8-8*b4^3-27*b6^2+9*b2*b4*b6

    if(delta%p == 0):
        return false

    elif(order(EllipticCurve(GF(q), [a1,a2,a3,a4,a6])) == q+1+2*sqrt(q)):
        return true

p = int(input("Enter a prime number: "))
r = int(input("Enter extension you wish to calculate: "))

q = p^r

for a1 in range(q):
    for a2 in range(q):
        for a3 in range(q):
            for a4 in range(q):
                for a6 in range(q):
                    if(isOptimal(a1,a2,a3,a4,a6, p, q)):
                        print("Curve defined by ", [a1,a2,a3,a4,a6], "| Optimal")
                    else:
                        print("Curve defined by ", [a1,a2,a3,a4,a6] ,"| Not optimal")
