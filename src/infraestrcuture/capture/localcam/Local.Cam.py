import cv2
from src.domain.interface.ICamera import ICamera

class LocalCam(ICamera):
    def __init__(self, camera_index = 0):
        self.camera_index = camera_index

    def connect_cam(self):
        cap = cv2.VideoCapture(self.camera_index)

    def read_frame(self):
        raise NotImplementedError

    def disconnect_cam(self):
        raise NotImplementedError    