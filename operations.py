def division():
    print("This operation help you divide two numbers")
    x=float(input("Please enter a number : "))
    y=float(input("Please enter a number : "))
    if y!=0:
        c=x/y
        print(f"The result of division is {c}")
    else:
        print("Division by cero does'nt exists")
division()