#!/usr/bin/python
# -*- coding: UTF-8 -*-

from basic_class.basic_class import basic_class


class data_designer(basic_class):
    def __init__(self, conf_file, aug_file):
        super().__init__()
        self.conf_file = conf_file
        self.aug_file = aug_file

    def prepare_data(self):
        pass

    def augment_data(self):
        pass

    def design_data_generator(self):
        pass