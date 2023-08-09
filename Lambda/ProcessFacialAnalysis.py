import boto3

rekognition = boto3.client('rekognition')

def detect_faces(image_bytes):
    # Call AWS Rekognition API for face detection
    response = rekognition.detect_faces(
        Image={
            'Bytes': image_bytes
        },
        Attributes=['ALL']  # To get detailed facial attributes like emotions, landmarks, etc.
    )

    return response

def analyze_facial_attributes(face_details_list):
    # Process the facial attributes detected by Rekognition for each face
    facial_attributes_list = []
    for face_detail in face_details_list:
        age_range = face_detail.get('AgeRange')
        emotions = face_detail.get('Emotions')
        filtered_emotions = []

        if emotions:
            for emotion in emotions:
                confidence = emotion['Confidence']
                if confidence > 50:
                    filtered_emotions.append(emotion['Type'])
                    
                    
        landmarks = face_detail.get('Landmarks')

        # Store the facial attributes in a dictionary for each face
        facial_attributes = {
            'AgeRange': age_range,
            'Emotions': filtered_emotions,
            # 'Landmarks': landmarks,
        }

        # Add other facial attributes here with similar checks
        gender = face_detail.get('Gender')
        if gender:
            facial_attributes['Gender'] = gender['Value']

        smile = face_detail.get('Smile')
        if smile:
            facial_attributes['Smile'] = smile['Value']
            facial_attributes['SmileConfidence'] = smile['Confidence']

        eyeglasses = face_detail.get('Eyeglasses')
        if eyeglasses:
            facial_attributes['Eyeglasses'] = eyeglasses['Value']
            facial_attributes['EyeglassesConfidence'] = eyeglasses['Confidence']


        facial_attributes_list.append(facial_attributes)
    print("facial_attributes_list: ",facial_attributes_list)
    return facial_attributes_list


def lambda_handler(event, context):
    # Extract image bytes from the S3 event
    bucket_name = event['event']['detail']['bucket']['name']
    object_key = event['event']['detail']['object']['key']
    
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket_name, object_key)
    image_bytes = obj.get()['Body'].read()

    # Detect faces in the image
    response = detect_faces(image_bytes)
    
    if 'FaceDetails' in response:
        face_details_list = response['FaceDetails']
        facial_attributes_list = analyze_facial_attributes(face_details_list)
        return {"facial_attributes_list": facial_attributes_list}
    else:
        return {'message': 'No faces detected in the image.'}