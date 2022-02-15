# fibonacci function
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)


# tests
def test_fib_of_negative_one():
    assert fib(-1) == -1


def test_fib_of_zero():
    assert fib(0) == 0


def test_fib_of_one():
    assert fib(1) == 1


def test_fib_of_10():
    assert fib(10) == 55


def test_fib_of_twenty():
    assert fib(20) == 6765
