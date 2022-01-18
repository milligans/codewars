def symmetric_point(p, q):
    print(p, q)
    grad= (q[1] - p[1])/(q[0]-p[0])
    print(grad)
    a = q[0] * grad
    b =q[1] * grad

    return [a, b]