import os
os.environ['DEVELOPMENT'] = 'DEVELOPMENT'

import numpy as np
import pandas as pd

from aquacrop.utils import get_filepath

from utils import *

from DT.BaseDt import BaseDt
from DT.DtCropModel import DtCropModel
from Sensors.CanopyCoverSensor import CanopyCoverSensor

class DtModelController(BaseDt):
    def __init__(self):
        
        sim_start = '2017/04/28'
        sim_end = '2017/08/30'

        soil_name = 'SandyLoam'
        crop_name = 'Sorghum' # 'Sorghum', 'SorghumGDD 'Maize'
        planting_date = '05/01'
        weather_path = AQUA_CROP_CONFIG_PATH #get_filepath('champion_climate.txt')

        #cc
        self.ccSensor = CanopyCoverSensor(CANOPY_SENSORS_PATH)
        self.ccSensor.load_data()
        #Height
        self.ccHeightSensor = CanopyCoverSensor(CANOPY_HEIGHT_PATH)
        self.ccHeightSensor.load_data()
        #leaf angle alpha
        self.ccLeafAngleAlphaSensor = CanopyCoverSensor(CANOPY_LEAF_ANGLE_ALPHA_PATH)
        self.ccLeafAngleAlphaSensor.load_data()
        #leaf angle alpha
        self.ccLeafAngleBetaSensor = CanopyCoverSensor(CANOPY_LEAF_ANGLE_BETA_PATH)
        self.ccLeafAngleBetaSensor.load_data()
        #leaf angle ch
        self.ccLeafAngleChiSensor = CanopyCoverSensor(CANOPY_LEAF_ANGLE_CHI_PATH)
        self.ccLeafAngleChiSensor.load_data()
        #Leaf length
        self.ccLeafLengthSensor = CanopyCoverSensor(CANOPY_LEAF_LENGTH_PATH)
        self.ccLeafLengthSensor.load_data()
        #Leaf width
        self.ccLeafWidthSensor = CanopyCoverSensor(CANOPY_LEAF_WIDTH_PATH)
        self.ccLeafWidthSensor.load_data()
        

        self.dtCrop = DtCropModel(soil_name, sim_start, sim_end, crop_name, planting_date, weather_path)

        #statistics
        date_size = 1 #len(self.dtCrop.calendar_dates)
        self.progression_rate = 0

        self.irrigation_points = np.zeros(date_size)
        self.sensor_cc_points = np.zeros(date_size)
        self.dt_cc_points = np.zeros(date_size)
        self.dt_max_cc_points = np.zeros(date_size)
        self.dt_depletion_points = np.zeros(date_size)
        
        self.sensor_cc_height_points = np.zeros(date_size)
        self.sensor_leaf_alpha_points = np.zeros(date_size)
        self.sensor_leaf_beta_points = np.zeros(date_size)
        self.sensor_leaf_chi_points = np.zeros(date_size)
        self.sensor_leaf_length_points = np.zeros(date_size)
        self.sensor_leaf_width_points = np.zeros(date_size)

     
    def get_crop_model(self):
        return self.dtCrop

    def get_sensor_model(self):
        return self.ccSensor

    def run_step(self):
        
        if self.dtCrop.is_finished() is False: 
     
            irrigation_depth = 0
            current_date = self.dtCrop.get_current_date()
            if self.ccSensor.is_date_exist(current_date):
        
                ccx = self.dtCrop.get_ccx()
                cc = self.dtCrop.get_predicted_canopy()
                sensor_cc = self.ccSensor.get_actual_cc_min(current_date)
        
                if sensor_cc < cc :
                    depletion_rate = self.dtCrop.get_soil_depletion()
                    if depletion_rate > 0.7:
                        irrigation_depth = 10
                    else:
                        irrigation_depth = 2
                
    
            self.dtCrop.day_avance(irrigation_depth)
            self.update_statistics(current_date, irrigation_depth)

            

    def update_statistics(self, current_date, irrigation_depth):

        current_day_index = self.dtCrop.get_time_index()
        self.progression_rate = current_day_index * 100 / len(self.dtCrop.calendar_dates)

        #self.irrigation_points[current_day_index] = irrigation_depth
        #self.sensor_cc_points[current_day_index] = self.ccSensor.get_actual_cc_min(current_date)
        #self.dt_cc_points[current_day_index] = self.dtCrop.get_predicted_canopy()
        #self.dt_max_cc_points[current_day_index] = self.dtCrop.get_ccx()
        #self.dt_depletion_points[current_day_index] = self.dtCrop.get_soil_depletion()
        
        self.irrigation_points = np.append(self.irrigation_points, irrigation_depth)
        self.sensor_cc_points = np.append(self.sensor_cc_points, self.ccSensor.get_actual_cc_mean(current_date))
        self.dt_cc_points = np.append(self.dt_cc_points, self.dtCrop.get_predicted_canopy())
        self.dt_max_cc_points = np.append(self.dt_max_cc_points, self.dtCrop.get_ccx())
        self.dt_depletion_points = np.append(self.dt_depletion_points, self.dtCrop.get_soil_depletion())

        self.sensor_cc_height_points = np.append(self.sensor_cc_height_points, self.ccHeightSensor.get_actual_cc_mean(current_date))
        self.sensor_leaf_alpha_points = np.append(self.sensor_leaf_alpha_points, self.ccLeafAngleAlphaSensor.get_actual_cc_mean(current_date))
        self.sensor_leaf_beta_points = np.append(self.sensor_leaf_beta_points, self.ccLeafAngleBetaSensor.get_actual_cc_mean(current_date))
        self.sensor_leaf_chi_points = np.append(self.sensor_leaf_chi_points, self.ccLeafAngleChiSensor.get_actual_cc_mean(current_date))
        self.sensor_leaf_length_points = np.append(self.sensor_leaf_length_points, self.ccLeafLengthSensor.get_actual_cc_mean(current_date))
        self.sensor_leaf_width_points = np.append(self.sensor_leaf_width_points, self.ccLeafWidthSensor.get_actual_cc_mean(current_date))
        


    def get_irrigation_points(self):
        return self.irrigation_points

    def get_sensor_cc_points(self):
        return self.sensor_cc_points

    def get_dt_cc_points(self):
        return self.dt_cc_points

    def get_dt_max_cc_points(self):
        return self.dt_max_cc_points

    def get_dt_depletion_points(self):
        return self.dt_depletion_points

    def get_progression_rate(self):
        return self.progression_rate

    def get_sensor_cc_height_points(self):
        return self.sensor_cc_height_points

    def get_sensor_leaf_alpha_points(self):
        return self.sensor_leaf_alpha_points

    def get_sensor_leaf_beta_points(self):
        return self.sensor_leaf_beta_points

    def get_sensor_leaf_chi_points(self):
        return self.sensor_leaf_chi_points

    def get_sensor_leaf_length_points(self):
        return self.sensor_leaf_length_points

    def get_sensor_leaf_width_points(self):
        return self.sensor_leaf_width_points
