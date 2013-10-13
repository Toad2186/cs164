# Test using typing for a general class.
class TestClass:
    def hello(self::TestClass):
        return True

a = TestClass()
b = a.hello()