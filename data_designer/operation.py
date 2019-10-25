#!/usr/bin/python
# -*- coding: UTF-8 -*-

from basic_class.basic_class import basic_class

import nibabel as nib
import numpy as np


class basic_operator(basic_class):
    def __init__(self, para_hub):
        super().__init__()
        self.para_hub = para_hub

    def process(self, input_data, para=None, others=None):
        pass

    def data_reshape(self, input_data):
        return input_data

    def excute(self, input_data, others=None):
        return_data = []
        input_data = self.data_reshape(input_data)
        for para in self.para_hub:
            return_data.extend(self.process(input_data, para=para, others=others))
        return return_data

class nib_smooth(basic_operator):
    def __init__(self, para_hub):
        super().__init__(para_hub=para_hub)

    def process(self, input_data, para=None, others=None):

        # special usage for [6, 256, 256, 80]-like data
        if len(input_data.shape) == 4:
            return_data = []
            for idx in range(input_data.shape[0]):
                temp_data = input_data[idx, :, :, :]
                temp_nii = nib.Nifti1Image(temp_data, others["affine"], others["header"])
                return_data.append(nib.processing.smooth_image(temp_nii, fwhm=para, mode='nearest').get_fdata())

        else:
            temp_nii = nib.Nifti1Image(input_data, others["affine"], others["header"])
            return_data = nib.processing.smooth_image(temp_nii, fwhm=para, mode='nearest').get_fdata()

        return return_data

class gaussian_noise(basic_operator):
    def __init__(self, para_hub):
        super().__init__(para_hub=para_hub)

    def process(self, input_data, para=None, others=None):
        noise = np.random.normal(loc=0, scale=np.std(input_data)*para, size=input_data.shape)
        return input_data+noise

class poisson_noise(basic_operator):
    def __init__(self, para_hub):
        super().__init__(para_hub=para_hub)

    def process(self, input_data, para=None, others=None):
        noise = np.random.poisson(size=input_data.shape, lam=np.mean(input_data*para))
        return input_data+noise




class operation_interpreter(basic_class):
    def __init__(self, op_conf, others_hub):
        super().__init__()
        self.op_conf = op_conf
        self.others_hub = others_hub

    def apply(self, input_data):

        return_data = []
        # only one operator
        if self.op_conf["n_method"] == 1:
            opeartor = globals()[self.op_conf["method"][0]["name"]](self.op_conf["method"][0]["para"])
            return_data = opeartor.excute(input_data, others=self.others_hub[0])
        else:
            operator_hub = []
            for method in self.op_conf["method"]:
                opeartor = globals()[method["name"]](method["para"])
                operator_hub.append(opeartor)

            if self.op_conf["method_relation"] == "parallel":
                for idx, opeartor in enumerate(operator_hub):
                    return_data.extend(opeartor.excute(input_data, others=self.others_hub[idx]))

        return np.asarray(return_data)


