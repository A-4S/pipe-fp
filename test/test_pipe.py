from pipepy import pipe


def test_pipe():
    def add_1(x: int):
        return x + 1
    
    def mult_2(x: int):
        return x * 2
    
    def minus_3(x: int):
        return x - 3
    
    assert pipe(add_1, mult_2, minus_3)(3) == 5
    assert pipe(mult_2, mult_2, mult_2)(1) == 8
