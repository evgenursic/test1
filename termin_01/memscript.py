def my_func():
    a = [1] * 100000
    b = [2] * 90000
    del b
    return a
