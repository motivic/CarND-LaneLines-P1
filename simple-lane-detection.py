import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
from moviepy.editor import VideoFileClip

class LaneDetector(object):
    def __init__(self, video_file):
        self._video_file = video_file
