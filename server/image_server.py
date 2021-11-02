# Sets up Flask, start camera stream and link them together

# Import the components
from flask import Flask, render_template, Response
import camera_stream
import time

# Set up Flas object
app = Flask(__name__)

# Setup route for index page
@app.route('/')
def index():
    # Render the template
    return render_template('image_server.html')

# Generator function to set up the video feed
def frame_generator():
    """This is our main video feed"""
    camera = camera_stream.setup_camera()

    # Allow the camera to warm up
    time.sleep(0.1)

    # Begin generator loop
    for frame in camera_stream.start_stream(camera):
        
        # Get the encoded bytes
        encoded_bytes = camera_stream.get_encoded_bytes_for_frame(frame)

        # Return HTML prefixed raw bytes (\r\n are raw line-ending characters)
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + encoded_bytes + b'\r\n')


# Setup route for loopable stream of HTTP frames from frame_generator
@app.route('/display')
def display():
    # Specify content type with boundary between items (string of characters frame)
    return Response(frame_generator(),
        mimetype='multipart/x-mixed-replace; boundary=frame')

# Start Flask on port 5001
app.run(host="0.0.0.0", debug=True, port=5001)
