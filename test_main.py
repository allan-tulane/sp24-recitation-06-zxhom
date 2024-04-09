from main import *

def test_fib_recursive():
    n = 10
    counts = [0] * (n+1)
    assert fib_recursive(n, counts) == 55
    print(counts)
    print(sum(counts))

test_fib_recursive()

def test_fib_top_down():
    n = 10
    fibs = [-1] * (n+1)
    assert fib_top_down(n, fibs) == 55
    print(fibs)

#test_fib_top_down()

def test_fib_bottom_up():
    n = 10
    #print(fib_bottom_up(n))
    assert fib_bottom_up(n) == 55
    

#test_fib_bottom_up()
