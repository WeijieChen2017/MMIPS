#!/usr/bin/python
# -*- coding: UTF-8 -*-

from basic_class.basic_class import basic_class


class data_designer(basic_class):
    def __init__(self, data_conf, aug_conf):
        super().__init__()
        self.data_conf = data_conf
        self.aug_conf = aug_conf

    def prepare_data(self):
        pass

    def augment_data(self):
        pass

    def design_data_generator(self):
        pass