import pydicom
import cv2
from pydicom.pixel_data_handlers.util import apply_voi_lut
import numpy as np
import argparse
import os
import sys


def dicom2image(input_directory: str, output_directory: str, brightness: float, pixel_array=None):
    for dicom_file_name in os.listdir(input_directory):
        full_dicom_path = os.path.join(input_directory, dicom_file_name)

        try:
            dicom_file = pydicom.dcmread(full_dicom_path)  # read dicom file
            if "VOILUTSequence" in dicom_file:
                output_image_file = apply_voi_lut(arr=dicom_file.pixel_array, ds=dicom_file)
            else:  # no VOILUTSequence
                output_image_file = dicom_file.pixel_array.astype(np.float32) * brightness

            cv2.imwrite(os.path.join(output_directory, os.path.splitext(dicom_file_name)[0] + ".png"), output_image_file)

        except pydicom.errors.InvalidDicomError as DICOMError:
            DICOMError.print(f"{dicom_file} is an invalid DICOM file.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is a command line interface to convert"
                                                 " dicom files to image files.")
    parser.add_argument("-i", "--input_directory", type=str, default="./dicom sets/")
    parser.add_argument("-o", "--output_directory", type=str, default="./image sets/")
    parser.add_argument("-b", "--brightness", type=float, default=0.3)
    args = parser.parse_args()
    dicom2image(args.input_directory, args.output_directory, args.brightness)


"""
Reference:

1. APPLY_VOI_LUT (pydicom): https://pydicom.github.io/pydicom/dev/reference/generated/pydicom.pixel_data_handlers.apply_voi_lut.html
2. PIXEL_ARRAY (pydicom): https://pydicom.github.io/pydicom/stable/reference/generated/pydicom.dataset.Dataset.html#pydicom.dataset.Dataset.pixel_array

"""