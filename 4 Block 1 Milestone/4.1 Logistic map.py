def logmap(r,x): return r*x*(1-x)

def experiment(r,x,n):
    print(x)
    for i in range(1,n):
        x = logmap(r,x)
        print(x)

def table(r,x1,x2,n):
    print(x1,x2)
    for i in range(1,n):
        x1 = logmap(r,x1)
        x2 = logmap(r,x2)
        print(x1,x2)

table(3.9,0.20,0.21,10)