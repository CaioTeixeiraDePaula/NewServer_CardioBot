import pydobot
import pydobot.enums as pdn
from .visuals import *


class CardioBot(pydobot.Dobot):
    def __init__(self):
        
        self.tool_status:bool = False


    def connect(self, port):
        start_spiner("Connecting Arm...", 1.5)
        try:           
            self.device = pydobot.Dobot(port=port, verbose=False)
            success_message(message="Arm connected with success :)")
        except KeyError as e:
            fail_message(message=f'{e}')
        


    def _disconnect(self): # Disconnects the arm
        self.home()
        self.close()


    def _move_l(self, x,y,z,r): # Moves the arm in linear way
        start_spiner(message="Starting move...")
        try:
            self.device._set_ptp_cmd(x, y, z, r, mode=pdn.PTPMode.MOVL_XYZ, wait=True)
        except Exception as e:
            fail_message(message=f"{e}")
            self.connect()
            self.device._set_ptp_cmd(x, y, z, r, mode=pdn.PTPMode.MOVL_XYZ, wait=True)
    

    def _move_j(self, x , y, z, r): # Moves the arm in join way
        try:
            self.device._set_ptp_cmd(x, y, z, r, mode=pdn.PTPMode.MOVJ_XYZ, wait=True)
        except Exception as e:
            fail_message(message=f"{e}")
            self.connect()
            self.device._set_ptp_cmd(x, y, z, r, mode=pdn.PTPMode.MOVJ_XYZ, wait=True)


    def home(self): # Put the arm in the home position
        start_spiner(message="Moving to home...")
        try:
            self._move_j(243, 0, 150, 0)
            success_message(message="Robot in home :)")
        except:
            self._move_l(243, 0, 150, 0)
            success_message(message="Robot in home :)")



    def tougle_tool(self, tool:str="suck"): # Tougles the tool status
        self.tool_status = not self.tool_status

        try:
            match tool:
                case "suck":
                    self.device.suck(self.tool_status)
                case "grip":
                    self.device.grip(self.tool_status)
        except Exception as e:
            fail_message(f"{e}")
            self.connect()