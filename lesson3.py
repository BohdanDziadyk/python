list_1 = [i for i in range(10)]


# def list_printer(lst):
#     print(lst)
#
#
# list_printer(list_1)
def minimal(a, b, c):
    if a < b and a < c:
        print(a)
        minim = a
    elif b < a and b < c:
        print(b)
        minim = b
    else:
        print(c)
        minim = c
    return minim
