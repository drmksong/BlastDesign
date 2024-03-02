# disregard this file, it is for testing purposes only

class Test:
    def __init__(self):
        self.__x = 1
        self.y = 2

    def __def(self):
        print("test")

    def test(self):
        print(self.__x)
        self.__def()

if __name__ == "__main__":
    t = Test()
    t.test()
    print(t.y)
    print(t.__x)
    t.__def()