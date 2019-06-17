from client.comm import BaseComm
from common.frame_enum import FrameType

class GUIController:
    def __init__(self, comm: BaseComm):
        self.comm = comm
        self.comm.listen_for([FrameType.ALL])       # FrameType all until we know what frametype we want

    def process(self):
        while self.comm.has_data():
            frame = self.comm.get_data()

            if frame.request:
                continue
            
            values = frame.get_data()

    def stop(self):
        self.comm.stop()
