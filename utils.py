import os
import pandas as pd

ROOT_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

CANOPY_SENSORS_PATH =  os.path.join(ROOT_DIR, 'datasets', 'sensors', 'season_4_canopy_cover_sensor.csv')

def convert_date_to_str(date_val):
    date_str = pd.to_datetime(str(date_val)).strftime('%Y-%m-%d')
    return date_str