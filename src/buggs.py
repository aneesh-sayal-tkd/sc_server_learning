def buggy_function():
    unused_var = 42  # unused variable (code smell)

    if True == True:  # redundant condition
        print("Always true!")

    print("Code smells are cool!")

buggy_function()
