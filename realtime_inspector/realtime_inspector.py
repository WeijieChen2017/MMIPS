#!/usr/bin/python
# -*- coding: UTF-8 -*-

from basic_class.basic_class import basic_class


class realtime_inspector(basic_class):
    def __init__(self):
        super().__init__()

    def log_this(self, *message, new_line=True):
        for sub_mesg in message:
            print(sub_mesg, end='')

        if new_line:
            print("")

    def add_break(self, n_row, n_col=72, char="%"):
        for idx_row in range(n_row):
            for idx_col in range(n_col):
                self.log_this(char, new_line=False)
            self.log_this("")
