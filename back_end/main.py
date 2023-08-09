from flask import Flask, jsonify

from login_handler import login_handler_app
from registration_handler import registration_handler_app
from imageProcessing_handler import imageProcessing_handler_app

app = Flask(__name__)

# Register login handler app
app.register_blueprint(login_handler_app)

# Register registration handler app
app.register_blueprint(registration_handler_app)

# Register invite users app
app.register_blueprint(imageProcessing_handler_app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
