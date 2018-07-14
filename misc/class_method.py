class A:
    var = None

    @staticmethod
    def static_method():
        print "In static "

    @classmethod
    def test(cls):
        print "In classmethod "
        cls.var = 1
        print cls.var

    def temp(self):
        print "In temp"
        print self.var

if __name__ == "__main__":
    A.test()
    a = A()
    a.temp()
