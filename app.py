"""
Simple REST API using Flask

You have been asked to create a web service that can keep 
track of multiple counters. 

The web service has the following requirements:

- The API must be RESTful.
- The endpoint must be called /counters.
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to get a counter's current value.
- The service must be able to delete a counter.

"""



############################################################
# Base URL
############################################################

# Place code here...



############################################################
# List counters
############################################################

# Place code here...


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

# Place code here...


############################################################
# Update counters
############################################################

# Place code here...


############################################################
# Delete counters
############################################################

# Place code here...

