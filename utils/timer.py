from timeit import default_timer as timer


def function_timer(func):
    def wrap(*args, **kwargs):
        start = timer()
        result = func(*args, **kwargs)
        end = timer()
        print(f'{func.__name__} took {end-start} seconds to complete')
        return result
    return wrap
