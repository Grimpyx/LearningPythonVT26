def logmap(r,x): return r*x*(1-x)

# Generator versions of the previous assignment (labeled 4.1)
# Basically it allows us to not specify a limit, similar to
# enumerables in C#.
def experiment(r,x):
    x0 = x
    while True:
        yield x0
        x_next = logmap(r,x0)
        x0 = x_next

def table(r,x0,y0):
    x_generator = experiment(r,x0)
    y_generator = experiment(r,y0)
    p0 = (next(x_generator),next(y_generator)) # Tuple

    while True:
        yield p0
        x_next = next(x_generator)
        y_next = next(y_generator)
        p_next = (x_next, y_next)
        p0 = p_next

# Check to see if it runs as expected
def RunTest():
    exp = experiment(3.9, 0.2)
    print(next(exp))
    print(next(exp))
    print(next(exp))
    table = table(3.9, 0.2, 0.2001)
    print(next(table))
    print(next(table))
    print(next(table))
RunTest()