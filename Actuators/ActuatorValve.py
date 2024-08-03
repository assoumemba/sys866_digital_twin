import numpy as np
import pandas as pd
from Actuators.BaseActuator import BaseActuator

class ActuatorValve(BaseActuator):
    def __init__(self):

        self.trigger_points = np.zeros(1)
        self.value_points = np.zeros(1)

    def append_value(self, trigger, value):

        self.trigger_points = np.append(self.trigger_points, trigger)
        self.value_points = np.append(self.value_points, value)
        
    def get_trigger_points(self):
        return self.trigger_points

    def get_value_points(self):
        return self.value_points



