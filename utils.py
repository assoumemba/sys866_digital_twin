import os
import pandas as pd

ROOT_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

#Canopy
CANOPY_SENSORS_PATH =  os.path.join(ROOT_DIR, 'datasets', 'sensors', 'season_4_canopy_cover_sensor.csv')
CANOPY_HEIGHT_PATH =  os.path.join(ROOT_DIR, 'datasets', 'sensors', 'season_4_canopy_height_sensor.csv')
CANOPY_LEAF_ANGLE_ALPHA_PATH =  os.path.join(ROOT_DIR, 'datasets', 'sensors', 'season_4_leaf_angle_alpha_sensor.csv')
CANOPY_LEAF_ANGLE_BETA_PATH =  os.path.join(ROOT_DIR, 'datasets', 'sensors', 'season_4_leaf_angle_beta_sensor.csv')
CANOPY_LEAF_ANGLE_CHI_PATH =  os.path.join(ROOT_DIR, 'datasets', 'sensors', 'season_4_leaf_angle_chi_sensor.csv')
CANOPY_LEAF_LENGTH_PATH =  os.path.join(ROOT_DIR, 'datasets', 'sensors', 'season_4_leaf_length_sensor.csv')
CANOPY_LEAF_WIDTH_PATH =  os.path.join(ROOT_DIR, 'datasets', 'sensors', 'season_4_leaf_width_sensor.csv')

#Climate 
ENVIRONMENT_CONFIG_PATH = os.path.join(ROOT_DIR, 'datasets', 'aquacrop', 'climate_data_summary2.csv')
AQUA_CROP_CONFIG_PATH = os.path.join(ROOT_DIR, 'datasets', 'aquacrop', 'climate_data_summary_21.txt') 

def convert_date_to_str(date_val):
    date_str = pd.to_datetime(str(date_val)).strftime('%Y-%m-%d')
    return date_str