def divide_by(a,b):
    return a/b


try:
    print(divide_by(1/0))
except ZeroDivisionError as e:
    print(e)
    print(e.__class__)