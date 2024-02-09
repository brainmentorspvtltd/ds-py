try:
    num_1 = int(input("Enter the first value.."))
    num_2 = int(input("Enter the second value.."))

    add = num_1 + num_2
    
    sub = num_1 - num_2
    
    mul = num_1 * num_2   

    div = num_1 / num_2
    
except ZeroDivisionError as msg:
    print(msg)

except ValueError as msg:
    print(msg)

else:
    print("Add is",add)
    print("Sub is",sub)
    print("Mul is",mul)
    print("Div is",div)
    
finally:
    print("hlo i'm calc")
    

    
