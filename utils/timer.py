from timeit import default_timer as timer


def function_timer(func):
    def wrap(*args, **kwargs):
        start = timer()
        result = func(*args, **kwargs)
        end = timer()
        print(f'{func.__name__} took {end-start} seconds to complete.')
        return result
    return wrap


def function_timer_avg(func):
    def wrap(*args, **kwargs):
        time_taken = 0
        for i in range(100):
            start = timer()
            result = func(*args, **kwargs)
            end = timer()
            time_taken += end-start
        print(f'{func.__name__} took {(time_taken) / 100} seconds to complete on average.')
        return result
    return wrap