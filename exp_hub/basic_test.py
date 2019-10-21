#!/usr/bin/python
# -*- coding: UTF-8 -*-

from basic_class.basic_class import basic_class
from para_center.para_center import para_center

from data_designer.data_designer import data_designer
from model_designer.model_designer import model_designer
from trainer.trainer import trainer_supervisor
from predictor.predictor import predictor_supervisor
from messager.messager import messager_supervisor

class experiment(basic_class):
    def __init__(self):
        super().__init__()

        self.model_conf = {"model_type": "unet",
                           "image_shape": (256, 256, 1),
                           "out_ch": 1,
                           "start_ch": 64,
                           "depth": 4,
                           "inc_rate": 2,
                           "activation": "relu",
                           "dropout": 0.5,
                           "batchnorm": True,
                           "maxpool": True,
                           "upconv": True,
                           "residual": True}

        self.data_conf = {}

        self.aug_conf = {}

        self.train_conf = {}

        self.pred_conf = {}

        self.mesg_conf = {}

    def start_experiment(self):
        data = data_designer(self.data_conf, self.aug_conf)
        model = model_designer(self.model_conf)
        trainer = trainer_supervisor(self.train_conf, model)
        trained_model = trainer.excute(data)
        predictor = predictor_supervisor(self.pred_conf)
        predictor.excute(trained_model)
        messager = messager_supervisor(self.mesg_conf)
        messager.excute()
