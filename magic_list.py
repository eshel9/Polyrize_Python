from typing import TypeVar


class MagicList(list):
    def __init__(self, cls_type: TypeVar = None):
        self.cls_type = cls_type

    def __setitem__(self, key, value):
        current_length = self.__len__()
        if current_length == key:
            self.append(value)
        elif 0 < key < current_length:
            super().__setitem__(key, value)
        else:
            raise IndexError("list index out of extended range")