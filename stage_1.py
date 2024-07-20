from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

# Function to validate UTC offset (+/- 2 hours)
def validate_utc_offset(utc_offset):
    try:
        offset = int(utc_offset)
        return abs(offset) <= 2
    except ValueError:
        return False

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters from the URL
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Check if both parameters are provided
    if slack_name is None or track is None:
        return jsonify({"error": "Both 'slack_name' and 'track' parameters are required"}), 400

    # Get current UTC time
    current_time = datetime.now(pytz.utc)
    
    # Get the current day of the week
    current_day = current_time.strftime("%A")
    

    # Use your actual GitHub URLs here
    github_url_file = "https://github.com/Maxidonx/HNG-Task-1/blob/master/stage_1.py"
    github_url_source = "https://github.com/Maxidonx/HNG-Task-1.git"

    
    
    # Create the response JSON
    response_data = {
        "slack_name": slack_name, #displays a set
        "current_day": current_day,
        "utc_time": current_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "track": track,
        "github_file_url": github_url_file,
        "github_repo_url": github_url_source,
        "status_code": 200 #this shows the status of app
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
