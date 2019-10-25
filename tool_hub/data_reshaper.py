#!/usr/bin/python
# -*- coding: UTF-8 -*-

from basic_class.basic_class import basic_class

class data_reshaper(basic_class):
    def __init__(self, shape_info):
        super().__init__()
        self.shape_info = shape_info

    def apply(self, input_data):
        pass
