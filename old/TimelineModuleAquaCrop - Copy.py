from importlib.resources import path
import os

os.environ['DEVELOPMENT'] = 'DEVELOPMENT'
#https://github.com/aquacropos/aquacrop/issues/135

import numpy as np
import pandas as pd

from aquacrop import AquaCropModel, Soil, Crop, InitialWaterContent, IrrigationManagement
from aquacrop.utils import prepare_weather, get_filepath

from utils import *

sim_start = '2017/04/28'
sim_end = '2017/08/30'

from DT.DtCropModel import DtCropModel
from Sensors.CanopyCoverSensor import CanopyCoverSensor

soil_name = 'SandyLoam'
crop_name = 'Maize'
planting_date = '05/01'
weather_path = get_filepath('champion_climate.txt')

ccSensor = CanopyCoverSensor(CANOPY_SENSORS_PATH)
ccSensor.load_data()

dtCrop = DtCropModel(soil_name, sim_start, sim_end, crop_name, planting_date, weather_path)
while dtCrop.is_finished() is False: 
     
    irrigation_depth = 0
    current_date = dtCrop.get_current_date()
    if ccSensor.is_date_exist(current_date):
        
        ccx = dtCrop.get_ccx()
        cc = dtCrop.get_predicted_canopy()
        sensor_cc = ccSensor.get_actual_cc_min(current_date)
        
        if sensor_cc < cc :
            depletion_rate = dtCrop.get_soil_depletion()
            if depletion_rate > 0.7:
                irrigation_depth = 10
            else:
                irrigation_depth = 2
                
    
    dtCrop.day_avance(irrigation_depth)





#crop_data = np.asarray(dtCrop.crop_data)


#root_dir = ".\\data"
#data_crop_dir = os.path.join(root_dir, "crop")
#os.makedirs(data_crop_dir, exist_ok=True)

#crop_data_path = os.path.join(data_crop_dir, "crop_data.csv")
#np.savetxt(crop_data_path,crop_data, delimiter=",", fmt='%s')