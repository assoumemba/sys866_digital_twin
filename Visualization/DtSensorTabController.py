class DtSensorTabController(object):
    def __init__(self, dt_controller, sensor_cc_curve_1, 
                 sensor_leaf_angle_chi_curve, sensor_leaf_lenght_curve, 
                 sensor_leaf_width_curve, sensor_cc_height_curve, 
                 sensor_leaf_angle_alpha_curve,sensor_leaf_angle_beta_curve, 
                 sensor_temperature_curve, sensor_humidty_curve):

        self.dt_controller = dt_controller
        self.sensor_cc_curve_1 = sensor_cc_curve_1
        self.sensor_leaf_angle_chi_curve = sensor_leaf_angle_chi_curve
        self.sensor_leaf_lenght_curve = sensor_leaf_lenght_curve
        self.sensor_leaf_width_curve = sensor_leaf_width_curve
        self.sensor_cc_height_curve = sensor_cc_height_curve
        self.sensor_leaf_angle_alpha_curve = sensor_leaf_angle_alpha_curve
        self.sensor_leaf_angle_beta_curve = sensor_leaf_angle_beta_curve
        self.sensor_temperature_curve = sensor_temperature_curve
        self.sensor_humidty_curve = sensor_humidty_curve

    def update_ui(self):
        pass




