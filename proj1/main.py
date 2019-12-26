from PIL import Image
import rawpy
import imageio
import os
import glob
import argparse


def transform_raw_jpg(raw_image, output_image):
    with rawpy.imread(raw_image) as raw:
        rgb = raw.postprocess()
        imageio.imwrite(output_image, rgb)
    return output_image

############ARGPARSE########
parser = argparse.ArgumentParser(description='Transform Raw to JPEG')
parser.add_argument('input_folder', type=str, help='insert folder containing .ORF photos')
parser.add_argument('--output_folder', default="Output_jpg" ,type=str, help='insert output folder for the JPEG photos')
args = parser.parse_args()
#############################

RAW_FOLDER = args.input_folder 
folder = args.output_folder

photos = glob.glob(RAW_FOLDER + "*.ORF")
if not os.path.exists(folder):
    os.mkdir(folder)

for photo in photos:
    photo_jpg = photo.strip(".ORF") + ".jpg"
    photo_folder = os.path.join(folder, os.path.basename(photo_jpg))
    print(photo_folder)
    transform_raw_jpg(photo, photo_folder)
