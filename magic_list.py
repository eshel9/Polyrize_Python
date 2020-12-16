from typing import Any


class MagicList(list):
    def __init__(self, cls_type: Any = None):
        self.cls_type = cls_type

    def __setitem__(self, key, value):
        current_length = self.__len__()
        if current_length == key:
            if self.cls_type is None:
                self.append(value)
        elif (-current_length - 1) < key < current_length:
            super().__setitem__(key, value)
        else:
            raise IndexError("list index out of extended range")

    def __getitem__(self, item):
        current_length = self.__len__()
        if current_length == item:
            if self.cls_type is not None:
                new_instance = self.cls_type()
                self.append(new_instance)
                return super().__getitem__(item)
            else:
                raise IndexError("range of MagicList is extended only when setting an item,"
                                 " or when getting an item if the cls_type was given")
        elif (-current_length - 1) < item < current_length:
            return super().__getitem__(item)
        else:
            raise IndexError("list index out of extended range")

