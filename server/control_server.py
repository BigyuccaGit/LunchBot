# Scrpt to act as a control web service using Flask
from flask import Flask
from robot_modes import RobotModes

# A Flask App contains all its routes.
app = Flask(__name__)

# Prepare our robot modes for use
mode_manager = RobotModes()

# Route to run the selected app
@app.route("/run/<mode_name>", methods=['POST'])
def run(mode_name):
    # Use our robot app to run something with this mode_name
    mode_manager.run(mode_name)
    # Confirming message
    return "%s running"

# Route to support the stop running process operation
@app.route("/stop", methods=['POST'])
def stop():
    # Tell our system to stop the mode it's in.
    mode_manager.stop()
    return "Stopped"

# Start the server
app.run(host="0.0.0.0", debug=True)
