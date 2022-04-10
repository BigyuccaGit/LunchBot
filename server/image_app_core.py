# Web app core to set up queues, run server process and set up Flask based routing

# The imports
import time
from multiprocessing import Process, Queue

from flask import Flask, render_template, Response, request

# Define queues and Flask app
app = Flask(__name__)
control_queue = Queue()
display_queue = Queue(maxsize=2)

# Define a global main template
display_template = 'image_server.html'

# Add route for index, rendering specified template
@app.route('/')
def index():
    return render_template(display_template)

# Generator function to get the video feed from the queue
def frame_generator():
    while True:
        # Limit frame rate to 20/second
        time.sleep(0.05)

        # Get a frame of encoded bytes
        encoded_bytes = display_queue.get()

        # Return HTML prefixed raw bytes (\r\n are raw line-ending characters)
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + encoded_bytes + b'\r\n')
        
# Setup route for loopable stream of HTTP frames from frame_generator
@app.route('/display')
def display():
    # Specify content type with boundary between items (string of characters frame)
    return Response(frame_generator(),
        mimetype='multipart/x-mixed-replace; boundary=frame')

# Setup route to post control messages (in dictionary form) via a queue to the robot
@app.route('/control', methods=['POST'])
def control():
    control_queue.put(request.form)
    return Response('queued')

# Function to start the server process 
def start_server_process(template_name):
    """Start the process, call .terminate to close it"""
    global display_template
    display_template = template_name
    # Start process running the Flask app using supplied parameters
    server = Process(target=app.run, kwargs={"host": "0.0.0.0", "port": 5001})
    server.start()
    return server

# Function to queue an output image
def put_output_image(encoded_bytes):
    
    if display_queue.empty():
        display_queue.put(encoded_bytes)

# Function to get control messages from the queue
def get_control_instruction():
    # Don't wait if nothing in the queue
    if control_queue.empty():
        return None
    else:
        return control_queue.get()
