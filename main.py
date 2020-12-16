from magic_list import MagicList
from dataclasses import dataclass


@dataclass
class Person:
    age: int = 1


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

    b = MagicList(cls_type=Person)
    b[0].age = 5
    print(b)

    # shouldn't work
    b[2].age = 5
    print(b)
    a[3] = 6
    print(a)


if __name__ == '__main__':
    main()
