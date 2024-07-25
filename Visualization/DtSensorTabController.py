class DtSensorTabController(object):
    def __init__(self, dt_controller, sensor_cc_curve, 
                 sensor_leaf_angle_chi_curve, sensor_leaf_lenght_curve, 
                 sensor_leaf_width_curve, sensor_cc_height_curve, 
                 sensor_leaf_angle_alpha_curve,sensor_leaf_angle_beta_curve, 
                 sensor_temperature_curve, sensor_humidty_curve):

        self.dt_controller = dt_controller
        self.sensor_cc_curve = sensor_cc_curve
        self.sensor_leaf_angle_chi_curve = sensor_leaf_angle_chi_curve
        self.sensor_leaf_lenght_curve = sensor_leaf_lenght_curve
        self.sensor_leaf_width_curve = sensor_leaf_width_curve
        self.sensor_cc_height_curve = sensor_cc_height_curve
        self.sensor_leaf_angle_alpha_curve = sensor_leaf_angle_alpha_curve
        self.sensor_leaf_angle_beta_curve = sensor_leaf_angle_beta_curve
        self.sensor_temperature_curve = sensor_temperature_curve
        self.sensor_humidty_curve = sensor_humidty_curve

    def update_ui(self):
        #Sensor Data - Canopy cover
        sensor_cc_points = self.dt_controller.get_sensor_cc_points()
        self.sensor_cc_curve.setData(sensor_cc_points)
        #Sensor Data - leaf chi
        sensor_leaf_chi_points = self.dt_controller.get_sensor_leaf_chi_points()
        self.sensor_leaf_angle_chi_curve.setData(sensor_leaf_chi_points)
        #Sensor Data - leaf length
        sensor_leaf_length_points = self.dt_controller.get_sensor_leaf_length_points()
        self.sensor_leaf_lenght_curve.setData(sensor_leaf_length_points)
        #Sensor Data - leaf width
        sensor_leaf_width_points = self.dt_controller.get_sensor_leaf_width_points()
        self.sensor_leaf_width_curve.setData(sensor_leaf_width_points)
        #Sensor Data - leaf width
        sensor_cc_height_points = self.dt_controller.get_sensor_cc_height_points()
        self.sensor_cc_height_curve.setData(sensor_cc_height_points)
        #Sensor Data - leaf alpha
        sensor_leaf_alpha_points = self.dt_controller.get_sensor_leaf_alpha_points()
        self.sensor_leaf_angle_alpha_curve.setData(sensor_leaf_alpha_points)
        #Sensor Data - leaf beta
        sensor_leaf_beta_points = self.dt_controller.get_sensor_leaf_beta_points()
        self.sensor_leaf_angle_beta_curve.setData(sensor_leaf_beta_points)




