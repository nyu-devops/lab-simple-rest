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
# Create counter
############################################################

# Place code here...


############################################################
# Read counters
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


# ######################################################################
# # Error Handlers
# ######################################################################
# @app.errorhandler(status.HTTP_404_NOT_FOUND)
# def not_found(error):
#     """Handles resources not found with 404_NOT_FOUND"""
#     message = str(error)
#     app.logger.warning(message)
#     return (
#         jsonify(
#             status=status.HTTP_404_NOT_FOUND,
#             error="404 Not Found",
#             message=message
#         ),
#         status.HTTP_404_NOT_FOUND,
#     )


# @app.errorhandler(status.HTTP_405_METHOD_NOT_ALLOWED)
# def method_not_supported(error):
#     """Handles unsupported HTTP methods with 405_METHOD_NOT_SUPPORTED"""
#     message = str(error)
#     app.logger.warning(message)
#     return (
#         jsonify(
#             status=status.HTTP_405_METHOD_NOT_ALLOWED,
#             error="Method not Allowed",
#             message=message,
#         ),
#         status.HTTP_405_METHOD_NOT_ALLOWED,
#     )


# @app.errorhandler(status.HTTP_409_CONFLICT)
# def conflicting_action(error):
#     """Handles unsupported HTTP methods with HTTP_409_CONFLICT"""
#     message = str(error)
#     app.logger.warning(message)
#     return (
#         jsonify(
#             status=status.HTTP_409_CONFLICT,
#             error="409 Conflict",
#             message=message,
#         ),
#         status.HTTP_409_CONFLICT,
#     )
