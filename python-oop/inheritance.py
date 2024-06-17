# class A:
#     a=1
# class B():
#     b=2

# class C(A,B):
#     pass

# c=C()
# print(c.a,c.b)
    

class A:
    a=1
class B(A):
    b=2

class C(B):
    pass

c=C()

print(c.a,c.b)

print(issubclass(A,B))
print(issubclass(B,A))