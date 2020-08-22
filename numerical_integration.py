from math import sqrt, cos, pi


def simpsons_rule(f, a, b, n):
    dx = (b - a)/n
    # print('dx:', dx)
    x = [i * dx + a for i in range(n + 1)]
    # print('x:', x)

    # for i in x:
    #     print('f(x[i]):', f(i))

    s = 0
    for i in range(len(x)):
        if i == 0 or i == len(x) - 1:
            # print(i, 'First or Last')
            s += f(x[i])
        elif i % 2 == 1:
            # print(i, 'i % 2 == 1')
            s += 4 * f(x[i])
        else:
            # print(i, 'else')
            s += 2 * f(x[i])

        # print('f(x[i]):', f(x[i]))
        # print('s:', s)

    s = s * (dx/3)
    return s


def f(x):
    return sqrt(1 + 4*x**2)


def g(x):
    return sqrt(1 + (1/x**4))


def main():
    L = simpsons_rule(g, 1, 2, 100)
    print(L)


if __name__ == '__main__':
    main()
