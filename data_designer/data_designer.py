#!/usr/bin/python
# -*- coding: UTF-8 -*-

from basic_class.basic_class import basic_class
from data_designer.operation import operation_interpreter
# from tool_hub.data_reshaper import data_reshaper
from realtime_inspector.realtime_inspector import realtime_inspector

import glob
import numpy as np
import nibabel as nib


class data_designer(basic_class):
    def __init__(self, data_conf):
        super().__init__()
        self.data_conf = data_conf
        self.data_log = {}
        self.logger = realtime_inspector()

    def prepare_data(self):
        input_list = glob.glob(self.data_conf["input_path"])

        if self.data_conf["data_storage"] == "memory":
            return_data = []

        for input_path in input_list:
            self.logger.log_this("Loading: ", input_path)
            input_file = nib.load(input_path)
            input_data = input_file.get_fdata()

            # save basic info of data
            temp_log = {"max": np.amax(input_data),
                        "min": np.amin(input_data),
                        "mean": np.mean(input_data),
                        "std": np.std(input_data),
                        "p99": np.percentile(input_data, 99),
                        "p99.9": np.percentile(input_data, 99.9),
                        "p99.99": np.percentile(input_data, 99.99),
                        "data_shape": input_data.shape,
                        "hist": np.histogram(np.ravel(input_data), bins=64),
                        "affine": input_file.affine,
                        "header": input_file.header}
            self.data_log[input_path] = temp_log

            # before augmentation
            if self.data_conf["pre_aug"]:
                pre_aug_conf = self.data_conf["pre_aug_conf"]
                if len(input_data.shape) == 3:
                    temp_data = input_data[np.newaxis, :, :, :]
                else:
                    temp_data = input_data

                self.logger.log_this("Processing before augmentation:")
                for op_dict in pre_aug_conf:

                    # plugin some required info (such as affine/header of nib_smooth)
                    others_hub = []
                    for op in op_dict["method"]:
                        others = {}
                        for other in op["others"]:
                            others[other] = temp_log[other]
                        others_hub.append(others)

                    operation = operation_interpreter(op_conf=op_dict, others_hub=others_hub)
                    temp_data = operation.apply(temp_data)
                    self.logger.log_this(op_dict)
                    self.logger.log_this("output_data_shape", temp_data.shape)
                input_data = temp_data

                self.logger.add_break(n_row=1)
            else:
                pass


            # augmentation
            if self.data_conf["augmentation"]:
                pass
            else:
                pass


            # after augmentation
            if self.data_conf["post_aug"]:
                pass
            else:
                pass


            # return memory-stored data or not
            if self.data_conf["data_storage"] == "memory":
                return_data.extend(input_data)

        if self.data_conf["data_storage"] == "memory":
            return np.asarray(return_data)

    def augment_data(self):
        pass

    def design_data_generator(self):
        pass
