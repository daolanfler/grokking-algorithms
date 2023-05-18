def g(x):
    breakpoint()
    return x * x


def f(x):
    list = []
    for i in range(x):
        list.append(g(i))
    return list


list = f(3)
print(list)
