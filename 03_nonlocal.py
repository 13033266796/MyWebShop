
def func1():
    a = 10

    def func2():
        a = 20
        def func3():
            nonlocal a
            a = 30
            print("func3*********",a)
        func3()

        print("func2***********",a)
    func2()
    print("func1*************", a)

func1()