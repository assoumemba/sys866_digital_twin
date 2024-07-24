class DtActuatorTabController(object):
    def __init__(self, dt_controller, actu_val_min_curve,
                 actu_val_min_water_curve, actu_val_mean_curve, actu_val_mean_water_curve):
        
        self.dt_controller = dt_controller
        self.actu_val_min_curve = actu_val_min_curve
        self.actu_val_min_water_curve = actu_val_min_water_curve
        self.actu_val_mean_curve = actu_val_mean_curve
        self.actu_val_mean_water_curve = actu_val_mean_water_curve

    def update_ui(self):
        pass




