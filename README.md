# Flask Endpoint Project

This project demonstrates how to create a simple Flask endpoint that provides specific information in JSON format. It includes details such as Slack name, current day of the week, current UTC time, track, and GitHub URLs.

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python
- Flask
- pytz (for handling timezones)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name


1. ## Create a virtual environment (optional but recommended):

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

2. ## Install the required packages:

    pip install Flask pytz

# Usage
1. Start the Flask application:
    python app.py

2. Open your web browser or use a tool like Postman to make a GET request to the following URL, replacing the placeholders with your information:
        http://localhost:5000/api?slack_name=YourName&track=YourTrack
You will receive a JSON response with the requested information.

# Customization
- To customize the project for your own use, update the values in the app.py file, such as Slack name, GitHub URLs, and any additional data points you want to include in the response.
# Deployment
You can deploy this Flask application to a hosting platform like Heroku for public access.

# Contributing
Feel free to contribute to this project by creating pull requests or reporting issues.