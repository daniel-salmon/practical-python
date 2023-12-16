# foo.py

x = 42
def bar():
    pass
def spam():
    pass

class B:
    def __init__(self):
        print('b')

class C:
    def __init__(self):
        print('c')

class A(B, C):
    def __init__(self):
        super().__init__()
        print('a')


class Loud:
    def noise(self):
        return super().noise().upper()


class Dog:
    def noise(self):
        return 'Bark'

    def chase(self):
        return 'Chasing!'


class LoudDog(Loud, Dog):
    pass


class Bike:
    def noise(self):
        return 'On Your Left'

    def pedal(self):
        return 'Pedaling!'


class LoudBike(Loud, Bike):
    pass


def countdown(n):
    while n > 0:
        yield n
        n -= 1

def filematch(filename, substr):
    with open(filename, 'r') as f:
        for line in f:
            if substr in line:
                yield line

if __name__ == '__main__':
    c = countdown(10)
    while True:
        try:
            x = c.__next__()
            print(x)
        except StopIteration as e:
            print('all done')
            break
    print("i'm out of there")
