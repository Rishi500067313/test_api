# app.py
# A simple Flask web server to act as an API endpoint for jackpot events.

from flask import Flask, request, jsonify
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure basic logging to see incoming data in the App Service logs
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    """A simple route for the homepage to show the service is running."""
    return "<h1>Jackpot API is running!</h1><p>Send a POST request to /api/jackpot to submit an event.</p>"

@app.route('/api/jackpot', methods=['POST'])
def receive_jackpot():
    """
    This is the main API endpoint. It listens for POST requests,
    logs the incoming JSON data, and returns a success response.
    """
    if request.is_json:
        # Get the JSON data sent from the Spark job
        data = request.get_json()
        
        # For demo purposes, we'll just log the received data.
        # You can view this log in your Azure App Service's "Log stream".
        app.logger.info("Received jackpot event:")
        app.logger.info(data)
        
        # Send back a success response
        response = {"status": "success", "message": "Jackpot event received"}
        return jsonify(response), 200
    else:
        # Handle cases where the request is not in the correct format
        response = {"status": "error", "message": "Request must be in JSON format"}
        return jsonify(response), 400

# This allows the app to be run directly for testing
if __name__ == '__main__':
    app.run(debug=True)