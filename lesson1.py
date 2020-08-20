list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
i = 1
while i > 0:
    print(list)
    print("1) min of list")
    print("2) delete similar")
    print("3) replace every 4th by X")
    print("4) print closest number to lists avg")
    print("5) print square with custom side")
    print("6) print tablichky umnozhenia")
    print("type 0 to end")
    inp = int(input("Choose an option:"))
    if inp == 1:
        l1 = list.copy()
        l1.sort()
        res = l1[0]
        print("-------------------------------------------------------------------")
        print(res)
        print("-------------------------------------------------------------------")
    elif inp == 2:
        l2 = list.copy()
        l2.sort()
        for item in l2:
            count1 = l2.count(item)
            if count1 > 1:
                l2.remove(item)
        print("-------------------------------------------------------------------")
        print(l2)
        print("-------------------------------------------------------------------")
    elif inp == 3:
        l3 = list.copy()
        lenght = len(l3)
        i = 3
        while i < lenght:
            l3[i] = 'X'
            i += 4
        print("-------------------------------------------------------------------")
        print(l3)
        print("-------------------------------------------------------------------")
    elif inp == 4:
        l4 = list.copy()
        lenght1 = len(l4)
        res1 = 0
        for item in l4:
            res1 += item
        res2 = res1 // lenght1
        res3 = round(res2)
        for item in l4:
            if item == res3:
                print("-------------------------------------------------------------------")
                print(item)
                print("-------------------------------------------------------------------")
                break
    elif inp == 5:
        inp1 = int(input("Enter square side:"))
        x = 0
        print("-------------------------------------------------------------------")
        while x < inp1:
            print("*", end="")
            x += 1
        print("")
        x = 0
        while x < inp1 - 2:
            print("*", end="")
            y = 0
            while y < inp1 - 2:
                print(" ", end="")
                y += 1
            print("*")
            x += 1
        x = 0
        while x < inp1:
            print("*", end="")
            x += 1
        print("")
        print("-------------------------------------------------------------------")
    elif inp == 6:
        x = 1
        y = 1
        while x < 10:
            while y < 10:
                print(x * y, end="")
                print(" ", end="")
                y += 1
            print("")
            y = 1
            x += 1
        print("")
    elif inp == 0:
        break
