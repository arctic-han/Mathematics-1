# Here is an algorithm for finding optimal elliptic curves, suitable for cryptogtraphy. It's only input is just any
# prime power q=p^r. 
# We range p over primes and r over any integer. We wish to compute for p some 100 digit prime, and also for 
# p=2,3,5,7,9 and thier close powers. Since the algotrithm grows fast in complexity (check by how much once algorithm 
# is finished, we have at least O(p^5)), it is advised not to input very large q, other than the 100 digit prime.

# from __future__ import print_function # Just import some of the print function's properties
                                        # to make output bearable.

##p = 2; r = 1
##q = p^r
##
##for a1 in range(q):
##    for a2 in range(q):
##        for a3 in range(q):
##            for a4 in range(q):
##                for a6 in range(q):
##                    b2=a1^2+4*a2; b4=a1*a3+2*a4; b6=a3^2+4*a6; b8=a1^2*a6-a1*a3*a4+a2*a3^2+4*a2*a6-a4^2
##                    
##                    delta=-b2^2*b8-8*b4^3-27*b6^2+9*b2*b4*b6
##                    if delta % p == 0:
##                        print("\n")
##                    else:
##                        E = EllipticCurve(GF(q),[a1,a2,a3,a4,a6])
##                        print(E, end="\n\n")
##                        
##                        # if order(E) == q+1+2*sqrt(q):
##                           # print("Optimal curve") ## Our curves would need to be evaluated at rational points, 
##                                                    #read documentation on how to count rational points on the curves.

################################## END NOTE ##################################

# Do not run this code on idle, it is SAGE code, not Python 3 code.

################################## END NOTE ##################################
