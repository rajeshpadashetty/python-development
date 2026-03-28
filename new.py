class A(Exception):
    pass
class B(A):
    pass
class C(B):
    pass

for i in [A, B, C]:
    try:
        raise i()
    except C:
        print("c exception")
    except B:
        print("b exception")
    except A:
        print("a exception")
