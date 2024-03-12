# 3rd party libraries

import pydicom
import cv2
from pydicom.pixel_data_handlers.util import apply_voi_lut
import numpy as np

# original library

import argparse
import os


def dicom2image(input_directory: str, output_directory: str, brightness: float):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is a command line interface to convert"
                                                 " dicom files to image files.")
    parser.add_argument("-i", "--input_directory", type=str, default="./dicom sets/")
    parser.add_argument("-o", "--output_directory", type=str, default="./image sets/")
    parser.add_argument("-b", "--brightness", type=float, default=0.03)
    args = parser.parse_args()
    dicom2image(args.input_directory, args.output_directory, args.brightness)

