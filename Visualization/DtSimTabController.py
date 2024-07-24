class DtSimTabController(object):
    def __init__(self, dt_controller, sim_humidity_curve, sim_cc_curve, sim_cc_max_curve):
        
        self.dt_controller = dt_controller
        self.sim_humidity_curve = sim_humidity_curve
        self.sim_cc_curve = sim_cc_curve
        self.sim_cc_max_curve = sim_cc_max_curve

    def update_ui(self):
        pass


