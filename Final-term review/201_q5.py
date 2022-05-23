# Coroutine programming

def printOdd():
    yield 1
    yield 3
    yield 5

if __name__ == '__main__':
    n = 0
    for i in printOdd():
        print(i)
        n += 2
        print(n)