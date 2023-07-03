# Hack-Camera-Location-Flask

This project allows users to capture images using their device's front and back cameras, retrieve battery percentage, IP address, and save the captured images along with user data. The application is built using Flask and JavaScript.

## Features

- Capture images using front and back cameras
- Retrieve battery percentage and IP address
- Save images with associated user data
- Password-protected data access

## Requirements

- Python 3.x
- Flask
- JavaScript-enabled web browser

## Installation

1. Clone the repository: git clone https://github.com/soheru/image-capture-data-storage.git
2. Navigate to the project directory: cd HACK-CAMERA-LOCATION-FLASK
3. Install the Python dependencies: pip install -r requirements.txt

## Usage

1. Start the Flask application: python app.py
2. Open a web browser and navigate to `http://localhost:5000` to access the application.
3. Follow the instructions on the webpage to capture images, retrieve battery percentage, and IP address.
4. Access the saved data by visiting `http://localhost:5000/data?password=YOUR_PASSWORD`, where `YOUR_PASSWORD` is the password you set in the application.

## Configuration

In the `app.py` file, you can modify the following configuration options:

- `PASSWORD`: The password required to access the saved data. The default password is set to `NOA`.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.









