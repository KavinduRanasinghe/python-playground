items = [1,2,3,4,5]

try:
    item = items[6]
except Exception as e:
    print(e)



def divide(a,b):
    return a/b


try:
    ans = divide(10,0)
    print(ans)

except Exception as e:
    print(e)


try:
    with open('file.txt',r) as file:
        print(file.read())

except Exception as e:
    print(e , " Unable to locate the file", sep=" - ")

