import os
from datetime import datetime

from mltu.configs import BaseModelConfigs


class ModelConfigs(BaseModelConfigs):
    def __init__(self):
        super().__init__()
        self.model_path = os.path.join("Model", datetime.strftime(datetime.now(), "%Y%m%d%H%M"))
        self.frame_length = 256
        self.frame_step = 160
        self.fft_length = 384

        self.vocab = "abcdefghijklmnopqrstuvwxyz'?! "
        self.input_shape = None
        self.max_text_length = None
        self.max_spectrogram_length = None

        self.batch_size = 10
        self.learning_rate = 0.0001
        self.train_epochs = 1000
        self.train_workers = 4
