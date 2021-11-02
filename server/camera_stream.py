# Helper library to set up the camera and get data streams from it

# Camera access code
from picamera.array import PiRGBArray
from picamera import PiCamera

# Numeriacl python
import numpy as np

# OpenCV (vision library)
import cv2

# Parameters specifying size and image quality
size = (320, 240)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

# Function to setup up the camera
def setup_camera():
    camera = PiCamera()
    camera.resolution = size
    camera.framerate = 24
    camera.rotation = 180 # Camera upside down
    return camera

# Generator function to start capturing a stream of images a frame at a time
def start_stream(camera):
    # Store for RGB image
    image_storage = PiRGBArray(camera, size=size)

    # Set up the stream (take photos repeatedly, format as RGB, reduce quality in exchange for faster frames)
    cam_stream = camera.capture_continuous(image_storage, format="bgr", use_video_port=True)

    # Begin generator loop
    for raw_frame in cam_stream:
        # Return 1 image
        yield raw_frame.array
        # Throw away addtional images
        image_storage.truncate(0)

# Function to encode image as jpeg, then into bytes
def get_encoded_bytes_for_frame(frame):
    result, encoded_image = cv2.imencode('.jpg', frame, encode_param)
    return encoded_image.tostring()
