import argparse
import SimpleITK as sitk
import glob


def image2nii(input_)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This is a command line interface to convert"
                                                 " image files to nii.gz.")
    parser.add_argument("-i", "--input_directory", type=str, default="./image src/")
    parser.add_argument("-f", "--file", type=str, default="")
    parser.add_argument("-o", "--output_directory", type=str, default="./nii.gz dst/")
    args = parser.parse_args()

"""

Reference
1. https://stackoverflow.com/questions/62896966/how-to-convert-multiple-png-or-jpeg-images-into-one-nifti-image-by-python3

"""