def add_length(str_):
    list = str_.split()
    res = []
    for el in list:
        res.append('{} {}'.format(el, len(el)))
    return res;


print(add_length("apple ban"))