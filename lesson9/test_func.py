import func, fib



class Test:
    def test_1_3_minus4(self):
        assert func.func1(1,3,-4)== (1.0, -4.0)

    def test_1_minus4_4(self):
        assert func.func1(1,-4, 4)== 2.0

    def test_1_4_minus29(self):
        assert func.func1(1,4, 29)== ((-2+5j), (-2-5j)) 

class Testfib:
    def test_8(self):
        assert fib.fibonacci(8)== 21

    def test_1(self):
        assert fib.fibonacci(1)== 1

    def test_munus1(self):
        assert fib.fibonacci(-1)== 'error'