from Sensors.BaseSensor import BaseSensor

import os.path
import pathlib
import sys


import numpy as np
import pandas as pd


class CanopyCoverSensor(BaseSensor):
    def __init__(self, data_path):
        self.data_path = data_path
        self.sensor_dates = None

        #validate data exists
        data_file = pathlib.Path(self.data_path)
        if not data_file.exists():
            print('Please make sure to prepare data before running this script...')
            sys.exit()

        self.sensor_data = None

    def load_data(self):

        df = pd.read_csv(self.data_path)
        df['date'] = pd.to_datetime(df["date"])
        
        df = df.sort_values(by='date')
        self.sensor_data = df.set_index('date')
        self.sensor_dates = np.array(df['date'].drop_duplicates())

    def get_actual_cc_max(self, date):
        
        cc_val = self.sensor_data.at[date, 'mean']
        return np.max(cc_val)/100.0

    def get_actual_cc_min(self, date):
        
        cc_val = self.sensor_data.at[date, 'mean']
        return np.min(cc_val)/100.0

    def get_actual_cc_mean(self, date):
        
        cc_val = self.sensor_data.at[date, 'mean']
        return np.mean(cc_val)/100.0

    def get_calendar_date(self):

        return self.sensor_dates 





