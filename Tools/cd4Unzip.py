import numpy as np
import json
import gzip
import xarray as xr
import time
import sys
import os
from datetime import date, datetime
from netCDF4 import Dataset


root_dir  = os.path.dirname(os.path.realpath(__file__))
file_in = os.path.join(root_dir, "data/","data.nc") 
file_out = os.path.join(root_dir, "data/", "data.csv") 


ds = xr.open_dataset(file_in)
df = ds.to_dataframe()
df.to_csv(file_out)

