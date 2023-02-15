"""
Simple REST API using Flask
"""
from flask import Flask, jsonify, abort, url_for
import status

app = Flask(__name__)

COUNTERS: dict = {}

@app.route("/", methods=["GET"])
def index():
    """Root URL"""
    return {"status": "OK"}

############################################################
# List counters
############################################################
@app.route("/counters", methods=["GET"])
def list_counters():
    """List counters"""
    app.logger.info("Request to list all counters...")

    counters: list = []
    for name in COUNTERS:  # pylint: disable=consider-using-dict-items
        counters.append({"name" : name, "counter" : COUNTERS[name]})

    return counters


############################################################
# Read counters
############################################################
@app.route("/counters/<name>", methods=["GET"])
def read_counters(name: str):
    """Read a counter"""
    app.logger.info("Request to Read counter: %s...", name)

    # Try and get the counter
    counter = COUNTERS.get(name)

    # Return an error if the counter cannot be found
    if counter is None:
        abort(status.HTTP_404_NOT_FOUND, f"Counter {name} does not exist")

    app.logger.info("Returning: %s = %d...", (name, counter))
    return jsonify(name=name, counter=counter), status.HTTP_200_OK


############################################################
# Create counter
############################################################
@app.route("/counters/<name>", methods=["POST"])
def create_counters(name):
    """Create a counter"""
    app.logger.info("Request to Create counter...")
    global COUNTERS

    if name in COUNTERS:
        abort(status.HTTP_409_CONFLICT, f"Counter {name} already exists.")

    counter = 0
    COUNTERS[name] = counter

    app.logger.info("Counter %s created.", name)
    location_url = url_for("read_counters", name=name, _external=True)
    return jsonify(name=name, counter=counter), status.HTTP_201_CREATED, {"Location": location_url}


############################################################
# Update counters
############################################################
@app.route("/counters/<name>", methods=["PUT"])
def update_counters(name):
    """Update a counter"""
    app.logger.info("Request to Update counter %s...", name)

    # Try and get the counter
    counter = COUNTERS.get(name)

    # Return an error if the counter cannot be found
    if counter is None:
        abort(status.HTTP_404_NOT_FOUND, f"Counter {name} does not exist")

    # Increment the counter
    COUNTERS[name]  = COUNTERS[name] + 1

    return jsonify(name=name, counter=COUNTERS[name]), status.HTTP_200_OK


############################################################
# Delete counters
############################################################
@app.route("/counters/<name>", methods=["DELETE"])
def delete_counters(name):
    """Delete a counter"""
    app.logger.info("Request to Delete counter...")

    if name in COUNTERS:
        del COUNTERS[name]

    return "", status.HTTP_204_NO_CONTENT
