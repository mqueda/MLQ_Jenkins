def New_Function():
    print("Hello World!!!")
    print("Second Commit!!!")
    print("Third Commit!!!")

def inc(x):
    return x + 1

def test_answer():
    #assert inc(3) == 4
    assert inc(3) == 5

def main ():
    New_Function()

main()
test_answer()