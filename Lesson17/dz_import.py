def func(a):
    b = set(a)
    if len(a)==len(b):
        return 'уникальны'
    else:
        return 'не уникальны'