import argparse
import SimpleITK as sitk
import glob


def image2nii(input_directory, save_filename, output_directory):
    image_folder_files = glob.glob("./" + input_directory + "/*.png")
    nii_reader = sitk.ImageSeriesReader()
    nii_reader.SetFileNames(image_folder_files)
    save_nii_file = nii_reader.Execute()
    sitk.WriteImage(save_nii_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This is a command line interface to convert"
                                                 " image files to nii.gz.")
    parser.add_argument("-i", "--input_directory", type=str, default="./image src/")
    parser.add_argument("-f", "--output_file", type=str, default="out.nii.gz")
    parser.add_argument("-o", "--output_directory", type=str, default="./nii.gz dst/")
    args = parser.parse_args()

"""
Reference

1. https://stackoverflow.com/questions/62896966/how-to-convert-multiple-png-or-jpeg-images-into-one-nifti-image-by-python3
2. https://simpleitk.readthedocs.io/en/master/link_DicomSeriesReader_docs.html


"""