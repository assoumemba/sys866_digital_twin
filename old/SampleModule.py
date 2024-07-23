
from importlib.resources import path
import os

os.environ['DEVELOPMENT'] = 'DEVELOPMENT'
#https://github.com/aquacropos/aquacrop/issues/135

import numpy as np
import pandas as pd

from aquacrop import AquaCropModel, Soil, Crop, InitialWaterContent
from aquacrop.utils import prepare_weather, get_filepath

weather_file_path = get_filepath('tunis_climate.txt')
model_os = AquaCropModel(
            sim_start_time=f"{1979}/10/01",
            sim_end_time=f"{1985}/05/30",
            weather_df=prepare_weather(weather_file_path),
            soil=Soil(soil_type='SandyLoam'),
            crop=Crop('Wheat', planting_date='10/01'),
            initial_water_content=InitialWaterContent(value=['FC']),
        )
model_os.run_model(till_termination=True)
model_results = model_os.get_simulation_results().head()
print(model_results)


root_dir = ".\\data"
data_crop_dir = os.path.join(root_dir, "crop")
os.makedirs(data_crop_dir, exist_ok=True)

data_stats_dir = os.path.join(root_dir, "stats")
os.makedirs(data_stats_dir, exist_ok=True)

#model_os._outputs.water_flux.head()
#model_os._outputs.water_storage.head()
crop_growth = model_os._outputs.crop_growth.head()
print(crop_growth)

final_stats = model_os._outputs.final_stats.head()
print(final_stats)


crop_growth_path = os.path.join(data_crop_dir, "crop_growth.csv")
crop_growth.to_csv(crop_growth_path)

final_stats_path = os.path.join(data_stats_dir, "final_stats.csv")
final_stats.to_csv(final_stats_path)