for i in range(100):
    if i % 3 == 0 or i % 5 == 0:
        if i % 15 == 0: print("FooBar")
        else:
            if i % 3 == 0: print("Foo") 
            else:
                print("Bar") 
    else:
        print(i)