from os import listdir
import subprocess
import shutil
import argparse

parser = argparse.ArgumentParser(
                    prog='Image to Video Slideshow Generator',
                    description='Convert a suite of images to video slideshow')
parser.add_argument("-b","--BASE_FOLDER", help="Base folder (image folder)",default="base_images")
parser.add_argument("-i","--IMAGE_SIZE", help="Image size (ex: 1980x1080)",default="1920x1080")
parser.add_argument("-c","--CROPPED_FOLDER", help="Cropped image folder",default="cropped_images")
parser.add_argument("-e","--OUT_FOLDER", help="Output folder",default="out_images")
parser.add_argument("-f","--FPS", help="FPS (ex: 25)", default=25)
parser.add_argument("-t","--TIME_PER_IMAGE", help="time per image", default=5)
parser.add_argument("-o","--OUT_FILE", help="Output file", default="video.mp4")
parser.add_argument("-r","--VIDEO_RESOLUTION", help="video resolution (ex: 1920:1)", default="1920:1")
args = parser.parse_args()

BASE_FOLDER = args.BASE_FOLDER
IMAGE_SIZE = args.IMAGE_SIZE
CROPPED_FOLDER = args.CROPPED_FOLDER
OUT_FOLDER = args.OUT_FOLDER
FPS = args.FPS
TIME_PER_IMAGE = args.TIME_PER_IMAGE
OUT_FILE = args.OUT_FILE
VIDEO_RESOLUTION = args.VIDEO_RESOLUTION

index = 0

for image in listdir(BASE_FOLDER):
    subprocess.run([
        "convert",
        "{}/{}".format(BASE_FOLDER, image),
        "-background",
        "black",
        "-gravity",
        "center",
        "-compress",
        "jpeg",
        "-resize",
        IMAGE_SIZE,
        "-extent",
        IMAGE_SIZE,
        "{}/{}".format(CROPPED_FOLDER,image)
    ])
    for _ in range(TIME_PER_IMAGE):
        file_name = "img_0{}.jpg".format(f'{index:025d}')
        shutil.copyfile("{}/{}".format(CROPPED_FOLDER,image), "{}/{}".format(OUT_FOLDER,file_name))
        index+=1
    print("treating item {}", image)
    
subprocess.Popen(["cat {}/*.jpg | ffmpeg -framerate 1 -f image2pipe -i - {} -vf {}".format(OUT_FOLDER, OUT_FILE, VIDEO_RESOLUTION)], shell=True)