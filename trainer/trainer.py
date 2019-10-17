#!/usr/bin/python
# -*- coding: UTF-8 -*-

from basic_class.basic_class import basic_class


class trainer(basic_class):
    def __init__(self, conf_file):
        super().__init__()
        self.conf_file = conf_file

    def train_exp(self):
        pass
