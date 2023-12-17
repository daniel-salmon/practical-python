# timethis.py

def timethis(func):
    def wrapped(*args, **kwargs):
        import time
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
    return wrapped
