from typing import TypeVar


class MagicList(list):
    def __init__(self, cls_type: TypeVar = None):
        self.cls_type = cls_type

    def __setitem__(self, key, value):
        if self.__len__() == key:
            self.__add__([value])

        super().__setitem__(key, value)