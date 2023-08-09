from flask import Flask, request, jsonify, Blueprint
import boto3
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)

imageProcessing_handler_app = Blueprint('imageProcessing_handler_app', __name__)


@imageProcessing_handler_app.after_request
def add_headers(response):
    response.headers.add("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers")
    return response

aws_region = 'us-east-1'

# AWS configuration
dynamodb = boto3.resource('dynamodb', region_name=aws_region)
table_name = 'UserRegistration'
bucket_name = 'b00936916-user-images'

@imageProcessing_handler_app.route('/s3_upload', methods=['POST'])
def handleImageProcessing():
    try:
        email = request.form['email']
        image = request.files['image']
        
        # image = request.files.get('image')
        # email = request.args.get('email')
        
        s3 = boto3.client('s3')
        # Generate a unique filename for the image
        filename = secure_filename(image.filename)

        # Create a folder name based on the user's email
        folder_name = email.replace('@', '_').replace('.', '_')

        # Specify the S3 bucket name

        # Create the S3 object key with the folder name and filename
        file_key = f"{folder_name}/{filename}"

        # Upload the image to S3
        s3.upload_fileobj(image, bucket_name, file_key)
        print('Image uploaded to S3:', file_key)

        # Continue with further processing or navigation
        return jsonify({'message': 'Image uploaded successfully'}),200

    except Exception as e:
        print('Error uploading image to S3:', str(e))
        return jsonify({'message': 'Error uploading image to S3'}), 500


# if __name__ == "__main__":
#     app.run("0.0.0.0",port=5002)



"""
All references:
    Flask - (Creating first simple application)
    Reference: `Flask in Python Documentation <https://www.geeksforgeeks.org/flask-creating-first-simple-application//>`_

    Enable Flask-CORS in Python
    Reference: `Flask-CORS in Python Documentation <https://www.geeksforgeeks.org/how-to-install-flask-cors-in-python/>`_

    Add data to Cloud Firestore
    Reference: `Firestore Documentation <https://firebase.google.com/docs/firestore/manage-data/add-data>`_

    Get data with Cloud Firestore
    Reference: `Firestore Documentation <https://firebase.google.com/docs/firestore/query-data/get-data>`_

    Delete data from Cloud Firestore
    Reference: `Firestore Documentation <https://firebase.google.com/docs/firestore/manage-data/delete-data>`_
 
"""