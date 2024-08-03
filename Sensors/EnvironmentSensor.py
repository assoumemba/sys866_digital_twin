from utils import *
from Sensors.BaseSensor import BaseSensor
import pathlib
import sys

import numpy as np
import pandas as pd


class EnvironmentSensor(BaseSensor):

    def __init__(self, data_path, col_name = 'tmean'):
        super().__init__(data_path, col_name)

        #tmean,prpc

    def load_data(self):

        df = pd.read_csv(self.data_path)
        df['date'] = pd.to_datetime(df["date"])
        
        df = df.sort_values(by='date')
        self.sensor_data = df.set_index('date')
        self.sensor_dates = np.array(df['date'].drop_duplicates())