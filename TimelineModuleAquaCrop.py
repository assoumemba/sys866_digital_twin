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

available_dates = ccSensor.get_calendar_date()

date_val = available_dates[2]
date_str = convert_date_to_str(date_val)


cc_val_min = ccSensor.get_actual_cc_min(date_str)
cc_val_max = ccSensor.get_actual_cc_max(date_str)
cc_val_mean = ccSensor.get_actual_cc_mean(date_str)

dtCrop = DtCropModel(soil_name, sim_start, sim_end, crop_name, planting_date, weather_path)
while dtCrop.is_finished() is False: 
    
    dtCrop.day_avance(0)
    current_date = convert_date_to_str(dtCrop.get_current_date())
    
    ccx = dtCrop.get_ccx()
    cc = dtCrop.get_predicted_canopy()

    soil = dtCrop.get_soil_depletion()




#crop_data = np.asarray(dtCrop.crop_data)


#root_dir = ".\\data"
#data_crop_dir = os.path.join(root_dir, "crop")
#os.makedirs(data_crop_dir, exist_ok=True)

#crop_data_path = os.path.join(data_crop_dir, "crop_data.csv")
#np.savetxt(crop_data_path,crop_data, delimiter=",", fmt='%s')