import boto3
import os
import re

s3 = boto3.client('s3')
sns = boto3.client('sns')

def get_user_email(object_key):
    # Extract the email from the object key
    parts = object_key.split('_')
    if len(parts) >= 1:
        user_email = parts[0]
        return user_email
    return None

def get_matching_topics(email):
    # List all SNS topics and filter the ones with the name format "SendDetectionInfoTo<userNamefromEmail>"
    topic_prefix = f"SendDetectionInfoTo{email.split('@')[0]}"
    response = sns.list_topics()
    topics = response.get('Topics', [])
    matching_topics = [topic['TopicArn'] for topic in topics if topic_prefix in topic['TopicArn']]
    
    return matching_topics

def send_notification_to_topics(object_key, topics):
    # Get the S3 bucket name from the object key
    bucket_name = "b00936916-user-report";
    
    # Construct the S3 URL
    s3_url = f"https://{bucket_name}.s3.amazonaws.com/{object_key}.txt"

    # Publish a message to each of the matching topics with the object key as the message body
    message_data = {
            'text': 'Your Image analysis results are ready!\n Please refer to the below attachment for the detection results.',
            'attachment': s3_url
        }
    message = "Your Image analysis results are ready!\n Please visit the URL for the detection results. URL: "+s3_url
    for topic in topics:
        sns.publish(TopicArn=topic, Message=message)

def lambda_handler(event, context):
    try:
        # Extract relevant information from the event
        object_key = event['object_key']
        
        print("object_key: ",object_key)
        # Get the user email from the object key
        user_email = get_user_email(object_key)
        print("user_email: ",user_email)

        if user_email:
            # Get all matching SNS topics with the user email
            matching_topics = get_matching_topics(user_email)
            print("matching_topics: ",matching_topics)

            if matching_topics:
                # Send notification to the matching topics with the object key as the message body
                send_notification_to_topics(object_key, matching_topics)

                return {
                    'statusCode': 200,
                    'body': 'Notification sent successfully!'
                }
            else:
                return {
                    'statusCode': 200,
                    'body': 'No matching topics found for the user!'
                }
        else:
            return {
                'statusCode': 400,
                'body': 'Invalid object key format!'
            }
        return "",200

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error occurred: {str(e)}'
        }
