import json

def lambda_handler(event, context):
    # Extract the object_key from the event
    object_key = event['event']['detail']['object']['key']

    # Create the response
    response = {
        "object_key": object_key
    }

    return response
