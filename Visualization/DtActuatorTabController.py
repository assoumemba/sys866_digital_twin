class DtActuatorTabController(object):
    def __init__(self, dt_controller, actu_val_min_curve,
                 actu_val_min_water_curve, actu_val_mean_curve, actu_val_mean_water_curve):
        
        self.dt_controller = dt_controller
        self.actu_val_min_curve = actu_val_min_curve
        self.actu_val_min_water_curve = actu_val_min_water_curve
        self.actu_val_mean_curve = actu_val_mean_curve
        self.actu_val_mean_water_curve = actu_val_mean_water_curve

    def update_ui(self):
        
        #Valves
        valve_1_trigger_points = self.dt_controller.get_valve_1_trigger_points()
        self.actu_val_min_curve.setData(valve_1_trigger_points)

        valve_1_value_points = self.dt_controller.get_valve_1_value_points()
        self.actu_val_min_water_curve.setData(valve_1_value_points)

        valve_2_trigger_points = self.dt_controller.get_valve_2_trigger_points()
        self.actu_val_mean_curve.setData(valve_2_trigger_points)
        
        valve_2_value_points = self.dt_controller.get_valve_2_value_points()
        self.actu_val_mean_water_curve.setData(valve_2_value_points)




