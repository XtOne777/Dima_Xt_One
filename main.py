from random import randint


def main():
    a = [randint(1, 100) for _ in range(100)]
    print(a)
    for i in range(len(a) - 1):
        for k in range(len(a) - 1 - i):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]
    print(a)


if __name__ == "__main__":
    main()
