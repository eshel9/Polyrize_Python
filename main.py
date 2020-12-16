from magic_list import MagicList


def main():
    # NOTE: with extra time, use unittests instead
    a = MagicList()
    # should work
    a[0] = 1
    print(a)
    a[1] = 2
    print(a)
    a[1] = 3
    print(a)
    a[-1] = 4   # should update last element
    print(a)

    # shouldn't work
    a[3] = 5
    print(a)


if __name__ == '__main__':
    main()
