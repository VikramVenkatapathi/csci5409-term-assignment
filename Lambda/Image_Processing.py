import boto3
import json

lambda_client = boto3.client('lambda')
rekognition = boto3.client('rekognition')
def lambda_handler(event, context):
    # Extract relevant information from the event
    bucket_name = event['event']['detail']['bucket']['name']
    object_key = event['event']['detail']['object']['key']
    # user_email = object_key.split('/')[0]
    # Detect labels in the image
    response_labels = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': object_key
            }
        },
        MaxLabels=10,
        MinConfidence=70
    )
    print(response_labels)
    # Process the results
    labels = response_labels['Labels']
    
    # Extract labels and their detected confidence levels
    detected_labels = []
    for label in labels:
        label_name = label['Name']
        confidence = label['Confidence']
        detected_labels.append({
            'label': label_name,
            'confidence': confidence
        })

    # Prepare the JSON response
    json_response = {
        'detected_labels': detected_labels
    }
    print(json_response)

    return json_response
