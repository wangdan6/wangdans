def a(f):
    def b():
        def c():
            print("4")
            f()
            print(5)
        return c()
    return b()
def test_case01():
    print("3")
a(test_case01)



 
