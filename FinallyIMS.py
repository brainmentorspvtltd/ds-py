def func():
    try:
        l = [1,2,3,4]
        i = int(input("Enter the index"))
        print(l[i])
        return 1
    except:
        print("Some error occur")
        return 0
    finally:
        print("Hlo i'm calc..")

x = func()
print(x)
