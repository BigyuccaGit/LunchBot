# Use Image App Core with behaviour to send images to the web service
# and accepts a simple exit control message

# The imports
import time

from image_app_core import start_server_process, get_control_instruction, put_output_image
import camera_stream


# Define the behaviour
def controlled_image_server_behavior():

    # Set up camera and let it warm up
    camera = camera_stream.setup_camera()
    time.sleep(0.1)

    # Loop over frames
    for frame in camera_stream.start_stream(camera):

        # Get the encoded bytes
        encoded_bytes = camera_stream.get_encoded_bytes_for_frame(frame)

        # Put in the queue
        put_output_image(encoded_bytes)

        # See if there is any control instruction to exit,if so, return
        instruction = get_control_instruction()
        if instruction and instruction['command'] == "exit":
                print("Stopping")
                return

# Start the server and the behaviour
process = start_server_process('control_image_behavior.html')

# Exit when exit command received
try:
    controlled_image_server_behavior()
finally:
    process.terminate()
