import random
import math
def inisialisasiya():
    T = 1000
    alpha = 0.9
    awalX1 = acak()
    awalX2 = acak()
    return T,alpha,awalX1,awalX2
def acak():
    angka=random.uniform(-10 , 10)
    return angka
def acakR():
    R = random.uniform(0,1)
    return R
def y(x1,x2):
    sx= math.sin(x1)
    cx=math.cos(x2)
    kuadrat=math.sqrt(x1*x1 + x2*x2)
    a =kuadrat/math.pi
    p = 1- a
    c= abs(p)
    ex=math.exp(c)
    o = sx*cx*ex
    mutlak=abs(o)
    return -1*mutlak
def putarDalamPutar(BSF,loop2,Temp):
    while loop2 < 100000:
        acax1 = acak()
        acax2 = acak()
        NS = y(acax1, acax2)
        deltaE = NS - BSF
        if deltaE < 0:
            BSF = NS
        else:
            rR = acakR()
            q = -1 * deltaE
            pP = math.exp(q / Temp)
            if pP > rR:
                BSF = NS
        loop2 = loop2 + 10
    return BSF,acax1,acax2
def putar2(T,BSF,alpha):
    while T > 0.1:
        loop2 = 1
        CS,jx1,jx2 = putarDalamPutar(BSF,loop2,T)
        T = T * alpha
    return CS,jx1,jx2
def output(jawaban,ex1,ex2):
    print('==========================================================')
    print('Nilai Minimum Fungsi Tersebut : ', jawaban)
    print('Dengan nilai x1               : ', ex1)
    print('Dengan nilai x2               : ', ex2)
    print('==========================================================')
t,alpha,awx1,awx2=inisialisasiya();
BFS = y(awx1,awx2)
BFS,x1,x2 = putar2(t,BFS,alpha)
output(BFS,x1,x2)










