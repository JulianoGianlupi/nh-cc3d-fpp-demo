from cc3d.core.PySteppables import *


class FocalPointPlasticityDemoSteppable(SteppableBasePy):

    def __init__(self, frequency=1):
        SteppableBasePy.__init__(self, frequency)

    def start(self):
        """
        Any code in the start function runs before MCS=0

        :return: None
        """
        self.init_config()

    def step(self, mcs):
        """
        type here the code that will run every frequency MCS
        
        :param mcs: current Monte Carlo step
        """
        # Run infinitely
        self.set_max_mcs(mcs + self.frequency + 1)
        # Initialize a new configuration if everything is dead
        if len(self.cell_list) == 0:
            self.init_config()
        # Kill anything at a upper/lower boundary
        for x in range(self.dim.x):
            cell = self.cell_field[x, 0, 0]
            if cell:
                cell.targetVolume = 0
            cell = self.cell_field[x, self.dim.y - 1, 0]
            if cell:
                cell.targetVolume = 0

    def init_config(self):
        """
        Initializes the cellular configuration of this demo

        :return: None
        """
        ch = int(self.dim.y / 2)
        for x in range(0, self.dim.x, 7):
            cell_t = self.new_cell(self.cell_type.Towards)
            cell_a = self.new_cell(self.cell_type.Away)
            cell_t.targetVolume = 49
            cell_a.targetVolume = 49
            cell_t.lambdaVolume = 2
            cell_a.lambdaVolume = 2
            for y in range(8):
                for xx in range(x, x + 8):
                    self.cell_field[xx, ch + y, 0] = cell_a
                    self.cell_field[xx, ch - y - 1, 0] = cell_t


class SteeringPanelSteppable(SteppableBasePy):
    def add_steering_panel(self):
        """
        Add steering panel to Player

        :return: None
        """
        self.add_steering_param(name='lambda_link',
                                val=10.0,
                                min_val=0.0,
                                max_val=10.0,
                                widget_name='slider',
                                decimal_precision=1)
        self.add_steering_param(name='lambda_chemo',
                                val=1E3,
                                min_val=0,
                                max_val=2E3,
                                widget_name='slider')

    def process_steering_panel_data(self):
        """
        Responds to change in Player steering panel

        :return: None
        """
        lambda_link = self.get_steering_param('lambda_link')
        self.get_xml_element('fpp_lam_tt').cdata = lambda_link
        self.get_xml_element('fpp_lam_aa').cdata = lambda_link
        lambda_chemo = self.get_steering_param('lambda_chemo')
        self.get_xml_element('chemo_lam_t').Lambda = lambda_chemo
        self.get_xml_element('chemo_lam_a').Lambda = -1 * lambda_chemo
