
import json

def lambda_handler(event, context):
    # Extract relevant information from the event
    bucket_name = event['detail']['bucket']['name']
    object_key = event['detail']['object']['key']
    
    # Extract email from object key
    # email = object_key.split('/')[0].replace('@', '_')
    
    # Construct the response object with the event information
    response = {
        'statusCode': 200,
        'body': 'Image upload Lambda function executed successfully!',
        'event': event  # Include the entire event object in the response
    }
    
    return response