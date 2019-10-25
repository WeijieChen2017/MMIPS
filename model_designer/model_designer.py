#!/usr/bin/python
# -*- coding: UTF-8 -*-

from basic_class.basic_class import basic_class

class model_designer(basic_class):
    def __init__(self, model_conf):
        super().__init__()
        self.conf_file = model_conf

    def design_model(self):
        model_type = self.conf_file['model_type']
        assert model_type is not None, "Model type is not specified."
        module = globals()[model_type](self.conf_file)
        func = getattr(module, 'output_model')
        return func()
