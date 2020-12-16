from typing import TypeVar


class MagicList(list):
    def __init__(self, cls_type: TypeVar = None):
        self.cls_type = cls_type

    def __