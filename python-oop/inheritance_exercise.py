# Example 1
class A:
   def a(self):
       return "Function inside A"

class B:
    def a(self):
        return "Function inside B"

class C(B,A):#left to right
    pass

# Driver code
c = C()
print(c.a())

class A:
    def b(self):
        return "Function inside A"

class B:
    def b(self):
        return "Function inside B"

class C(A, B):
    
    pass

class D(C):
    pass

d = D()
print(d.b())