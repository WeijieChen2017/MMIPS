#!/usr/bin/python
# -*- coding: UTF-8 -*-

from basic_class.basic_class import basic_class


class messager_supervisor(basic_class):
    def __init__(self, mesg_conf):
        super().__init__()
        self.mesg_conf = mesg_conf

    def excute(self):
        pass