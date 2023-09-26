"""
Simple REST API using Flask
"""
from flask import Flask, jsonify, abort, url_for
import status

app = Flask(__name__)

COUNTERS: dict = {}


############################################################
# Index page
############################################################
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

    counters = [{"name": name, "counter": counter} for name, counter in COUNTERS.items()]

    return counters


############################################################
# Create counter
############################################################
@app.route("/counters/<name>", methods=["POST"])
def create_counters(name):
    """Create a counter"""
    app.logger.info("Request to Create counter...")

    if name in COUNTERS:
        abort(status.HTTP_409_CONFLICT, f"Counter '{name}' already exists.")

    counter = 0
    COUNTERS[name] = counter

    app.logger.info("Counter %s created.", name)
    location_url = url_for("read_counters", name=name, _external=True)
    return jsonify(name=name, counter=counter), status.HTTP_201_CREATED, {"Location": location_url}


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
        abort(status.HTTP_404_NOT_FOUND, f"Counter '{name}' does not exist")

    app.logger.info("Returning: %s = %d...", name, counter)
    return jsonify(name=name, counter=counter), status.HTTP_200_OK


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
        abort(status.HTTP_404_NOT_FOUND, f"Counter '{name}' does not exist")

    # Increment the counter
    COUNTERS[name] += 1

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


######################################################################
# Error Handlers
######################################################################
@app.errorhandler(status.HTTP_404_NOT_FOUND)
def not_found(error):
    """Handles resources not found with 404_NOT_FOUND"""
    message = str(error)
    app.logger.warning(message)
    return (
        jsonify(
            status=status.HTTP_404_NOT_FOUND,
            error="404 Not Found",
            message=message
        ),
        status.HTTP_404_NOT_FOUND,
    )


@app.errorhandler(status.HTTP_405_METHOD_NOT_ALLOWED)
def method_not_supported(error):
    """Handles unsupported HTTP methods with 405_METHOD_NOT_SUPPORTED"""
    message = str(error)
    app.logger.warning(message)
    return (
        jsonify(
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
            error="Method not Allowed",
            message=message,
        ),
        status.HTTP_405_METHOD_NOT_ALLOWED,
    )


@app.errorhandler(status.HTTP_409_CONFLICT)
def conflicting_action(error):
    """Handles unsupported HTTP methods with HTTP_409_CONFLICT"""
    message = str(error)
    app.logger.warning(message)
    return (
        jsonify(
            status=status.HTTP_409_CONFLICT,
            error="409 Conflict",
            message=message,
        ),
        status.HTTP_409_CONFLICT,
    )
