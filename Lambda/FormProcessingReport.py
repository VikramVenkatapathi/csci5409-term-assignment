import boto3
import os
import json

s3 = boto3.client('s3')

def create_file_content(facial_attributes_list, detected_celebrities_list, detected_labels_list, object_key):
    # Format the facial attributes list
    facial_attributes_content = "Facial Attributes List:\n"
    for attributes in facial_attributes_list:
        facial_attributes_content += f"{attributes}\n"

    # Format the detected celebrities list
    detected_celebrities_content = "Detected Celebrities List:\n"
    for celebrity in detected_celebrities_list:
        detected_celebrities_content += f"{celebrity}\n"

    # Format the detected labels list
    detected_labels_content = "Detected Labels List:\n"
    for label in detected_labels_list:
        detected_labels_content += f"{label}\n"

    # Combine all the content with dotted lines
    content = f"{facial_attributes_content}\n{'.'*50}\n\n{detected_celebrities_content}\n{'.'*50}\n\n{detected_labels_content}\n{'.'*50}\n\n"

    return content
    
def lambda_handler(event, context):
    try:
        # input_json = json.dumps(event)
        facial_attributes_json = event[0]
        # Extract relevant information from the input JSON
        facial_attributes_list = facial_attributes_json['facial_attributes_list']
        # facial_attributes_json_final =  facial_attributes_list[0]
        print("facial_attributes_list: ",facial_attributes_list)
        
        detected_celebrities_json = event[1]
        detected_celebrities_list = detected_celebrities_json['detected_celebrities']
        # detected_celebrities_json_final = detected_celebrities_list[0]
        print("detected_celebrities_list: ",detected_celebrities_list)
        
        detected_labels_json = event[2]
        detected_labels_list = detected_labels_json['detected_labels']
        # detected_labels_json_final = detected_labels_list[0]
        print("detected_labels_list: ",detected_labels_list)
        
        object_key = event[3].get('object_key')
        print("object_key: ",object_key)
        
        
        # Create the file content
        file_content = create_file_content(facial_attributes_list, detected_celebrities_list, detected_labels_list, object_key)

        # Create the folder structure using the user's email as the folder name
        user_email = object_key.split('/')[0]
        file_name = os.path.basename(object_key)
        folder_path = f"{user_email}/{file_name}.txt"

        # Upload the file to S3
        bucket_name = "b00936916-user-report"
        s3.put_object(Bucket=bucket_name, Key=folder_path, Body=file_content,ContentDisposition="attachment")

        return {
            'statusCode': 200,
            'body': 'File creation and upload successful!',
            "object_key": object_key
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error occurred: {str(e)}'
        }