import numpy as np
import pandas as pd
import pathlib
import sys
from utils import *

class BaseSensor(object):
    def __init__(self, data_path, col_name):
        self.data_path = data_path
        self.sensor_dates = None
        self.zero_value_treshold = 0.06
        self.col_name = col_name
        
        #validate data exists
        data_file = pathlib.Path(self.data_path)
        if not data_file.exists():
            print('Please make sure to prepare data before running this script...')
            sys.exit()
            
        #hold latest data
        self.last_cc_min = 0
        self.last_cc_max = 0
        self.last_cc_mean = 0
        self.sensor_data = None

    def get_actual_cc_val(self, date):
        if self.is_date_exist(date):
            cc_val = self.sensor_data.at[date, self.col_name]
            return cc_val
        return np.zeros(1)

    def select_new_val(self, new_val, old_val):
        if new_val > 0 :
            return new_val 
        else:
            return old_val

    def get_actual_cc_max(self, date):
        
        cc_val = self.get_actual_cc_val(date)
        new_val = np.max(cc_val)/100.0
        #select value to return
        if new_val > self.zero_value_treshold:
            self.last_cc_max = new_val

        return self.select_new_val(new_val, self.last_cc_max)

    def get_actual_cc_min(self, date):
        
        cc_val = self.get_actual_cc_val(date)
        new_val = np.min(cc_val)/100.0
        #select value to return
        if new_val > self.zero_value_treshold:
            self.last_cc_min = new_val

        return self.select_new_val(new_val, self.last_cc_min)


    def get_actual_cc_mean(self, date):
        
        cc_val = self.get_actual_cc_val(date)
        new_val = np.mean(cc_val)/100.0
        #select value to return
        if new_val > self.zero_value_treshold:
            self.last_cc_mean = new_val

        return self.select_new_val(new_val, self.last_cc_mean)

    def get_calendar_date(self):

        return self.sensor_dates 

    def is_date_exist(self, date_in):

        date_list = self.get_calendar_date()
        for date_c in np.nditer(date_list):
            date_c_str = convert_date_to_str(date_c)
            date_in_str = convert_date_to_str(date_in)
            if date_c_str == date_in_str:
                return True

        return False





