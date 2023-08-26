# Images to Video slideshow

Simple python script to convert a folder of images to a video slideshow.

## Requirements 
- Python >= 3.10
- imagemagick
- ffmpeg

This script was tested on linux (ubuntu based distro 22.04)

## How to use ? 

1. Create a python venv directory 
> python3 -m venv venv 
2. Active the venv directory
> source venv/bin/activate
3. install dependencies from requirements.txt
> pip install -r requirements.txt
4. run the main file
> python main.py 

To configure some parameters such as image size, folders or duration per video, use the following commands arguments

- -b or --BASE_FOLDER : Base folder (image folder) default="base_images"
- -i or --IMAGE_SIZE : Image size (ex: 1980x1080) default="1920x1080"
- -c or --CROPPED_FOLDER : Cropped image folder default="cropped_images"
- -e or --OUT_FOLDER : Output folder",default out_images"
- -f or --FPS : FPS (ex: 25) default=25
- -t or --TIME_PER_IMAGE : time per image default=5
- -o or --OUT_FILE : Output file default="video.mp4"
- -r or --VIDEO_RESOLUTION : video resolution (ex: 1920:1) default="1920:1"

by default if the parameters are not specified, the default will be used
by default put all your pictures in the base_images folder saved as jpg format