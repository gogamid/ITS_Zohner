def mod_inv(n, a):
    b,a1 = 1,0
    u,v = 0,1
    while a != 0:
        z1,z2,z3 = a, u, v
        q = n/a
        u = b-q*u
        v = a1 - q*v
        