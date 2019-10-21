#!/usr/bin/python
# -*- coding: UTF-8 -*-

from basic_class.basic_class import basic_class


class predictor_supervisor(basic_class):
    def __init__(self, pred_conf):
        super().__init__()
        self.pred_conf = pred_conf

    def predict_on_data(self):
        pass
