def printf(value='', *formats):
    print(value % formats, end='')


def scanf(value, num: int=None):
    if num is None:
        return input(value).split()
    else:
        inf = input(value).split()
        if len(inf) == num:
            return inf
        raise ValueError('num not')
