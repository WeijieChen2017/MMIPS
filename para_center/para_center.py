#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import datetime
import numpy as np
from basic_class.basic_class import basic_class


class para_center(basic_class):
    def __init__(self):
        super().__init__()
        self.center = {}

    def pc_set(self, key, value):
        self.center[key] = value

    def pc_get(self, key):
        assert key in self.center, "There is no such para in the para_center"
        return self.center[key]

    def pc_save(self, path, tag='para_center'):
        time_stamp = datetime.datetime.now().strftime("-%Y-%m-%d-%H-%M")
        name = os.path.join(path, time_stamp+'_'+tag+'.npy')
        np.save(name, self.center)
        print('Saved in '+name)
