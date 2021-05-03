def b(func):
    return func ** 2
@b
def a(x): print(x)

c = b(a(10))







