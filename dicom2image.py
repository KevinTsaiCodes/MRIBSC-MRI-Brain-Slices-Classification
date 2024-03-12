# 3rd party libraries

import pydicom
import cv2
from pydicom.pixel_data_handlers.util import apply_voi_lut
import numpy as np

# original library

import argparse
import os
import sys


def dicom2image(input_directory: str, output_directory: str, brightness: float):
    for dicom in os.listdir(input_directory):
        dicom_file_path = os.path.join(input_directory, dicom)  # create full filepath
        if not dicom_file_path.endswith(".dcm"):
            print(f"Skipping {dicom_file_path} because it doesn't with .dcm extension'")
            continue
        try:  # try the conversion
            dicom_file = pydicom.dcmread(dicom_file_path)
            if "VOILUTSequence" in dicom_file:
                image_file = apply_voi_lut(dicom_file.pixel_array, dicom_file)

            else:
                image_file = dicom_file.pixel_array.astype(np.float32) * brightness

        except pydicom.errors.InvalidDicomError as invalid_dicom:
            invalid_dicom.println("Finished Skipping")

        finally:
            print("Finished conversion")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is a command line interface to convert"
                                                 " dicom files to image files.")
    parser.add_argument("-i", "--input_directory", type=str, default="./dicom sets/")
    parser.add_argument("-o", "--output_directory", type=str, default="./image sets/")
    parser.add_argument("-b", "--brightness", type=float, default=0.03)
    args = parser.parse_args()
    dicom2image(args.input_directory, args.output_directory, args.brightness)

