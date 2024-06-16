set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)

def aa(some):
   return

print(aa("w"))

numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(filter(lesser, numbers))
print(small)