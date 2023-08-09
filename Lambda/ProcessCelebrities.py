import boto3

rekognition = boto3.client('rekognition')

def lambda_handler(event, context):
    try:
        # Extract relevant information from the event
        bucket_name = event['event']['detail']['bucket']['name']
        object_key = event['event']['detail']['object']['key']

        # Detect celebrities in the image
        response_celebs = rekognition.recognize_celebrities(
            Image={
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': object_key
                }
            }
        )

        # Process the results
        celebrities = response_celebs['CelebrityFaces'] if 'CelebrityFaces' in response_celebs else []

        detected_celebrities = []
        for celebrity in celebrities:
            celebrity_name = celebrity['Name']
            confidence = celebrity['MatchConfidence']

            # Construct the celebrity object for each detected celebrity
            detected_celeb = {
                'name': celebrity_name,
                'confidence': confidence
            }

            # Add the celebrity to the list
            detected_celebrities.append(detected_celeb)
        
        print(detected_celebrities)
        return {
            'detected_celebrities': detected_celebrities
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e)
        }
