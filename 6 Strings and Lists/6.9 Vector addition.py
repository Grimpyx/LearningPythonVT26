#def add_vectors(a, b):return (a[0] + b[0], a[1] + b[1])

# With pattern matching
def add_vectors(a, b):
    (ax,ay) = a
    (bx,by) = b
    return (ax+bx, ay+by)