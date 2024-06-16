def sum_of(**kwargs):
    sum=0
    for ky,value in kwargs.items():
        sum+=value
        print(ky)
    return sum

print(sum_of(x=1,y=2,z=3))