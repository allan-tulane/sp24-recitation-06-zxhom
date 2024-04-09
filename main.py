def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """
    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        counts[n] += 1  # adding index (nth fib num) to array w intermediate results
        return fib_recursive(n - 1, counts) + fib_recursive(n - 2, counts)

# Issue with counts and fib, has 2 extra indices (maybe from final recursive call, unecessary 2 indexes created??)

def fib_top_down(n, fibs):
    if fibs[n] != -1:
        return fibs[n]

    elif n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        fibs[n] += 1
        fibs[n] = fib_top_down(n - 1, fibs) + fib_top_down(n - 2, fibs)
        return fibs[n]


def fib_bottom_up(n):
    mem = [-1] * (n + 1)

    for i in range(n+1):
        if mem[0] == -1:
            mem[0] = 0
        elif mem[1] == -1:
            mem[1] = 1
        else:
            mem[i] = mem[i-1] + mem[i-2]
    #print(mem)       
    return mem[n]

#print(fib_bottom_up(5))
#fib_bottom_up(5)

def fib_bottom_up_better(n):
    ###TODO
    pass
