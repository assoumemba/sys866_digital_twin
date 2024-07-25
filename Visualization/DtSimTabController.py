class DtSimTabController(object):
    def __init__(self, dt_controller, sim_humidity_curve, sim_cc_curve, sim_cc_max_curve):
        
        self.dt_controller = dt_controller
        self.sim_humidity_curve = sim_humidity_curve
        self.sim_cc_curve = sim_cc_curve
        self.sim_cc_max_curve = sim_cc_max_curve

    def update_ui(self):
        #Modele numerique
        dt_cc_points = self.dt_controller.get_dt_cc_points()
        self.sim_cc_curve.setData(dt_cc_points)

        dt_max_cc_points = self.dt_controller.get_dt_max_cc_points()
        self.sim_cc_max_curve.setData(dt_max_cc_points)

        dt_depletion_points = self.dt_controller.get_dt_depletion_points()
        self.sim_humidity_curve.setData(dt_depletion_points)


