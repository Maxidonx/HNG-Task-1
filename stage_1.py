from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)

# Function to validate UTC offset (+/- 2 hours)
def validate_utc_offset(utc_offset):
    try:
        offset = int(utc_offset)
        return abs(offset) <= 2
    except ValueError:
        return False

@app.route('/get_info', methods=['GET'])
def get_info():
    # Get query parameters from the URL
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    utc_offset = request.args.get('utc_offset')

    # Check if all parameters are provided
    if slack_name is None or track is None or utc_offset is None:
        return jsonify({"error": "All parameters are required"}), 400

    # Validate UTC offset
    if not validate_utc_offset(utc_offset):
        return jsonify({"error": "Invalid UTC offset, must be within +/- 2"}), 400

    # Get current UTC time with the provided offset
    current_time = datetime.now(pytz.utc) + timedelta(hours=int(utc_offset))

    # Get the current day of the week
    current_day = current_time.strftime("%A")

    # Use your actual GitHub URLs here
    github_url_file = "https://github.com/Maxidonx/Back-End-assignment/blob/Maxwell/stage_1.py"
    github_url_source = "https://github.com/Maxidonx/Back-End-assignment.git"

    # Create the response JSON
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "current_utc_time": current_time.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "track": track,
        "github_url_file": github_url_file,
        "github_url_source": github_url_source,
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)