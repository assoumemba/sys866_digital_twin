# CCo (float): Fractional canopy cover size at emergence
# CCx (float): Maximum canopy cover (fraction of soil cover)
# CGC (float): Canopy growth coefficient (fraction per gdd)
# CDC (float): Canopy decline coefficient (fraction per gdd/calendar day)
# dt (float): Time delta of canopy growth (1 calander day or ... gdd)
# Mode (str): stage of Canopy developement (Growth or Decline)
# CCx0 (float): Maximum canopy cover (fraction of soil cover)

from DT.BaseDt import BaseDt
from importlib.resources import path
import os

os.environ['DEVELOPMENT'] = 'DEVELOPMENT'
#https://github.com/aquacropos/aquacrop/issues/135

import numpy as np
import pandas as pd
from datetime import date, datetime, timedelta

from aquacrop import AquaCropModel, Soil, Crop, InitialWaterContent, IrrigationManagement
from aquacrop.utils import prepare_weather, get_filepath


class DtCropModel(BaseDt):
      
    def __init__(self, soil_name, sim_start, sim_end, crop_name, planting_date, weather_path):
        
        soil= Soil(soil_name)
        crop = Crop(crop_name,planting_date=planting_date)
        initWC = InitialWaterContent(value=['FC'])
        wdf = prepare_weather(weather_path)

        
        
        self.model = AquaCropModel(sim_start,sim_end,wdf,soil,crop,initial_water_content=initWC,
                              irrigation_management=IrrigationManagement(irrigation_method=5,)) 

        self.model._initialize()
        self.crop_data = self.get_crop_data()


        sdate = datetime.strptime(sim_start, '%Y/%m/%d').date()
        edate = datetime.strptime(sim_end, '%Y/%m/%d').date()
        
        self.calendar_dates = pd.date_range(sdate,edate-timedelta(days=1),freq='d')


    def day_avance(self, depth):
        if self.is_finished() is False:    
            
            self.model._param_struct.IrrMngt.depth=depth
            self.model.run_model(initialize_model=False)
            self.cumul_stats()


    def get_depth(self):    
        t = self.model._clock_struct.time_step_counter # current timestep
        # get weather data for next 7 days
        weather10 = self.model._weather[t+1:min(t+10+1,len(self.model._weather))]
        # if it will rain in next 7 days
        if sum(weather10[:,2])>0:
            # check if soil is over 70% depleted
            if t>0 and self.get_soil_depletion() > 0.7:
                depth=10
            else:
                depth=0
        else:
            # no rain for next 10 days
            depth=10


        return depth

    def get_ccx(self):
        
        current_ccx = self.model._init_cond.ccx_act
        return current_ccx

    def get_et0(self):
        
        current_ccx = self.model._init_cond.et0
        return current_ccx

    def get_ccx_crop(self):
        
        ccx = self.model.crop.CCx
        return ccx

    def get_max_canopy(self):
        
        current_max = self.model.crop.MaxCanopy
        return current_max

    def get_predicted_canopy(self):
        
        cc = 0
        t = self.get_time_index() - 1
        if t > 0:

            crop_growth = np.array(self.model._outputs.crop_growth)[t]

            canopy_cover_index = 7
            cc = crop_growth[canopy_cover_index]

        return cc

    def get_time_index(self):
        t = self.model._clock_struct.time_step_counter # current timestep
        return t

    def get_soil_depletion(self):
        if self.get_time_index() > 0:
            depletion_level = self.model._init_cond.depletion/self.model._init_cond.taw
            return depletion_level
        return 0

    def is_finished(self):
        model_is_finished =self.model._clock_struct.model_is_finished
        return model_is_finished

    def get_current_date(self):

        index = self.get_time_index()
        date_cal = self.calendar_dates[index]
        return date_cal

    def get_crop_data(self):

        crop = self.model.crop
        data = np.array([
            crop.Aer,
            crop.CC0,
            crop.CCmin,
            crop.CCx,
            crop.CDC,
            crop.CDC_CD,
            crop.CGC,
            crop.CGC_CD,
            crop.CalendarType,
            crop.Canopy10Pct,
            crop.Canopy10PctCD,
            crop.CanopyDevEnd,
            crop.CanopyDevEndCD,
            crop.CropType,
            crop.Determinant,
            crop.ET0dorm,
            crop.ETadj,
            crop.Emergence,
            crop.EmergenceCD,
            crop.Flowering,
            crop.FloweringCD,
            crop.FloweringEndCD,
            crop.GDD_lo,
            crop.GDD_up,
            crop.GDDmethod,
            crop.GermThr,
            crop.HI0,
            crop.HIGC,
            crop.HIend,
            crop.HIendCD,
            crop.HIini,
            crop.HIstart,
            crop.HIstartCD,
            crop.Kcb,
            crop.LagAer,
            crop.Maturity,
            crop.MaturityCD,
            crop.MaxCanopy,
            crop.MaxCanopyCD,
            crop.MaxFlowPct,
            crop.MaxRooting,
            crop.MaxRootingCD,
            crop.Name,
            crop.PctZmin,
            crop.PlantMethod,
            crop.PlantPop,
            crop.PolColdStress,
            crop.PolHeatStress,
            crop.SeedSize,
            crop.Senescence,
            crop.SenescenceCD,
            crop.SwitchGDD,
            crop.SwitchGDDType,
            crop.SxBot,
            crop.SxBotQ,
            crop.SxTop,
            crop.SxTopQ,
            crop.Tbase,
            crop.Tmax_lo,
            crop.Tmax_up,
            crop.Tmin_lo,
            crop.Tmin_up,
            crop.TrColdStress,
            crop.Tupp,
            crop.WP,
            crop.WPy,
            crop.YldForm,
            crop.YldFormCD,
            crop.YldWC,
            crop.Zmax,
            crop.Zmin,
            ])
        return data

    def cumul_stats(self):
        pass
        












