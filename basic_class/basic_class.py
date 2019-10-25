#!/usr/bin/python
# -*- coding: UTF-8 -*-


class basic_class:
    def __init__(self):
        pass

    def __repr__(self):
        class_name = self.__class__.__name__
        # class_attr = self.__dict__
        return class_name
