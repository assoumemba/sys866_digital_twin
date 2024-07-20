# CCo (float): Fractional canopy cover size at emergence
# CCx (float): Maximum canopy cover (fraction of soil cover)
# CGC (float): Canopy growth coefficient (fraction per gdd)
# CDC (float): Canopy decline coefficient (fraction per gdd/calendar day)
# dt (float): Time delta of canopy growth (1 calander day or ... gdd)
# Mode (str): stage of Canopy developement (Growth or Decline)
# CCx0 (float): Maximum canopy cover (fraction of soil cover)



from importlib.resources import path
import os

os.environ['DEVELOPMENT'] = 'DEVELOPMENT'
#https://github.com/aquacropos/aquacrop/issues/135

import numpy as np
import pandas as pd

from aquacrop import AquaCropModel, Soil, Crop, InitialWaterContent, IrrigationManagement
from aquacrop.utils import prepare_weather, get_filepath

# define labels to help after
labels=[]
outputs=[]

soil= Soil('SandyLoam')
sim_start = '1982/05/01'
sim_end = '2018/10/30'
crop = Crop('Maize',planting_date='05/01')
initWC = InitialWaterContent(value=['FC'])

path = get_filepath('champion_climate.txt')
wdf = prepare_weather(path)



def get_depth(model):    
    t = model._clock_struct.time_step_counter # current timestep
    # get weather data for next 7 days
    weather10 = model._weather[t+1:min(t+10+1,len(model._weather))]
    # if it will rain in next 7 days
    if sum(weather10[:,2])>0:
        # check if soil is over 70% depleted
        if t>0 and model._init_cond.depletion/model._init_cond.taw > 0.7:
            depth=10
        else:
            depth=0
    else:
        # no rain for next 10 days
        depth=10


    return depth

# create model with IrrMethod= Constant depth
crop.Name = 'weather' # add helpfull label

model = AquaCropModel(sim_start,sim_end,wdf,soil,crop,initial_water_content=initWC,
                      irrigation_management=IrrigationManagement(irrigation_method=5,)) 

model._initialize()

while model._clock_struct.model_is_finished is False:    
    # get depth to apply
    depth=get_depth(model)
    
    model._param_struct.IrrMngt.depth=depth

    model.run_model(initialize_model=False)

outputs.append(model._outputs.final_stats) # save results
labels.append('weather')

##OUTPUT###
root_dir = ".\\data"
data_crop_dir = os.path.join(root_dir, "crop")
os.makedirs(data_crop_dir, exist_ok=True)

data_stats_dir = os.path.join(root_dir, "stats")
os.makedirs(data_stats_dir, exist_ok=True)

#model._outputs.water_flux.head()
#model._outputs.water_storage.head()
crop_growth = model._outputs.crop_growth
#print(crop_growth)

final_stats = model._outputs.final_stats
#print(final_stats)


crop_growth_path = os.path.join(data_crop_dir, "crop_growth.csv")
crop_growth.to_csv(crop_growth_path)

final_stats_path = os.path.join(data_stats_dir, "final_stats.csv")
final_stats.to_csv(final_stats_path)